"""Compare GitHub against data/projects.md. Changes nothing; it only tells you what to review.

    python scripts/sync_repos.py          report new repos and repos pushed since the last review
    python scripts/sync_repos.py --done   record today as reviewed

A repo counts as known if its name appears anywhere in data/projects.md (library table, bullets
or the "Do not list" line). Private repo names only ever print here; nothing is written to the repo
except the date in data/.last-sync.
"""
import datetime
import json
import pathlib
import subprocess
import sys

USER = "gauravbhatia-bit"
ROOT = pathlib.Path(__file__).resolve().parent.parent
STAMP = ROOT / "data" / ".last-sync"

if "--done" in sys.argv:
    STAMP.write_text(datetime.date.today().isoformat() + "\n")
    print(f"Recorded {STAMP.read_text().strip()} as the last review.")
    sys.exit()

run = subprocess.run(
    ["gh", "repo", "list", USER, "--limit", "200", "--json", "name,isPrivate,pushedAt,description"],
    capture_output=True, text=True,
)
if run.returncode:
    sys.exit(f"gh failed (is it installed and logged in? try `gh auth status`):\n{run.stderr}")

repos = json.loads(run.stdout)
known = (ROOT / "data" / "projects.md").read_text(encoding="utf-8")
since = STAMP.read_text().strip() if STAMP.exists() else None

new = [r for r in repos if r["name"] not in known]
# >= so a push later on the day of the last review is not missed
changed = [r for r in repos if r["name"] in known and r["name"] not in (ROOT.name, USER) and since and r["pushedAt"][:10] >= since]


def show(title, rows):
    print(f"\n{title}" if rows else f"\n{title.split(' (')[0]}: none")
    for r in sorted(rows, key=lambda r: r["pushedAt"], reverse=True):
        tag = "private" if r["isPrivate"] else "public "
        print(f"  {r['pushedAt'][:10]}  {tag}  {r['name']}  {(r['description'] or '')[:60]}")


show("NEW (not mentioned in data/projects.md)", new)
if since:
    show(f"CHANGED (pushed on or after {since})", changed)
else:
    print("\nNo baseline yet, so showing NEW only. Run with --done after reviewing.")
if new or changed:
    print("\nFor each: read its README, update data/projects.md, then run with --done.")
