# CV Tailoring Rules

How a job description turns into a CV. Read with `data/master.md`.

---

## 0. Hard rules — never break these

1. **Nothing goes on a CV that is not in `data/master.md`.** No invented metrics, tools, dates or titles.
2. **One page.** Gaurav has ~4.5 years of experience. Two pages is a mistake at this stage.
3. **Never remove a job.** Gaps look worse than a less relevant role. Shrink it to one bullet instead.
4. **Every number on the CV must be traceable** to a README, a dashboard or a report. If a number cannot be shown in an interview, it does not go on.
5. **Do not claim German above A2** and do not hide it either. It is on the CV as A2, improving.
6. If an open question in `master.md` section 2 blocks a line, **ask — do not guess**.

---

## 1. Read the JD in this order

Write the answers into `jd/<company>-<role>.md` before building anything.

| Step | What to extract |
|---|---|
| 1 | **Role family** — DA / DS / AI / EN / BIZ (see tags in master.md). Often two. |
| 2 | **Top 5 hard requirements** — the tools and methods named in "Your profile" / "Requirements". |
| 3 | **Exact keyword spellings** — "Power BI" vs "PowerBI", "A/B testing" vs "experimentation". Copy their spelling into the CV. ATS matches strings. |
| 4 | **Domain** — energy, fintech, e-commerce, logistics, SaaS, consulting. This decides which projects get picked. |
| 5 | **Seniority** — junior / working student / mid. If mid+ and asking for 3-5 years, lead with Troika and Bhatia Traders, not the internship. |
| 6 | **Language** — if the JD is in German, the CV stays in English but mirror German technical terms where natural, and address the German level in the cover letter. |
| 7 | **Blockers** — needs C1 German? needs an existing permit? 5 years required? Note it. A blocker may mean "do not apply". |

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
- Always end with: `Available full-time in Berlin from January 2027.`
- Never write "passionate", "motivated", "team player", "results-driven".

---

## 4. Bullet budget (one page, fits reliably)

| Role | DA / BI | DS / ML | AI / GenAI | Energy | BIZ |
|---|---|---|---|---|---|
| KnowGuard AI (intern) | 1 | 2 | 3 | 1 | 1 |
| Croud Control (freelance) | 1 | 2 | 1 | 2 | 1 |
| Troika International | 3 | 2 | 1 | 2 | 2 |
| Bhatia Traders | 2 | 1 | 1 | 1 | 3 |
| **Projects shown** | 3 | 3 | 3 | 3 | 3 |
| Bullets per project | 2 | 2 | 2 | 2 | 2 |

If it spills past one page, cut in this order: **any bullet without a number** → the 2nd bullet of project 3 → the weakest Bhatia Traders bullet → a skills row → Certifications. Keep Certifications if the JD mentions cloud or data engineering. Never shrink the Profile below 3 lines; never drop a project to 1 bullet.

Before cutting content, try `--fs: 9.5pt` / `--gap: 2px` (the template defaults — these already fit the base CV on one A4 page). Below 9pt, cut content instead.

---

## 5. Project picking

Rank every project by `tag match + domain match + has a number`. Take the top 3, then apply:

- **Never show 3 projects of the same type.** Two in the JD's area, one that shows range.
- **Domain beats tag.** Applying to an energy company? P4/P5/P6/P7 go first even for a DA role — use P11 (DuckDB SQL + Power BI) as the analyst proof.
- **The thesis counts as a project** for energy and research roles, and also stays in Education.
- **Link live demos** when the JD mentions stakeholders, products or deployment.
- Applying to a competitor of a company a project is modelled on (P12 is Riverty-style)? Keep the project, drop the company name from the title.

### Starting picks

| Role family | Projects |
|---|---|
| Data Analyst / BI | P2 (data quality), P12 (Power BI 100K rows), P1 (pricing) |
| Data Scientist / ML | P3 (model comparison), P1 (elasticity + XGBoost), P5 or P7 (deep learning / tuning) |
| AI / GenAI / LLM | P8 (agent + cost routing), P9 (RAG + CI/CD), P6 (FinBERT NLP) |
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

Based on the full history, these fit beyond the four we agreed:

| Role | Why it fits | What it would need |
|---|---|---|
| **Commercial / Pricing Analyst** | Strongest unused angle. 3.5 years running a real P&L, plus elasticity modelling on 15,000 SKUs and an RFM segmentation. Very few analyst candidates have both. | Lead with Bhatia Traders + P1. Reframe Troika as commercial, not just ops. |
| **Supply Chain / Operations Analyst** | Troika (700+ vendors, 500+ SKUs) + demand forecasting + inventory savings is a clean, coherent story. German logistics hires heavily. | Lead with P3 + Troika. Mention the 10% inventory cost cut in the Profile. |
| **Energy Market / Power Trading Analyst** | Thesis is literally day-ahead price modelling on EPEX/SMARD. Berlin and Leipzig have a real market for this. | Needs the thesis finished and the long thesis variant. Likely the highest-ceiling path. |
| **Analytics Engineer** | SQL depth (CTEs, window functions, DuckDB, star schemas) + data quality + CI/CD + Docker. | Would benefit from one dbt project. Currently the gap. |
| **BI Developer** | Power BI/DAX across Troika, P12 and P11, plus the automated reporting suite. | Ready now. Lowest-friction path to a German role. |
| **AI Solutions / Forward Deployed Engineer** | P8 and P9 are both full product builds, not notebooks, with FastAPI + Docker + K8s. | Needs the KnowGuard metrics (G7). |

**Avoid for now:** ML Engineer at scale (no production MLOps), Senior Data Scientist (years), anything requiring C1 German.

---

## 9. Build checklist

Before handing over a CV:

- [ ] One page when printed to A4
- [ ] Headline matches the JD's job title
- [ ] Profile names the top 3 JD requirements and ends with the availability line
- [ ] JD's top requirement appears in Skills row 1
- [ ] Every one of the 4 jobs still present
- [ ] 3 projects, 2 bullets each, each with a number and a working repo link
- [ ] No claim outside `master.md`
- [ ] No unresolved `G#` question affecting a line on this CV
- [ ] Filename `Gaurav_Bhatia_CV_<Company>.pdf`
- [ ] Saved to `out/`, JD notes saved to `jd/`
