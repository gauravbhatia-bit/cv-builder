# CV Tailoring Rules

How a job description turns into a CV. Read with `data/master.md` (career),
`data/projects.md` (projects) and **`STYLE.md` (voice, which overrides everything here on wording)**.

---

## 0. Hard rules — never break these

1. **Nothing goes on a CV that is not in `data/master.md` or `data/projects.md`.** No invented metrics, tools, dates or titles.
2. **Two pages by default** (`templates/base-2page.html`, the full project set, thesis permanent). Gaurav's decision, 30 Oct 2026, replacing the earlier one-page default; it applies to German applications too. Use the **one-page** `templates/base.html` only when the ad or the portal asks for a one-page CV, or Gaurav asks for one. Never three.
3. **Never remove a job to save space.** Gaps look worse than a less relevant role. Shrink it to one bullet instead. The one exception is an entry with **nothing delivered** — Croud Control is registered-but-idle and is off the CV for that reason, not for space. See `master.md` section 4.
4. **Every number on the CV must be traceable** to a README, a dashboard or a report. If a number cannot be shown in an interview, it does not go on. **This bans unprovable numbers, not projects without one** — in-progress work goes on the CV described by its *scope* (sources, geography, window, techniques) in the present tense. Add the number when it exists. See `projects.md` → In-flight.
5. **Do not claim German above A2** and do not hide it either. It is on the CV as A2, improving.
6. If an open question in `master.md` section 2 blocks a line, **ask — do not guess**.
7. **Never mention visa, residence or work-permit status** in a CV, cover letter or outreach email (Gaurav's rule, 30 Oct 2026). Availability is a date ("available from December 2026"), never a permit. This is about not volunteering it in writing: if a form or recruiter asks directly, Gaurav answers that himself and accurately. Never assert anything about his status either way. `check.py` enforces it.

---

## 1. Read the JD in this order

Write the answers into `jd/<company>-<role>.md` before building anything.

| Step | What to extract |
|---|---|
| 1 | **Role family** — DA / DS / AI / EN / BIZ (tags are defined in both data files). Often two. |
| 2 | **Top 5 hard requirements** — the tools and methods named in "Your profile" / "Requirements". |
| 3 | **Exact keyword spellings** — "Power BI" vs "PowerBI", "A/B testing" vs "experimentation". Copy their spelling into the CV. ATS matches strings. |
| 4 | **Domain** — energy, fintech, e-commerce, logistics, SaaS, consulting. This decides which projects get picked. |
| 5 | **Seniority** — junior / working student / mid. If mid+ and asking for 3-5 years, lead with Troika and Bhatia Traders, not the internship. |
| 6 | **Language** — if the JD is in German, the CV stays in English but mirror German technical terms where natural, and address the German level in the cover letter. |
| 7 | **Blockers** — needs C1 German? needs EU citizenship or an existing work authorisation? 5 years required? Note it **in the JD note for Gaurav only**, never in a document. A blocker may mean "do not apply". |

---

## 2. What changes per JD, what never changes

| Section | Changes? | How |
|---|---|---|
| Name, contact, links | Never | Fixed block |
| **Headline** (line under name) | **Always** | Match the JD's own job title where honest. "Data Analyst" for a DA role, not "Data Scientist". |
| **Profile** (3 lines) | **Always** | Rewritten per JD. See section 3. |
| Education | Rarely | Swap thesis variant: short for DA/BIZ, long for EN/DS. |
| **Skills rows** | **Always** | Reorder rows so the JD's top requirement is in row 1. Cut rows the JD never mentions. |
| Experience — roles & dates | Never | All four roles always appear |
| **Experience — bullets** | **Always** | Pick from the superset by tag. Budget below. |
| **Projects** | **Always** | Pick 3 by tag + domain. This is the single biggest lever. |
| Certifications | Rarely | Drop if space is tight and the JD is not cloud/data-eng |

---

## 3. The Profile paragraph

Three lines, roughly 45 words. Formula:

> `[What I am today]` + `[the 3 skills the JD asks for most, in their words]` + `[a proof number]` + `[availability]`

Rules:
- Line 1 names the role the JD is hiring for. If they want a Data Analyst, the first words are about analysis, not about AI.
- Include **one** concrete number. Rotate it to match the role: 91.1% QA score for DA, 6.07% MAPE for DS, 55.7% repricing for BIZ, 4,444 headlines for AI, 26,280 hourly rows for EN.
- Always end with: `Available full-time in Berlin from December 2026.`
- Never write "passionate", "motivated", "team player", "results-driven".

---

## 4. Bullet budget

**Two-page CV (the default):** start from `templates/base-2page.html`, which already holds the full experience bullets and the project set in priority order. Tailor by reordering projects so the JD's three strongest come first, swapping the weakest for a better match, and trimming bullets that do not serve this JD. It must still land on exactly two pages, never spilling onto a third.

**One-page CV (only on request), fits reliably:**

Three roles, not four — Croud Control is off the CV (hard rule 3).

| Role | DA / BI | DS / ML | AI / GenAI | Energy | BIZ |
|---|---|---|---|---|---|
| KnowGuard AI (intern) | 2 | 3 | 3 | 2 | 1 |
| Troika International | 3 | 2 | 2 | 2 | 3 |
| Bhatia Traders | 2 | 1 | 1 | 1 | 3 |
| **Projects shown** | 3 | 3 | 3 | 3 | 3 |
| Bullets per project | 2 | 2 | 2 | 2 | 2 |

For **BIZ** roles, one of the three Troika bullets must be the ₹2.75M export order and one of the three Bhatia bullets must be the side ventures. Those two lines are what separate him from an analyst who has only ever reported on someone else's decisions.

If it spills past one page, cut in this order: **any bullet without a number** → the 2nd bullet of project 3 → the weakest Bhatia Traders bullet → a skills row → Certifications. Keep Certifications if the JD mentions cloud or data engineering. Never shrink the Profile below 3 lines; never drop a project to 1 bullet.

Before cutting content, try `--fs: 9.5pt` / `--gap: 2px` (the template defaults — these already fit the base CV on one A4 page). Below 9pt, cut content instead.

---

## 5. Project picking

Pick from `data/projects.md`. Rank by `tag match + domain match + has a number`. Take the top 3, then apply:

- **Never show 3 projects of the same type.** Two in the JD's area, one that shows range.
- **Prefer a current project where it fits.** P20–P22 are live work, described in the present tense, and they are products rather than analyses. For AI, LLM, platform or startup roles they outrank most of P1–P19 even without final numbers — "currently building" is a strength, not a hedge.
- **Domain beats tag.** Applying to an energy company? P4/P5/P6/P7 go first even for a DA role — use P11 (DuckDB SQL + Power BI) as the analyst proof.
- **The thesis is permanent.** It appears in Selected Projects on every CV that shows more than three projects, and always stays in Education. It is Gaurav's flagship and his clearest domain claim (his call, 30 Oct 2026).
- **Link live demos** when the JD mentions stakeholders, products or deployment.
- Applying to a competitor of a company a project is modelled on (P12 is Riverty-style)? Keep the project, drop the company name from the title.

### Starting picks

| Role family | Projects |
|---|---|
| Data Analyst / BI | P2 (data quality), P12 (Power BI 100K rows), P1 (pricing) |
| Data Scientist / ML | P3 (model comparison), P1 (elasticity + XGBoost), P5 or P7 (deep learning / tuning) |
| AI / GenAI / LLM | **P22 (token-reduction layer)**, P8 (agent + cost routing), P9 (RAG + CI/CD) — P6 if the JD is NLP-heavy |
| AI platform / LLMOps / infra cost | **P22**, P9 (Docker/K8s CI/CD), P8 (confidence routing) |
| Startup / early team / generalist | **P21 (odd-jobs aggregator)**, **P20 (job-search automation)**, P8 — products with users and judgement, not notebooks |
| Energy / CleanTech | P4 (thesis), P5 (solar LSTM), P7 (office energy) — swap P11 in for analyst-leaning roles |
| Business / Commercial | P1 (pricing + margin), P3 (demand), P15 or P12 (funnel / payments) |

---

## 6. Keyword mirroring

ATS filters on strings, humans read for meaning. Do both:

- Copy the JD's **exact spelling** of tools into the Skills rows.
- A skill may only be mirrored if it is already in `master.md` section 6. If the JD wants something Gaurav does not have, **leave it out** — do not approximate.
- Adjacent-but-not-equal is allowed only when it is honestly described: Snowflake SQL and DuckDB are both "cloud/columnar SQL", but do not write "Databricks" because of them.
- Put the single most-demanded tool in the **first Skills row** and in the **Profile**.

---

## 7. Honesty guardrails specific to this CV

- KnowGuard AI is an **internship** — the word stays on the CV.
- Azure is **FutureLearn coursework**, not production experience. The CV says so. Keep it that way.
- Most projects are **personal/academic**, not client work. Never imply otherwise. The "Projects" heading does that job.
- Croud Control is freelance. "Freelance Data Scientist" is the title; do not upgrade it.
- Thesis is **in progress** until the viva. Say "Thesis:" not "Published".

---

## 8. Role families worth exploring (Gaurav asked)

**Verdict on business roles: yes, and after the career walkthrough it is arguably his strongest
track, not a fallback.**
**Eight years** running Bhatia Traders end to end — purchasing, pricing, stock, supplier
terms, P&L — plus three side ventures and a rescued ₹2.75M export order at Troika, is operator
experience, not analyst experience. Paired with elasticity modelling on
15,000 SKUs, RFM segmentation and a demand-forecasting engine built on that same business, it
makes an unusual combination: someone who has carried the commercial consequence of a pricing or
stocking decision *and* can model it. Most analytics candidates have only the second half, and
most commercial candidates have only the first.

Where it does **not** reach: strategy consulting (needs a target-school brand or an MBB internship),
Product Manager (no shipped product owned with a roadmap and users), and anything titled Senior
or Lead (years). Treat "Business Analyst" postings with care — in Germany the title often means
requirements engineering for IT projects, which is a different job; read the responsibilities, not
the title.

Based on the full history, these fit beyond the four we agreed:

| Role | Why it fits | What it would need |
|---|---|---|
| **Commercial / Pricing Analyst** | Strongest unused angle. 8 years running a real P&L, plus elasticity modelling on 15,000 SKUs and an RFM segmentation. Very few analyst candidates have both. | Lead with Bhatia Traders + P1. Reframe Troika as commercial, not just ops. |
| **Supply Chain / Operations Analyst** | Troika (700+ vendors, 500+ SKUs) + demand forecasting + inventory savings is a clean, coherent story, and the export order proves he has carried a shipment deadline himself. German logistics hires heavily. | Lead with P3 + Troika. Mention the 10% inventory cost cut in the Profile. |
| **Import/Export, Trade or Logistics Analyst** | New since the walkthrough. India-to-EU export execution, freight-mode economics, customs-facing vendor and client management, and Tally ERP. Berlin and Hamburg both hire for this. | Lead with the Troika export bullet and the 8 years of purchasing. Title the headline "Supply Chain Analyst", not "Data Scientist". |
| **Energy Market / Power Trading Analyst** | Thesis is literally day-ahead price modelling on EPEX/SMARD. Berlin and Leipzig have a real market for this. | Needs the thesis finished and the long thesis variant. Likely the highest-ceiling path. |
| **Analytics Engineer** | SQL depth (CTEs, window functions, DuckDB, star schemas) + data quality + CI/CD + Docker. | Would benefit from one dbt project. Currently the gap. |
| **BI Developer** | Power BI/DAX across Troika, P12 and P11, plus the automated reporting suite. | Ready now. Lowest-friction path to a German role. |
| **AI Solutions / Forward Deployed Engineer** | P8 and P9 are both full product builds, not notebooks, with FastAPI + Docker + K8s. | Needs the KnowGuard metrics (G7). |

**Avoid for now:** ML Engineer at scale (no production MLOps), Senior Data Scientist (years), anything requiring C1 German.

### Reality check from the automation's own data (526 scored jobs, 30 Oct 2026)

The job-search automation had stored 526 jobs. Counts only, no postings, in this public file:

- **112 (21%) scored "strong" or "apply with tailoring"**; 255 were "stretch" and 154 "low".
- **German is the biggest blocker by far:** 340 of 526 (65%) flag it, though only 10% of ads are written in German. The single biggest lever on his options is his German level, ahead of any CV change.
- **Volume by role type** (title keywords, a job can count twice): AI/LLM engineer 172, data scientist/ML 126, data analyst/BI 111, working student/intern/trainee 101, analytics/data engineer 44, commercial analyst 19, product/project 12.
- **Highest hit rate: working student, intern and trainee roles (40% good).** Check each ad: many require current enrolment, and his enrolment ends in December 2026.
- **Coverage gap:** his most distinctive tracks barely appear. Supply chain 4 jobs, energy 4, commercial 19, because the automation's searches are aimed at data and AI titles. Searching those explicitly is the cheapest way to widen his options. **Done in `job-search-automation` v1.3.0 (30 Oct 2026): released, live once deployed.** It added a title filter and scoring for these families, 6 Arbeitsagentur terms, and XING, Indeed, StepStone and Arbeitnow searches. The new StepStone URLs and Arbeitsagentur terms were not tested against the live sites.
- Scores cap in the 60s and 70s because of the German deduction, so a "tailoring" verdict is a normal good match, not a weak one.

---

## 9. Build checklist

Before handing over a CV:

- [ ] Exactly two pages when printed to A4 (one page only if the ad or Gaurav asked for it)
- [ ] Photo shows top-right (`assets/photo.jpg`) on the CV and the cover letter
- [ ] Headline matches the JD's job title
- [ ] Profile names the top 3 JD requirements and ends with the availability line
- [ ] JD's top requirement appears in Skills row 1
- [ ] All 3 jobs still present (Croud Control is not one of them — hard rule 3)
- [ ] 3 projects, 2 bullets each, each with a working repo link — **except P20–P22**, whose repos are private and which show "Private repo" instead. At least one project on every CV must still have both a link and a metric.
- [ ] No claim outside `master.md` / `projects.md`
- [ ] **Zero em dashes.** Search for the character. `STYLE.md` has the full voice checklist
- [ ] No unresolved `G#` question affecting a line on this CV
- [ ] Filename `Gaurav_Bhatia_CV_<Company>.pdf`
- [ ] Saved to `out/`, JD notes saved to `jd/`
- [ ] If a cover letter goes with it: two stories, picked via §10, limits respected — see `COVER-LETTER-BUILDER.md`

---

## 10. Which experience answers which requirement

When a JD asks for something, this is what to reach for. **CV** = may go on the CV as a bullet;
**Letter** = cover letter and interview only, never a CV line. Stories marked Letter are in
`COVER-LETTER-BUILDER.md`; facts and numbers still come only from `master.md` and `projects.md`.

| JD asks for | Reach for | Where |
|---|---|---|
| Ownership, autonomy, "own it end to end" | The ₹2.75M export order — handed the whole project, sourced at the manufacturer, freight, client, delivery | **CV** (S1) |
| Negotiation, supplier or client management | Export-order renegotiation; 8 years of supplier terms across 20+ suppliers | **CV** (S1, S2) |
| Deadline pressure, "thrives under pressure" | The sea-to-air freight switch that saved the order | **CV** (S1) |
| Commercial acumen, P&L, pricing | 8 years running purchasing, pricing and stock; P1 elasticity on 15,000 SKUs | **CV** (S2) |
| Supply chain, inventory, demand planning | Troika: 700+ vendors, 500+ SKUs, 10% excess-inventory cut; P3 demand forecasting | **CV** (S7) |
| Import/export, international trade, customs | The Lithuania export order; freight-mode economics | **CV** (S1) |
| ERP systems | Tally (Troika) — the only ERP he has used. Do not stretch it to SAP | **CV** (S7) |
| Non-technical stakeholders, "translate data" | Troika Power BI across 3 divisions; logistics, vendor and client communication | **CV** (S7) |
| Experimentation, A/B testing, causal inference | The KnowGuard paired A/B test and the pre-set 0.05 threshold | **CV** (S4) |
| Statistical rigour, scientific method | Same — reporting a positive result as not worth shipping | **CV** (S4) |
| Energy, utilities, grid, CleanTech | Thesis + 6 energy repos (P4–P7, P11, P13, P14) | **CV** (S9) |
| E-commerce, online retail, marketplaces | Shopify stores and Guru Disha (venture); P1, P12, P15 (CV) | **CV** projects, **Letter** ventures (S3) |
| Startup, 0-to-1, "wear many hats", generalist | The three side ventures — marketplace, e-commerce, restaurant | **CV** BIZ only, **Letter** elsewhere (S3) |
| Entrepreneurial mindset | Same three ventures, plus 8 years of ownership | **CV** BIZ only (S2, S3) |
| Self-starter, curiosity, continuous learning | Self-taught SQL while running the business; 19 repos | **Letter** (S5) |
| "Career changer", non-traditional background | Self-taught SQL → own business's data → MSc | **Letter** (S5) |
| Customer-facing, service, hospitality | Restaurant management; tutoring; Troika clients | **Letter** (S3, S7) |
| Teaching, enablement, mentoring, documentation | Maths tutoring; Guru Disha tutor marketplace | **Letter** (S3) |
| Resilience, discipline, team culture | Third-tier football with Lonestar FC, 2019–2020 | **Letter, always**, one sentence linked to a story (S8). Never a CV line |
| Relocation, availability | Deliberate exit Jul 2025, available from Dec 2026. **No visa or permit wording, ever** | **CV** one line, **Letter** close (S6) |

Two rules for this table:

1. **A Letter row never becomes a CV bullet to fill space.** If the CV is short, add a project
   bullet, not a venture.
2. **Nothing here outranks §0.** Every number still has to be traceable, and the limits written
   into each story in `COVER-LETTER-BUILDER.md` apply identically on a CV — above all, the export
   order was *given* to him, never won by him.

---

---

## 11. Cold emails to startups: the CV always goes with it

Gaurav's rule, 30 Oct 2026: **every cold email to a startup goes out with his CV.** How it travels
depends on who sends it (his call, 31 Oct 2026):

- **The unattended routine** (the scheduled job-search tasks) does not build a CV and does not attach a
  file: Gmail takes attachments only as base64 typed out by the model, which costs tens of thousands
  of tokens per email and can corrupt the file. It **picks the closest of the eight role CVs** by the
  table in section 12 and puts **one link line** in the email: see section 13. The PDFs are published
  on his portfolio site.
- **A custom CV on call** (Gaurav asks in chat for one, for a named company or job) is built by the
  full procedure in `CLAUDE.md`, checked, rendered and **attached** as a PDF, as below.

For an attached custom CV:

1. **Build the CV first**, by the normal procedure (`CLAUDE.md`), tailored to the startup's field and the role he would fit. Two pages, with the photo. `scripts/check.py` must report 0 failures.
2. **Render it to PDF** and name it `Gaurav_Bhatia_CV_<Company>.pdf`. Count the pages: exactly two.
3. **Attach the PDF** to the email itself (Gmail `attachments`: base64 `content`, `filename`, `mimeType` `application/pdf`; the combined size must stay under 25 MB).
4. **In the body**, one plain sentence that the CV is attached, and his portfolio link: https://gauravbhatia-bit.github.io/
5. **No CV, no email.** If the CV cannot be built, fails the check or cannot be attached, do not send. Save the email as a draft and say why in the report. An email that goes out without the CV cannot be taken back.
6. The email follows `STYLE.md` like everything else: no em dashes, no banned phrases, and **never a word about visa, residence or work-permit status**.
7. Attach the CV only. Send a cover letter as well only if Gaurav asked for one.

---

## 12. Ready-made role CVs (the cheap path)

Building a CV from scratch means reading the data files and the rules, which costs thousands of
tokens per application. So eight finished, checked, two-page CVs live in `roles/`, one per job
family (Gaurav's call, 31 Oct 2026). **Start from one of them every time the job fits a family.**

| JD is about | File in `roles/` |
|---|---|
| Junior data scientist, data scientist, ML scientist, forecasting, statistics | `Gaurav_Bhatia_CV_Junior_Data_Scientist.html` |
| ML engineer, machine learning engineer, deploying models, MLOps (junior) | `Gaurav_Bhatia_CV_Junior_ML_Engineer.html` |
| Applied scientist, experimentation, A/B testing, causal inference, quantitative research | `Gaurav_Bhatia_CV_Applied_Scientist.html` |
| AI engineer, LLM engineer, GenAI, agents, RAG, prompt or AI solutions engineer | `Gaurav_Bhatia_CV_AI_LLM_GenAI_Engineer.html` |
| Data analyst, BI analyst, BI developer, reporting, Power BI | `Gaurav_Bhatia_CV_Data_Analyst_BI_Analyst.html` |
| Analytics engineer, junior data engineer, ETL, pipelines, data warehouse | `Gaurav_Bhatia_CV_Analytics_Engineer_Data_Engineer.html` |
| Supply chain, operations, demand planning, logistics, procurement, inventory, import/export | `Gaurav_Bhatia_CV_Supply_Chain_Operations_Analyst.html` |
| Business analyst, commercial or pricing analyst, business intelligence | `Gaurav_Bhatia_CV_Business_Analyst.html` |

Choose by the **job title first**, then by what the ad actually asks for. If two fit, take the one
whose first skills row matches the ad's first requirement.

**The quick build** (what to do for most applications, and all that is needed):

1. `cp roles/<file>.html out/Gaurav_Bhatia_CV_<Company>.html`
2. Change the headline `<h2>` to the ad's own job title, where that is honest. Change `<title>` to match.
3. Optional and small: if the ad spells a skill differently ("PowerBI", "experimentation"), mirror its spelling in the Skills row, only for a skill already in `master.md` section 6.
4. `python scripts/check.py`, render, count two pages.

Do not re-pick projects, rewrite the Profile or read `master.md` / `projects.md` for this. The role
CV already holds the right projects in the right order, and that is what the eight files are for.
Escalate to a **full custom build** (`CLAUDE.md` procedure, from `templates/base-2page.html`) only when:

- the ad is in a family with no role CV (for example an **energy or power-market analyst**: start from the Junior Data Scientist file and move the thesis and energy projects first);
- the ad asks for a tool the role CV does not show and he has it (check `master.md` section 6);
- Gaurav asks for a deeper tailoring.

**Gaps to name to Gaurav, never to write on the CV:** dbt (no project yet; matters for analytics-engineer ads), production MLOps, SAP, Databricks.

**Keeping them current.** The role CVs are generated: their content lives in `scripts/build_roles.py`
(`ROLES`), which reads the look and the shared project text from `templates/base-2page.html`. After a
change to `data/` or to that template, run `python scripts/build_roles.py`, then `python scripts/check.py --render`.
Never hand-edit a file in `roles/`: the next build overwrites it. `check.py` fails if there are not
eight, if any carries an untraceable number, an em dash or a wrong date, or if one is not two pages.

---

## 13. Sending a role CV by link (the routine's way)

The eight role CVs are rendered with his contact details and published as PDFs in the `cv/` folder
of his portfolio repo (`gauravbhatia-bit/gauravbhatia-bit.github.io`, served at
https://gauravbhatia-bit.github.io/cv/). His phone and email are on those PDFs on purpose (Gaurav, 31 Oct
2026: fine on a public page). The repo `cv-builder` still never holds them.

| Role CV | Link |
|---|---|
| Junior Data Scientist | https://gauravbhatia-bit.github.io/cv/Gaurav_Bhatia_CV_Junior_Data_Scientist.pdf |
| Junior ML Engineer | https://gauravbhatia-bit.github.io/cv/Gaurav_Bhatia_CV_Junior_ML_Engineer.pdf |
| Applied Scientist | https://gauravbhatia-bit.github.io/cv/Gaurav_Bhatia_CV_Applied_Scientist.pdf |
| AI / LLM / GenAI Engineer | https://gauravbhatia-bit.github.io/cv/Gaurav_Bhatia_CV_AI_LLM_GenAI_Engineer.pdf |
| Data Analyst / BI Analyst | https://gauravbhatia-bit.github.io/cv/Gaurav_Bhatia_CV_Data_Analyst_BI_Analyst.pdf |
| Analytics Engineer / Junior Data Engineer | https://gauravbhatia-bit.github.io/cv/Gaurav_Bhatia_CV_Analytics_Engineer_Data_Engineer.pdf |
| Supply Chain & Demand Planning Analyst | https://gauravbhatia-bit.github.io/cv/Gaurav_Bhatia_CV_Supply_Chain_Operations_Analyst.pdf |
| Business Analyst | https://gauravbhatia-bit.github.io/cv/Gaurav_Bhatia_CV_Business_Analyst.pdf |

**Picking one.** Use the table in section 12 on the startup's open role if it has one, otherwise on
the field and the problem the email names (a data platform startup: Analytics Engineer; an LLM
product: AI / LLM / GenAI; a logistics or procurement startup: Supply Chain). If nothing fits, take
Junior Data Scientist. Never ask, never build a CV for this.

**In the email**, one plain line before the signature: `My CV: <link>`. The email still carries the
portfolio link. Record which role was picked next to the company in the run log.

**Keeping the PDFs current.** After any change to the role CVs (`python scripts/build_roles.py`), run
`render.cmd roles` (full path), copy the eight `out\Gaurav_Bhatia_CV_<Role>.pdf` files into `cv/` of a clone
of the portfolio repo, and commit and push there. The links do not change.
