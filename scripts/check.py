"""Guardrails for the CV repo. Exits 1 if any rule is broken; warnings do not fail.

    python scripts/check.py            static checks (pre-commit hook and GitHub run this)
    python scripts/check.py --render   also render both CVs and check the page counts (Windows + Chrome)

These turn the rules in CLAUDE.md, RULES.md and STYLE.md into something that cannot be forgotten.
"""
import datetime
import html
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "CLAUDE.md", "README.md", "RULES.md", "STYLE.md", "COVER-LETTER-BUILDER.md", "render.cmd",
    "data/master.md", "data/projects.md", "data/.last-sync", "letters/base.md",
    "templates/base.html", "templates/base-2page.html", "scripts/sync_repos.py",
    "skill/cv-builder/SKILL.md",
]
GITIGNORE_MUST_HAVE = ["private/", "out/", "*.pdf"]

# Wording that must never reach an employer (STYLE.md).
BANNED = [
    r"i am writing to apply", r"passionate about", r"dynamic professional", r"team player",
    r"perfect fit", r"results-driven", r"\bmotivated\b", r"proven track record", r"\bleverag",
    r"\bsynerg", r"spearheaded", r"detail-oriented", r"think outside the box",
    r"hit the ground running", r"wealth of experience",
]
# Visa and residence status must never appear in a document (Gaurav's rule, RULES.md hard rule 7).
VISA = [r"\bvisa\b", r"\bpermit\b", r"residen(ce|cy)", r"work authori[sz]ation", r"blue card",
        r"post-study", r"job.?seeker", r"right to work"]
# Things CLAUDE.md says never to write (old claims that were wrong or retired).
FORBIDDEN_IN_CV = ["Croud", "January 2027", "Self-Learning Token", "Data Analyst, Operations"]
# Titles, employers and dates must stay exactly as given (STYLE.md, CV rules).
REQUIRED_IN_CV = [
    "Mar 2024 – Jul 2025", "Nov 2015 – Jan 2024", "Aug 2026 – Present", "Sep 2025 – Dec 2026",
    "Operations & Supply Chain Analyst", "Business Manager", "Data Science Intern", "KnowGuard AI",
    "Troika International Pvt. Ltd.", "Bhatia Traders", "GISMA", "Civil Engineering", "December 2026",
    "[EMAIL]", "[PHONE]", "[PHOTO]",
]
PAGES = {"templates/base.html": 1, "templates/base-2page.html": 2}
LETTER_WORD_LIMIT = 300
PHONE = re.compile(r"\+\d{2}[ \d]{9,}")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
EMAIL_OK = {"noreply@anthropic.com", "example@example.com"}


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8").replace("\r\n", "\n")


