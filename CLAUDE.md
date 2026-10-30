# How to build a tailored CV in this repo

Instructions for Claude. Gaurav reads `README.md`; this file is the working procedure.

## Repo map

| Path | What it is |
|---|---|
| `data/master.md` | Every fact, bullet, project and metric. **The only allowed source of CV content.** |
| `RULES.md` | How a JD becomes a CV. Bullet budgets, project picking, honesty guardrails. |
| `templates/base.html` | The neutral base CV. Rezume style, editable in a browser, prints to A4. |
| `jd/` | One markdown note per job description, before building. |
| `out/` | Finished CVs, one HTML per application. Open and Ctrl+P to get the PDF. |

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
7. **Report** to Gaurav: what was picked, what was cut, and anything that had to be left out for honesty.
8. **Commit and push.** One commit per application: `cv: <Company> <Role>`.

## One page

The template holds one page at `--fs: 10pt` / `--gap: 7px` with 4 jobs, 3 projects and 6 skill rows. If it spills, drop `--fs` to 9.5pt and `--gap` to 5px before cutting content. Below 9pt, cut content instead — see `RULES.md` §4.

## Keeping the data current

When Gaurav mentions a new job, project, repo or metric, add it to `data/master.md` **in the same turn**, then commit. This repo is public on GitHub so the content library is reachable from any machine — fetch `data/master.md` and `RULES.md` raw from `github.com/gauravbhatia-bit/cv-builder` when the local copy is not available.

## Do not

- Invent a metric, tool, date or title.
- Drop a job to save space.
- Go to two pages.
- Put anything in this repo that should not be public — it is a public repo.
