---
name: cv-builder
description: Use whenever Gaurav asks for a CV, resume, cover letter or application documents, or a job-search task needs them for a job or a funded-startup email. Builds tailored, honest documents from his versioned content library at github.com/gauravbhatia-bit/cv-builder, so facts never drift. Works interactively and in unattended scheduled runs.
---

# CV and cover letter builder

Everything about Gaurav (facts, numbers, dates, titles, projects, wording rules, templates) lives in
one public repo: **github.com/gauravbhatia-bit/cv-builder**. This skill deliberately holds none of it.
A copy here would go stale, and the previous version of this skill did exactly that. If anything in
this file disagrees with the repo, the repo wins.

## 1. Get the repo, fresh, every time

```bash
gh repo clone gauravbhatia-bit/cv-builder cv-builder      # or, without gh:
# fetch https://raw.githubusercontent.com/gauravbhatia-bit/cv-builder/master/<path>
```

Read in this order, and follow them rather than summarising from memory:

1. `CLAUDE.md`: the build procedure. It is the source of truth for the steps below.
2. `RULES.md`: how a job description becomes a CV, bullet budgets, honesty rules, and section 10 (which experience answers which requirement).
3. `STYLE.md`: voice. No em dashes, no banned phrases, plain direct language.
4. `data/master.md` (career) and `data/projects.md` (projects). **The only allowed source of any claim.**
5. `COVER-LETTER-BUILDER.md` and `letters/base.md`: the story bank and the saved base letter.
6. `templates/base.html` (one page, default) or `templates/base-2page.html`.

**If GitHub is unreachable, stop and say so.** Do not fall back to memory or an old copy. A CV built
from stale facts is worse than no CV.

## 2. Build

Work inside the clone's `out/` folder (it is gitignored). In short, per `CLAUDE.md`:

- Read the JD; write the note; check blockers (C1 German, 5+ years, work-authorisation requirements, on-site outside Berlin) and name them to Gaurav before building.
- **Never mention his visa, residence or work-permit status in any CV, letter or email**, and never assert anything about it either way. Availability is a date. If a form or recruiter asks directly, flag it for Gaurav to answer.
- Pick content per `RULES.md` sections 4, 5 and 10. Edit a copy of the template: headline, profile, skills order, bullets, three projects.
- **Cover letter:** start from `letters/base.md`, change only the marked parts, research the company first, use two stories, and **always include the football sentence, linked to a real story**. Under 300 words. Save as `out/Gaurav_Bhatia_Letter_<Company>.md`.
- Names: `Gaurav_Bhatia_CV_<Company>.html` and `.pdf`, plus the letter.

## 3. Verify, then deliver

Run `python scripts/check.py` in the clone. It must report **0 failures** before anything is
attached or sent. It enforces the rules mechanically: em dashes, banned phrases, every CV number
traceable to the data files, unchanged titles and dates, letter length and the football sentence,
no contact details in the repo. If it fails, fix the document. Never loosen the check.

## 4. Contact details and photo: never from the repo

The templates contain `[EMAIL]`, `[PHONE]` and `[PHOTO]` on purpose. Fill them at render time from
the host automation's private configuration (the private `job-search-automation` repo holds them).
Never write a real email, phone or photo into any file that could be committed to the public repo.

## 5. Interactive versus unattended

- **Interactive:** before writing, ask Gaurav (briefly, multiple choice where possible) about format (PDF only unless he says otherwise), language of the ad, any eligibility blocker, and anything the ad asks that the repo does not answer.
- **Unattended (a scheduled task):** you cannot ask. If an open question in `data/master.md` section 2 or a JD blocker affects a line, still draft, put the question in the report, and **never guess**. Do not commit or push to the repo from a task.

## 6. Rendering

The repo's templates are HTML; print to PDF with headless Chrome (`render.cmd` does this on Windows).
If the host automation compiles its own LaTeX (moderncv) template, keep using that layout, but fill it
only from the repo's data and keep the repo's wording rules. One page by default; the two-page
template only where `RULES.md` hard rule 2 allows; never three.

## 7. Keeping this skill current

When his career or projects change, **edit the repo, not this skill**. Update this file only when the
procedure itself changes.
