# CV Builder — Gaurav Bhatia

A content library plus a print-ready HTML template, so every job application gets a CV tailored to its job description without rewriting anything from scratch.

## Make a CV for a job

Paste the job description into a Claude session opened on this folder. Claude reads `CLAUDE.md`, follows `RULES.md`, picks content from `data/master.md`, and writes `out/Gaurav_Bhatia_CV_<Company>.html`.

Then open that file in Chrome → **Print / Save as PDF** → destination "Save as PDF", margins **Default**, **uncheck** "Headers and footers".

## Edit by hand

Every CV file is editable in the browser. Click any text and type. The toolbar at the top adjusts text size and spacing to fit one page, and **Save edited HTML** downloads the edited file so the change can be committed. The toolbar does not print.

## What is where

| Path | What it holds |
|---|---|
| `data/master.md` | Every job, bullet, project, metric and link. The source of truth. |
| `RULES.md` | How a job description turns into a CV. |
| `templates/base.html` | The neutral base CV. |
| `jd/` | Notes on each job description. |
| `out/` | Finished CVs. |
| `CLAUDE.md` | Procedure Claude follows. |

## Open questions

`data/master.md` §2 lists facts still needed before certain lines can go on a CV. Worth clearing.
