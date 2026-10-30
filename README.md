# CV Builder — Gaurav Bhatia

A content library plus a print-ready HTML template, so every job application gets a CV tailored to its job description without rewriting anything from scratch.

## Make a CV for a job

Paste the job description into a Claude session opened on this folder. Claude reads `CLAUDE.md`, follows `RULES.md`, picks content from `data/master.md` and `data/projects.md`, and writes `out/Gaurav_Bhatia_CV_<Company>.html`.

Then open that file in Chrome → **Print / Save as PDF** → destination "Save as PDF", margins **Default**, **uncheck** "Headers and footers".

## Edit by hand

Every CV file is editable in the browser. Click any text and type. The toolbar at the top adjusts text size and spacing to fit one page, and **Save edited HTML** downloads the edited file so the change can be committed. The toolbar does not print.

## What is where

| Path | What it holds |
|---|---|
| `data/master.md` | Your career: jobs, bullets, education, skills. The source of truth. |
| `data/projects.md` | Every project, with what it proves and which roles it suits. |
| `RULES.md` | How a job description turns into a CV. §10 says which of your experiences answers which requirement. |
| `COVER-LETTER-BUILDER.md` | Your career stories, written up for cover letters: what happened, what it proves, when to use it. |
| `STYLE.md` | Your voice rules. Applied to every CV and letter. |
| `letters/` | `base.md` is your saved base cover letter. `sample-energy-analyst.md` shows a finished custom one. |
| `scripts/sync_repos.py` | Checks GitHub against your project list. Reports only, never edits. |
| `render.cmd` | Turns the HTML CVs into PDFs, filling in your photo and contact details. |
| `templates/base.html` | The one-page base CV. The default. |
| `templates/base-2page.html` | The two-page version, 9 projects including your thesis. For roles where the project detail is the point. |
| `jd/` | Notes on each job description. |
| `out/` | Finished CVs. |
| `CLAUDE.md` | Procedure Claude follows. |

## Adding or changing a project

Edit `data/projects.md` only. Add a new project as the next number (P24, P25 ...), edit one in place,
never renumber. To pick up what changed on GitHub, run `python scripts/sync_repos.py`: it lists new
repos and repos you pushed to since the last review, and Claude reads their READMEs and updates the
file. It is deliberately not fully automatic, so a README edit can never quietly rewrite a claim on
your CV. The two CV templates carry copies of the projects they show, so ask for them to be refreshed
when one of those changes.

To make PDFs, run `C:\Users\gaura\cv-builder\render.cmd` from any folder.

## Using this from your job-search automation

`skill/cv-builder/SKILL.md` packages this whole project as a Claude skill, named `cv-builder`. It holds no
facts on purpose: it tells the agent to fetch this repo fresh, follow `CLAUDE.md`, and run the
guardrail check before delivering. So when your career or projects change, you edit the repo and
every automation that uses the skill is current. To attach it:

1. Upload `out/cv-builder.zip` in Claude (Customize, Skills). It has a different name from the old
   `cv-cover-letter-builder`, so both can be attached at once. **Detach the old one**: it carries stale facts.
2. Optionally mirror `SKILL.md` into `skills/cv-builder/` in `job-search-automation`, through that
   repo's own release process, and remove its old `skills/cv-cover-letter-builder/` folder.
3. In any task prompt that builds documents, say: "Use the cv-builder skill for every CV and cover letter."

Rebuild the zip after changing the skill: it is one file in a folder, zipped.

**In Claude Code on this machine** it is installed as a folder link, `C:\Users\gaura\.claude\skills\cv-builder`,
pointing at `skill\cv-builder` in this repo, so the installed skill is always the repo's file and cannot
drift. Claude Code reads skills when a session starts, so it appears in new sessions. On another machine,
clone the repo and run, in PowerShell: `New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\cv-builder" -Target "<repo>\skill\cv-builder"`.

## Guardrails

So the quality cannot slip, `scripts/check.py` enforces the rules automatically: no em dashes or
buzzwords, every number on the CV traceable to your data files, job titles and dates unchanged,
letters under 300 words with the football sentence, no contact details in the repo, and the right
page count. It blocks a bad commit on your machine and runs on GitHub on every push. Run it yourself
with `python scripts/check.py --render`. On a new machine, run `git config core.hooksPath scripts/hooks` once.

## Cover letters

`COVER-LETTER-BUILDER.md` holds nine stories from your career, each with what it proves, when to
reach for it, and where the honest limit is. Ask for a cover letter and it gets used automatically —
two stories per letter, picked against the job ad and the company.

## Open questions

`data/master.md` §2 lists facts still needed before certain lines can go on a CV. None are open
right now; the career walkthrough cleared the last of them.
