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
git clone https://github.com/gauravbhatia-bit/cv-builder.git cv-builder
# gh repo clone also works locally, but is blocked in cloud sessions. Last resort, per file:
# https://raw.githubusercontent.com/gauravbhatia-bit/cv-builder/master/<path>
```

Read in this order, and follow them rather than summarising from memory:

1. `CLAUDE.md`: the build procedure. It is the source of truth for the steps below.
2. `RULES.md`: how a job description becomes a CV, bullet budgets, honesty rules, and section 10 (which experience answers which requirement).
3. `STYLE.md`: voice. No em dashes, no banned phrases, plain direct language.
4. `data/master.md` (career) and `data/projects.md` (projects). **The only allowed source of any claim.**
5. `COVER-LETTER-BUILDER.md` and `letters/base.md`: the story bank and the saved base letter.
6. `templates/base-2page.html` (two pages, the default), `templates/base.html` (one page, only on request) and `templates/letter.html` (letter page with the photo header).

**If GitHub is unreachable, stop and say so.** Do not fall back to memory or an old copy. A CV built
from stale facts is worse than no CV.

## 2. Build

Work inside the clone's `out/` folder (it is gitignored). In short, per `CLAUDE.md`:

- Read the JD; write the note; check blockers (C1 German, 5+ years, work-authorisation requirements, on-site outside Berlin) and name them to Gaurav before building.
- **Never mention his visa, residence or work-permit status in any CV, letter or email**, and never assert anything about it either way. Availability is a date. If a form or recruiter asks directly, flag it for Gaurav to answer.
- **Fast path first (saves tokens):** `RULES.md` section 12 maps job families to eight ready-made two-page CVs in `roles/`. If the job fits one, copy that file to `out/`, set the headline to the ad's job title, run the check and render. Do not re-read the data files or re-pick projects. Fall through to the full build below only when section 12 says to.
- Pick content per `RULES.md` sections 4, 5 and 10. **Two pages is the default:** edit a copy of `templates/base-2page.html` (headline, profile, skills order, bullets, project order). Use the one-page `templates/base.html` only when the ad or Gaurav asks for one page.
- **Cover letter:** start from `letters/base.md`, change only the marked parts, research the company first, use two stories, and **always include the football sentence, linked to a real story**. Under 300 words. Save as `out/Gaurav_Bhatia_Letter_<Company>.md`, then run `python scripts/build_letter.py out/Gaurav_Bhatia_Letter_<Company>.md "<Company>"` to get the designed letter page with the same photo header as the CV.
- Names: `Gaurav_Bhatia_CV_<Company>.html` and `.pdf`, and `Gaurav_Bhatia_Letter_<Company>.md`, `.html` and `.pdf`.

## 3. Cold emails: always attach the CV

Whenever you send a cold email to a startup, **attach the tailored CV as a PDF**, and put his
portfolio link in the body. Build the CV first by the steps above, make sure the check passes, and
render it to exactly two pages. Attach it through the email tool's attachments (base64 PDF named
`Gaurav_Bhatia_CV_<Company>.pdf`, under 25 MB). A link is not a substitute. If the CV cannot be built
or attached, **do not send**: save a draft and say why in the report. The full rule is `RULES.md`
section 11, and the repo wins if it differs from this file.

## 4. Verify, then deliver

Run `python scripts/check.py` in the clone. It must report **0 failures** before anything is
attached or sent. It enforces the rules mechanically: em dashes, banned phrases, every CV number
traceable to the data files, unchanged titles and dates, letter length and the football sentence,
no contact details in the repo. If it fails, fix the document. Never loosen the check.

## 5. Photo from the repo; contact details never from the repo

**Photo:** always `assets/photo.jpg` in the repo. It is public on purpose. Every CV template and the
letter template already point at it (`src="../assets/photo.jpg"`), so a fresh clone has it. Never
leave it off, and never take a photo from anywhere else.

**Contact details:** the templates contain `[EMAIL]` and `[PHONE]` on purpose. Fill them at render
time from private configuration (`private/contact.md` on Gaurav's laptop, or the private
`job-search-automation` repo). Never write a real email or phone into any file that could be
committed to the public repo.

## 6. Interactive versus unattended

- **Interactive:** before writing, ask Gaurav (briefly, multiple choice where possible) about format (PDF only unless he says otherwise), language of the ad, any eligibility blocker, and anything the ad asks that the repo does not answer.
- **Unattended (a scheduled task):** you cannot ask. If an open question in `data/master.md` section 2 or a JD blocker affects a line, still draft, put the question in the report, and **never guess**. Do not commit or push to the repo from a task.

## 7. Rendering

The repo's templates are HTML; print to PDF with headless Chrome. On Windows `render.cmd` does it and
embeds the photo. Elsewhere, render the file **from inside `out/`** (so `../assets/photo.jpg`
resolves) with headless Chromium or Playwright, A4, and count the pages of the PDF.
If the host automation compiles its own LaTeX (moderncv) template, keep using that layout, but fill it
only from the repo's data and keep the repo's wording rules. **Two pages by default**, exactly two;
one page only when asked; never three. The cover letter is always one page. Check the photo is
visible on both before delivering.

## 8. Keeping this skill current

When his career or projects change, **edit the repo, not this skill**. Update this file only when the
procedure itself changes.
