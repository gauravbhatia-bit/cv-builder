# How to build a tailored CV in this repo

Instructions for Claude. Gaurav reads `README.md`; this file is the working procedure.

## Repo map

| Path | What it is |
|---|---|
| `data/master.md` | Identity, experience, education, skills, certifications. **The career half of the source of truth.** |
| `data/projects.md` | Every project: tags, stack, metrics, repos, bullet bank. **The only source of project content.** |
| `RULES.md` | How a JD becomes a CV. Bullet budgets, project picking, honesty guardrails. §10 maps JD requirements to the right experience. |
| `COVER-LETTER-BUILDER.md` | The stories behind the facts, for cover letters. Narrative only, never a source of a number. |
| `STYLE.md` | How everything is written. Gaurav's own voice rules. Overrides any default phrasing. |
| `templates/base.html` | The neutral base CV, **one page**, 3 projects. The default. |
| `templates/base-2page.html` | **Two-page** variant, 9 projects in priority order, thesis permanent, fuller experience bullets. For roles where project depth is the evidence. |
| `jd/` | One markdown note per job description, before building. |
| `out/` | Finished CVs. **Gitignored** — these carry real contact details. |
| `private/contact.md` | Real email and phone. **Gitignored.** |

## Procedure

1. **Read the JD.** Write `jd/<company>-<role>.md` using the extraction table in `RULES.md` §1.
2. **Check blockers.** C1 German, 5+ years, existing permit, on-site outside Berlin. Say so before building.
3. **Check open questions.** `master.md` §2. If a `G#` affects a line on this CV, ask Gaurav first — do not guess.
4. **Pick content** per `RULES.md` §4 and §5. Write the picks into the JD note so the choice is reviewable.
5. **Build.** `cp templates/base.html out/Gaurav_Bhatia_CV_<Company>.html`, then edit:
   - `<h2>` right after the header block = the headline. Match the JD's job title.
   - The `<p>` under it = the Profile. Rewrite per `RULES.md` §3.
   - Reorder `<dt>/<dd>` skill rows; the JD's top requirement goes first.
   - Trim/swap `<li>` bullets to the budget.
   - Swap the three `.entry` project blocks.
   - Set `<title>` — the "Save edited HTML" button uses it as the filename.
6. **Verify** against the checklist in `RULES.md` §9.
7. **Cover letter**, if one is wanted: `COVER-LETTER-BUILDER.md`. Research the company first, pick two stories via `RULES.md` §10, respect each story's stated limit.
8. **Report** to Gaurav: what was picked, what was cut, and anything that had to be left out for honesty.
8. **Commit and push.** One commit per application: `cv: <Company> <Role>`.

## Voice

`STYLE.md` governs every word that reaches an employer. Read it before writing a CV or a cover
letter. The rule that breaks most drafts: **no em dashes.** Reword the sentence; do not swap in a
hyphen. En dashes in ranges (`Aug 2026 – Present`) are fine.

## Photo

Optional and **off by default**. Drop a `photo.jpg`, `.jpeg` or `.png` into `private/` and
`render.cmd` embeds it top-right as base64; with no such file the `[PHOTO]` placeholder is removed
and the layout is unchanged. `private/` is gitignored, so the photo never reaches GitHub.

A photo costs about **54px**, roughly two bullets, on the one-page CV, which normally runs with
only ~18px spare. The two-page version absorbs it without trouble. If Gaurav wants a photo on the
one-pager, cut per `RULES.md` §4 rather than shrinking below 9pt.

## Contact details

The committed template carries `[EMAIL]` and `[PHONE]` placeholders, never the real values.
`render.cmd` substitutes them from `private/contact.md` at render time, so the PDF is complete
while the repo stays clean. If a CV is edited by hand in the browser instead of rendered,
the real details have to be typed in — the placeholders must never reach an employer.

Both `private/` and `out/` are gitignored. Never commit a file containing the phone number or
email, and never paste either into `data/master.md`, `RULES.md` or a `jd/` note.

**Settled, do not raise again:** commits `b4ea0d3`, `7d49d07` and `576fa84` predate the masking and
still carry the phone number. They are off the branch but remain fetchable from GitHub by direct SHA.
Gaurav weighed this on 30 Oct 2026 and chose to leave them. The rule above still applies to every
new commit.

## One page

The template holds one page at its defaults (`--fs: 9.5pt`, `--gap: 2px`) with 3 jobs, 3 projects and 6 skill rows — that is already tight, so anything added must displace something. Check with `render.cmd` and count pages before handing over. Below 9pt, cut content instead — see `RULES.md` §4.

## Keeping the data current

When Gaurav mentions a new job, project, repo or metric, write it down **in the same turn**, then commit — a project goes in `data/projects.md`, anything else in `data/master.md`. Never both. This repo is public on GitHub so the content library is reachable from any machine — fetch `data/master.md`, `data/projects.md` and `RULES.md` raw from `github.com/gauravbhatia-bit/cv-builder` when the local copy is not available.

**P22's test results are due within days of 30 Oct 2026.** Ask for the measured token reduction and the quality guard before the next CV goes out, and record them in `projects.md`.

## Do not

- Invent a metric, tool, date or title.
- Drop a job to save space.
- Go to three pages. Two is allowed via `templates/base-2page.html`; see `RULES.md` hard rule 2 for when.
- Put anything in this repo that should not be public — it is a public repo.
- Source anything from the Apr 2026 hospitality CVs — their *dates* are wrong, though their pre-2020 roles are real side ventures. See `master.md` §2.
- Shorten "Deloitte Data Analytics Job Simulation" to "Deloitte Data Analytics".
- Re-add **Croud Control** as a job. He is registered on the marketplace with nothing delivered. `master.md` §4 says why.
- Put **SQL** in a Troika bullet, or **Power BI** in a Bhatia Traders bullet. Neither is true. `master.md` §4 says why.
- Write "January 2027" as the availability. It is **December 2026**.