def visible_text(page):
    page = re.sub(r"<(style|script)\b.*?</\1>|<!--.*?-->|<div id=\"bar\">.*?</div>", " ", page, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", " ", page))


def banned_in(text):
    return [b for b in BANNED if re.search(b, text, re.I)] + [
        f"{v} (never mention visa or residence status)" for v in VISA if re.search(v, text, re.I)
    ]


def untraceable_numbers(text, sources):
    """Numbers on a CV that appear in no data file. Single digits are skipped as noise."""
    toks = {t.rstrip(",.") for t in re.findall(r"\d[\d,]*\.?\d*", text)}
    return sorted(t for t in toks if len(t) >= 2 and t not in sources)


def letter_problems(text, is_base=False):
    body = text.split("\n---\n", 1)[1] if "\n---\n" in text else text
    out = []
    words = len(body.split())
    if words > LETTER_WORD_LIMIT:
        out.append(f"{words} words, limit {LETTER_WORD_LIMIT}")
    if "—" in body:
        out.append("contains an em dash")
    out += [f"banned phrase /{b}/" for b in banned_in(body)]
    if "football" not in body.lower():
        out.append("no football sentence (always required)")
    if not is_base and re.search(r"\[(WHY|PROOF|LINK|Company|Role)\]", body):
        out.append("unresolved [WHY]/[PROOF]/[LINK]/[Company]/[Role] marker")
    return out


def has_control_chars(text):
    """A broken escape sequence leaves invisible characters (backspace, form feed) in a file."""
    return bool(re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", text))


def skill_problems(text):
    """The skill must point at the repo and hold no facts of its own, or it drifts (the old one did)."""
    out = []
    m = re.match(r"---\nname: [\w-]+\ndescription: (.+)\n---\n", text)
    if not m:
        out.append("frontmatter must be exactly --- name, description ---")
    elif len(m.group(1)) > 1024:
        out.append("description is over 1024 characters")
    if "github.com/gauravbhatia-bit/cv-builder" not in text:
        out.append("does not point at the cv-builder repo")
    out += [f"holds a date or year {y!r}: facts belong in the repo" for y in sorted(set(re.findall(r"\b20\d\d\b", text)))]
    out += [f"contains retired claim {s!r}" for s in FORBIDDEN_IN_CV if s in text]
    return out


def tracked_files():
    run = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True)
    if run.returncode:
        return [str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]
    return run.stdout.split()


def run_checks(render=False):
    fails, warns = [], []

    for f in REQUIRED_FILES:
        if not (ROOT / f).exists():
            fails.append(f"missing file: {f}")

    ignore = read(".gitignore").splitlines() if (ROOT / ".gitignore").exists() else []
    fails += [f".gitignore must contain {g}" for g in GITIGNORE_MUST_HAVE if g not in ignore]

    files = tracked_files()
    for f in files:
        if f.lower().endswith((".pdf", ".jpg", ".jpeg", ".png")) or f.startswith(("private/", "out/")):
            fails.append(f"must never be tracked (carries personal details): {f}")

    # Personal details must not appear in any tracked text file.
    secrets = []
    contact = ROOT / "private" / "contact.md"
    if contact.exists():
        c = contact.read_text(encoding="utf-8")
        secrets = [m.strip() for m in re.findall(r"\|\s*(?:Email|Mobile)\s*\|\s*([^|]+?)\s*\|", c)]
    for f in files:
        if not f.lower().endswith((".md", ".html", ".py", ".cmd", ".json", ".yml", ".txt")) and f != ".gitignore":
            continue
        if f == "scripts/check.py":
            continue
        text = read(f)
        if has_control_chars(text):
            fails.append(f"{f}: contains an invisible control character (a broken escape sequence)")
        fails += [f"{f}: contains a private contact detail" for s in secrets if s and s in text]
        fails += [f"{f}: looks like a phone number {m.strip()!r}" for m in PHONE.findall(text)]
        fails += [f"{f}: looks like an email address {m!r}" for m in EMAIL.findall(text) if m not in EMAIL_OK]

    # CV templates.
    sources = read("data/master.md") + read("data/projects.md")
    for t in PAGES:
        if not (ROOT / t).exists():
            continue
        text = visible_text(read(t))
        raw = read(t)
        if "—" in text:
            fails.append(f"{t}: contains an em dash")
        fails += [f"{t}: banned phrase /{b}/" for b in banned_in(text)]
        fails += [f"{t}: forbidden text {s!r}" for s in FORBIDDEN_IN_CV if s in text]
        fails += [f"{t}: required text missing {s!r}" for s in REQUIRED_IN_CV if s not in text and s not in raw]
        fails += [f"{t}: number {n} is in no data file (every number must be traceable)" for n in untraceable_numbers(text, sources)]

    # Cover letters: the saved ones, plus any custom ones kept locally in out/.
    letters = [(f, f == "letters/base.md") for f in files if f.startswith("letters/") and f.endswith(".md")]
    out = ROOT / "out"
    if out.exists():
        # custom letters are named Gaurav_Bhatia_Letter_<Company>.md; other notes in out/ are left alone
        letters += [(str(p.relative_to(ROOT)).replace("\\", "/"), False) for p in out.glob("*[Ll]etter*.md")]
    for f, is_base in letters:
        fails += [f"{f}: {p}" for p in letter_problems(read(f), is_base)]

    skill = "skill/cv-builder/SKILL.md"
    if (ROOT / skill).exists():
        fails += [f"{skill}: {p}" for p in skill_problems(read(skill))]

    # Data files: stable project IDs, and every reference resolves.
    projects = read("data/projects.md")
    table = re.search(r"^\| # \| Project \|.*?\n\n", projects, re.S | re.M)  # the library table only
    rows = re.findall(r"^\| P\d+ \|.*$", table.group(0), re.M) if table else []
    ids = [re.match(r"\| (P\d+) \|", r).group(1) for r in rows]
    if not rows:
        fails.append("projects.md: library table not found")
    fails += [f"projects.md: duplicate project ID {i}" for i in sorted({i for i in ids if ids.count(i) > 1})]
    for row in rows:
        if len(row.strip("|").split("|")) != 6:
            fails.append(f"projects.md: row does not have 6 columns: {row[:40]}...")
    for f in ("RULES.md", "COVER-LETTER-BUILDER.md"):
        for ref in sorted(set(re.findall(r"\bP(\d+)\b", read(f)))):
            if f"P{ref}" not in ids:
                fails.append(f"{f}: refers to P{ref}, which is not in projects.md")

    sync = (ROOT / "data" / ".last-sync")
    if sync.exists():
        try:
            age = (datetime.date.today() - datetime.date.fromisoformat(sync.read_text().strip())).days
            if age > 14:
                warns.append(f"projects last reviewed against GitHub {age} days ago: run scripts/sync_repos.py")
        except ValueError:
            fails.append("data/.last-sync is not a valid YYYY-MM-DD date")

    for py in (ROOT / "scripts").glob("*.py"):
        try:
            compile(py.read_text(encoding="utf-8"), str(py), "exec")
        except SyntaxError as e:
            fails.append(f"{py.name}: {e}")

    if render:
        fails += render_checks(warns)
    return fails, warns


def render_checks(warns):
    if sys.platform != "win32":
        warns.append("--render needs Windows and Chrome; page counts were not checked")
        return []
    fails = []
    for t, want in PAGES.items():
        run = subprocess.run(["cmd", "/c", str(ROOT / "render.cmd"), str(ROOT / t)], capture_output=True, text=True)
        pdf = ROOT / "out" / (pathlib.Path(t).stem + ".pdf")
        if run.returncode or not pdf.exists():
            fails.append(f"{t}: render failed. {run.stdout.strip()} {run.stderr.strip()}")
            continue
        got = len(re.findall(rb"/Type\s*/Page[^s]", pdf.read_bytes()))
        if got != want:
            fails.append(f"{t}: renders to {got} pages, must be {want}")
    return fails


if __name__ == "__main__":
    fails, warns = run_checks(render="--render" in sys.argv)
    for w in warns:
        print(f"warning: {w}")
    for f in fails:
        print(f"FAIL: {f}")
    print(f"\n{len(fails)} failure(s), {len(warns)} warning(s)")
    sys.exit(1 if fails else 0)
