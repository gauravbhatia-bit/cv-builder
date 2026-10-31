# Project Library — Gaurav Bhatia

Every project, with tags, stack, metric and repo. Companion to `master.md`, which holds everything
else (identity, experience, education, skills). **This file is the only source of project content.**
Nothing about a project lives in `master.md` any more.

Tags: `[DA]` Data Analyst / BI · `[DS]` Data Scientist / ML · `[AI]` AI / GenAI / LLM · `[EN]` Energy / CleanTech · `[BIZ]` Business / Commercial

Pick 3 per CV using `RULES.md` §5.

**Changing this file is safe.** IDs (`P1`, `P2` ...) are permanent: add a project as the next number,
edit one in place, mark one retired, but **never renumber**, because `RULES.md` §5 and the cover
letter notes point at them. The two CV templates carry a *copy* of the projects they show, so when
you edit one of those, ask for the template to be refreshed too. Everything else reads from here.
`python scripts/sync_repos.py` tells you when GitHub has moved on from this file.

---

## The library

19 usable repos, plus 3 in flight (P20–P22, see §5a — **not CV-ready until each has a number**).
A CV shows **3, at most 4**. Pick by tag match to the JD.

| # | Project | Tags | Stack | Headline metric | Repo |
|---|---|---|---|---|---|
| P1 | Dynamic Pricing & Segmentation | DA DS BIZ | Python, statsmodels, XGBoost, Plotly, Streamlit | Elasticity on 15,000 SKUs; repriced 55.7% of catalogue; XGBoost MAPE 2.14% | `ecommerce-dynamic-pricing-engine` |
| P2 | BI Data-Quality Pipeline | DA | Python, pandas, NumPy | 45 checks / 7-table star schema, 41 passed (91.1%); traced 2 silent data losses | `bi-data-quality-pipeline` |
| P3 | Demand Forecasting Engine | DS BIZ | Python, ARIMA, Prophet, XGBoost, Streamlit | Prophet 6.07% MAPE vs 15.49% ARIMA, 12 SKUs, 12-week hold-out | `demand-forecasting-engine` |
| P4 | MSc Thesis — Hormuz to German power prices | EN DS | Python, Chronos, XGBoost, Granger, event study | 5 research questions, reproducible pipeline, scenario modelling | `US-Iran-impact_on_German_Electricity_thesis` |
| P5 | Solar Power Forecasting (LSTM) | EN DS | TensorFlow/Keras LSTM, OPSD, Open-Meteo | 26,280 hourly rows, chronological 70/15/15 split, RMSE/MAE/MAPE | `solar-power-forecasting` |
| P6 | Energy News to Price Volatility (NLP) | EN AI DS | FinBERT, VADER, TF-IDF, Google Trends, XGBoost, SHAP | 4,444 headlines; 4-model comparison; Granger-informed lags | `energy-news-volatility-nlp` |
| P7 | Office Energy Forecasting Dashboard | EN DS | XGBoost, Optuna (50 trials), SHAP, Streamlit | MAE 22.98 Wh, RMSE 50.96, MAPE 22.28%; live app | `office-energy-forecasting-dashboard` |
| P8 | Sales Intelligence Agent | AI DS | TF-IDF + logistic regression, Gemini fallback, FastAPI, Streamlit | 5-intent classifier with confidence routing; versioned hold-out; live API + UI | `sales-intelligence-agent` |
| P9 | RAG Retail Agent | AI | LangChain, FAISS, flan-t5, FastAPI, Docker, K8s, GitHub Actions | End-to-end RAG microservice with CI/CD | `rag-retail-agent` |
| P10 | Dutch Business Risk Radar | EN AI BIZ | Streamlit, NLP, event study | News-intensity risk scoring + scenario analysis; live app | `dutch-risk-radar` |
| P11 | Solar Demand Analytics | EN DA | DuckDB SQL (window functions), Open-Meteo, SMARD, Power BI | Summer output 4x winter; >75% cloud cover cuts generation ~40% | `solar-demand-analytics` |
| P12 | Payments BI Dashboard (Riverty-style) | DA BIZ | Power BI, DAX, Python, star schema | 100K transactions, $15.99M revenue, 3-page dashboard, 51% BNPL share | `riverty-style-payments-bi-dashboard` |
| P13 | Building Energy Efficiency Predictor | EN DS | XGBoost, Optuna, Streamlit | Predicts heating load + EU energy class A-E for retrofit triage | `building-energy-efficiency-predictor` |
| P14 | Germany Energy Load Forecasting | EN DS | Prophet, LSTM, OPSD | Daily German load + solar generation forecast | `Germany-Energy-Load-Forecasting` |
| P15 | Marketing Funnel Dashboard | BIZ DA | Python, SQLite, Matplotlib | Funnel, CAC and CVR across 5 channels, 52 weeks | `marketing-funnel-dashboard` |
| P16 | Toll SQL Reporting Pipeline | DA | DuckDB, SQL (CTEs, window functions, RANK) | 4 standing reports; Z-score anomaly flagging | `toll-sql-reporting-pipeline` |
| P17 | Toll Traffic Anomaly Detector | DA DS | Z-score + Isolation Forest, Plotly | 6 months hourly data, 5 autobahn segments | `toll-traffic-anomaly-detector` |
| P18 | Maut Weekly Report Automation | DA | APScheduler, Jinja2, Plotly, DuckDB | Fully automated Monday 08:00 HTML KPI report | `maut-report-automation` |
| P19 | Bhatia Traders Sales Analysis | BIZ | pandas, Matplotlib, moving averages | 15% stockout-reduction potential; margin ranking by product | `bhatia-traders-sales-analysis` |
| P20 | Job-Search Automation (4 chained scheduled agent tasks) | AI DS BIZ | Scheduled agents, shared database, ATS and Arbeitsagentur feeds, validator, versioned releases | 4 tasks, 37 standing rules, job boards across 12 countries, 25 stored job batches | `job-search-automation` (**private**) |
| P21 | Odd-Jobs Aggregator for Students in Germany | AI DA BIZ | Multi-source listing ingestion (Kleinanzeigen, Craigslist, extensible), dedup, draft generation, human-in-the-loop approval, auto-apply | 2 sources live, pluggable; 24h window; built | **private** |
| P22 | **ParetoGate** — cost-aware LLM gateway | AI DS | FastAPI, MiniLM, scikit-learn, SQLite semantic cache, Ollama/LM Studio, code graph | 86,416 → 11,351 input tokens on a frozen 25-task suite, all reviewed changes passing (80.8% modelled cost cut) | **private** |
| P23 | Bhatia Traders SQL Inventory Alerts | DA BIZ | MySQL (CASE, JOINs, UPDATE) | Automated 20% low-stock alerts with reorder recommendations | `bhatia_traders_inventory_alert_system` |
| P24 | Agent Evaluation Harness — fin-agent-eval | AI | LangGraph, Gemini, FastAPI, Streamlit, Docker, Terraform, GitHub Actions | 50 golden test cases, LLM-as-judge audit (Cohen's κ), decision/tool/consistency metrics, quality gate CI, deployed on Render | `fin-agent-eval` |

Repo URL = `https://github.com/gauravbhatia-bit/<repo>`

Live demos (link these when the JD mentions deployment, product sense or stakeholders):
- Sales Intelligence Agent — https://sales-intelligence-agent-5brv6ii7xelgzq7omewadn.streamlit.app/
- Office Energy Dashboard — https://office-energy-forecasting-dashboard-byb9cixihrwm3c779d3hpv.streamlit.app/
- Dutch Risk Radar — https://dutch-risk-radar-lu7gdrmdsmobmccabmbypw.streamlit.app/

**Do not list:** `testing1`, `testing.`, `pappu`, `machine-learning-practice`, `Machine-learning-intro`, `Churn-Analysis` (empty README), `berlin-football-analystics` (fun, not professional), `iran-energy-impact-analyzer` (superseded by P4), `ds-intern-challenge-submission` (someone else's brief), `gauravbhatia-bit.github.io` and `gauravbhatia-bit.bio` (the portfolio site and profile, not projects).

## In-flight projects — P20, P21, P22

Added 30 Oct 2026. The three Gaurav is building now, and **the strongest product work in the
portfolio** — full systems with schedulers, persisted state, generated documents and human-in-the-
loop approval, not notebooks.

**These go on CVs.** They are current work, written in the present tense. Hard rule 4 forbids
claiming a number he cannot show; it does not forbid a project that has no number yet. Describe
**scope** — sources covered, geography, time window, techniques — which is factual, and leave
**results** out until they exist. For a role that cares about AI engineering these beat most of
P1–P19, because they are products rather than analyses.

### Repo status

Checked against his GitHub account on 30 Oct 2026 (`gh repo list`, 33 repos):

| Project | On GitHub? |
|---|---|
| P20 Job-Search Automation | **Yes, private** as `job-search-automation` |
| P21 Odd-Jobs Aggregator | **Not found** under `gauravbhatia-bit`, public or private |
| P22 ParetoGate | **Not found** under `gauravbhatia-bit`, public or private |

**Update, 30 Oct 2026:** Gaurav confirms P21 and P22 are on his machine and he will push them to
GitHub soon ("no worries"). Until then the **"Private repo" label on the CV is a forward-looking
claim**; it becomes accurate the day they are pushed. After he pushes, run
`python scripts/sync_repos.py`: they will appear as NEW, and their real slugs and READMEs go in here
(the P21 and P22 rows still say "private" with no slug). Never link a repo that 404s, and never guess
a slug.

> **Worth doing, and it is the cheapest win available.** Every other project here is verifiable in
> one click, and these three, the most impressive work in the library, are the only ones a reader
> has to take on trust. Making even one public changes that. P21 is the best candidate: it is
> built rather than in progress, and a sanitised version without credentials or scraping keys
> would be enough. Failing that, a README with screenshots in a public repo carries most of the
> benefit for an hour of effort. It is Gaurav's call, not a blocker.

### Numbers to add the moment they land

Not gates. These just turn a good line into a strong one, and P22's are days away.

| # | Add when available | Why that one |
|---|---|---|
| P20 | Reply or interview rate vs. his manual baseline | Volume proves a cron job runs. A reply rate proves the targeting and the generated documents work, which is the actual engineering. |
| P21 | Users, and listings ingested per day | Users is the one metric nothing else in this library has. One user outside himself changes what the project means. |
| P22 | **% token reduction at equal task quality**, with the quality guard named | A router can always cut tokens by downgrading the model. The pairing is the whole claim. |

### P20 — Job-Search Automation

**Repo `job-search-automation`, private** (it holds his personal details). Facts below are from its
README, read on 30 Oct 2026; re-read it when it changes (`scripts/sync_repos.py` will flag that).

His daily Berlin job search as versioned code. **Four scheduled agent tasks hand work to each other
through a shared database:**

| Task | Does |
|---|---|
| Find jobs (weekdays, morning) | ATS and Arbeitsagentur feeds, government portals, job boards in Germany, the Netherlands and ten further countries, plus funding news |
| Outreach (weekdays) | Inbox, LinkedIn accepts, funded-startup and agency emails, tracker, calendar, a daily digest |
| Report (weekdays) | One daily report, a checker receipt, a run log, a push notification, a GitHub archive step |
| LinkedIn (on demand) | 14 searches, **drafts only** |

**Quotable, all from the README:** 4 tasks · **37 standing rules** with an ownership map · a
**validator that gates each run and issues receipts** · a regression test built on a real report ·
**versioned releases with rollback and snapshots** · 25 stored job batches · LaTeX CV and
cover-letter templates · install config kept separate from the code.

> **This is a real engineering project, and the README proves it.** Gates, receipts, ownership of
> rules, rollback: that is how production systems are run, and almost no portfolio project has it.
> It was undersold in the first description ("a scheduled pipeline"). For AI-engineering, platform
> or automation roles, lead with the governance (rules, validator, rollback), not the job search.
>
> **Compliance: mostly settled by the README.** The LinkedIn task produces **drafts only**, so
> nothing is sent or connected automatically, and sourcing is from ATS, Arbeitsagentur and
> government feeds, which is the safe pattern. That removes the scraping and platform-terms worry
> raised earlier. What remains is the outreach task emailing agencies and funded startups: keep to
> role-based addresses, human-scale volume, say plainly it is a job application, and cap
> follow-ups (UWG §7 and GDPR). A flag, not legal advice.
>
> **How to describe it.** Lead with the system (scheduled agents, shared state, validation, rollback),
> not "sends automated cold emails". A reader who hears the first sees an engineer; one who hears
> the second sees a compliance risk.

### P21 — Odd-Jobs Aggregator for Students in Germany

Aggregates odd-job listings posted in the last 24h across Kleinanzeigen, Craigslist and further
sources he can add, for Indian students arriving in Germany who cannot realistically search them by
hand. Drafts the outreach message and tailors a CV per listing. He ticks the ones he wants; the
system applies on his behalf.

> **This is the best project in the library and it is not close.** Everything else — including the
> energy work — is Gaurav solving a problem for Gaurav. This one identifies a group of people with
> a painful problem and builds for them, and it contains a product decision (human-in-the-loop
> approval rather than full automation) that shows judgement, not just capability.
>
> **It belongs on a CV now, with or without users.** Gaurav's call, 30 Oct 2026, and he is right:
> the insight is what is being assessed. Describe it as built — sources, window, the approval step.
> Say nothing about adoption either way; an unasked "no users yet" is a disclaimer nobody requested.
> If users do arrive, add the count, because it is the one proof point nothing else here has.
>
> Same platform-terms caution as P20, lower stakes: respect robots.txt, rate-limit, store no
> personal data about the people posting listings, and prefer official feeds where they exist.
> Framing it as an aggregator with human approval is both accurate and defensible.

### P22 — ParetoGate

**The real name is ParetoGate.** Use it. "Self-learning token-reduction layer" is a description;
ParetoGate is a product, and a named product reads as something that exists.

A local-first, cost-aware LLM gateway. It embeds an incoming request with MiniLM (384-dim),
predicts which optimisations apply via ten one-vs-rest logistic classifiers, applies deterministic
safeguards that can veto a risky choice, then selects a `local` / `standard` / `premium` route and
measures candidate plans against explicit quality **and** cost constraints. Ships as a FastAPI
service with a SQLite + MiniLM semantic cache, versioned conversation memory, and an incremental
Python code graph.

**Measured, from the README (30 Oct 2026).** All of these are quotable; the labels matter.

| Figure | What it actually measures | How to quote it |
|---|---|---|
| **86,416 → 11,351 input tokens** (86.9% fewer) on a frozen **25-task** code-change suite, all reviewed changes passing | Real token counts from the native retriever, replay harness | Safest and strongest. A measured token count, not a model. |
| **80.8% modelled cost reduction** (native), **84.1%** (Graphify) | Cost *model* applied to those tokens | Always say "modelled". Never "saved 80% of our bill". |
| **13.75% aggregate modelled savings**, 4-case live Ollama run, 3 plans accepted + 1 fallback, 16 tests passing | End-to-end execution with a real local model | Small n. Quote with the n. |
| **Realised cost 25.7% worse** on a 5-task live run, despite 81.3% fewer input tokens | Candidates were cheaper but none matched the reviewed solution; conservative accounting charged the retry | **The most valuable line in the whole file.** See below. |

> **The negative result is the story, and it is the second time he has done this.** The README
> reports a run where the headline component number was excellent — 81.3% fewer input tokens — and
> the end-to-end outcome was *worse*, because failed candidates were charged the baseline retry. He
> wrote "This is a negative end-to-end result, not a savings claim" into his own documentation
> rather than quoting the 81.3% and moving on.
>
> That is exactly what he did at KnowGuard with the pre-set 0.05 threshold. Twice is not luck; it
> is how he works, and it is rare enough to be a differentiator in its own right. **Put it on the
> CV.** Most candidates cannot name a result they chose not to claim.

> **The honesty is structural, not cosmetic.** Rejected candidates are charged as zero savings;
> rollback cost is included in realised figures; the measurement endpoint labels itself `estimate`
> and names its tokenizer; pricing is supplied by the caller so no stale vendor rate is baked in;
> the trainer **refuses to train on undersized evidence** rather than publishing a misleading
> metric. An engineer reading that README will trust the numbers precisely because of how heavily
> they are qualified. Do not strip the qualifiers to make a punchier bullet — the qualifiers are
> the achievement.

**Safety design worth a bullet on its own:** semantic reuse is denied for fresh, sensitive,
high-stakes and exact-wording requests; cache is tenant-isolated, data-versioned, TTL-bounded and
similarity-gated, and serves only quality-verified answers. Lossy compression is vetoed for
high-stakes work. This is the answer to "how do you stop a cost optimiser from quietly degrading
output".

**Known limits — do not overstate.** It is a localhost prototype, not an authenticated multi-user
service; tenant IDs are isolation keys, not authorisation. Production and shadow request modes are
not complete. General document RAG is future work. The 72-row sample dataset is explicitly
illustrative. The replay suite validates the harness, not model intelligence. If asked "is it in
production?", the answer is no, and the README says so first.

> **The architecture is well-trodden; the learning and the gate are the differentiators.** Semantic
> caching and routing exist in GPTCache, semantic-router, LiteLLM and Portkey, and an interviewer in
> this area will know that immediately. What those do not generally have is a *quality-constrained*
> selector with a bounded repair path (a candidate may cost up to 25% more if the baseline itself
> fails the quality floor), calibrated per-plan outcome prediction, and realised-cost accounting
> that includes rollback. Lead with the gate, not the caching.

### Overlap with this repo

P20 generates tailored CVs and cover letters, which is what `cv-builder` does. Decide which is the
engine: either P20 calls this repo's `master.md`, `RULES.md` and `COVER-LETTER-BUILDER.md` as its
content layer, or the two drift into different claims about the same career. **The first is better**
— it keeps one source of truth, and "my automation generates applications from a versioned,
rule-governed content library" is a considerably more impressive sentence than "my automation writes
cover letters".

---

### Project bullet bank

Two bullets max per project. Lead with the number.

**P1 Dynamic Pricing & Segmentation**
- Estimated price elasticity per category with log-log OLS on 15,000 SKUs in 8 categories (e.g. Fashion -2.1, Food & Beverages -0.5)
- Segmented customers with RFM scoring (Champions, Loyal, Price-Sensitive); 6 business rules + XGBoost repriced 55.7% of the catalogue (8,352 SKUs)
- XGBoost price recommender reached 2.14% MAPE, served in a Streamlit KPI dashboard

**P2 BI Data-Quality Pipeline**
- Automated 45 validation checks (missing values, duplicates, referential integrity, outliers, row counts) across a 7-table star schema; 41/45 passed (91.1%)
- Traced two silent data losses (614 payment rows, 551 review rows) to their root cause and documented fixes in an auto-generated report

**P3 Demand Forecasting Engine**
- Compared ARIMA, Prophet and XGBoost on 5 years of weekly sales for 12 SKUs on a 12-week hold-out; Prophet best at 6.07% MAPE vs. 15.49% for ARIMA
- Shipped as a Streamlit app where a planner picks SKU, model and horizon and sees MAE/RMSE/MAPE live

**P4 Thesis — Hormuz to German electricity**
- Built a reproducible pipeline answering 5 research questions on how the 2026 US-Iran conflict moved German day-ahead prices, benchmarked against the 2022 energy shock
- Combined event study, Granger causality and ablation tests with Chronos and XGBoost forecast arms to identify the transmission channel

**P5 Solar Power Forecasting**
- Forecast hourly German solar generation with an LSTM on 26,280 hourly rows (OPSD + Open-Meteo), chronological 70/15/15 split to prevent leakage
- Framed against market value: a 1% national forecast gain is ~600 MW/hour, worth roughly EUR 48-90k per hour

**P6 Energy News Volatility NLP**
- Predicted high-volatility days on EPEX Spot from 4,444 energy headlines using FinBERT and VADER sentiment, TF-IDF trend signals and Google Trends attention
- Compared four models (dummy, FinBERT-only, default and tuned XGBoost) with SHAP attributions and Granger-causality-informed lags

**P7 Office Energy Forecasting**
- Tuned XGBoost with 50 Optuna trials to predict office energy use — MAE 22.98 Wh, RMSE 50.96 Wh — and surfaced CO2 savings in a live Streamlit app
- SHAP showed short-term momentum (lag_1, rolling_mean_6) dominates consumption, with out-of-hours waste alerts

**P8 Sales Intelligence Agent**
- Routed plain-English business questions through a local TF-IDF + logistic-regression intent classifier, calling Gemini only below a confidence threshold to control cost
- Served it as a FastAPI microservice with a Streamlit front end, with versioned training and hold-out sets so accuracy is measurable

**P9 RAG Retail Agent**
- Built a LangChain + FAISS retrieval pipeline over product data behind a FastAPI service, with GitHub Actions to Docker Hub to Kubernetes CI/CD

**P10 Dutch Risk Radar**
- Scored conflict-related news intensity and ran event-study analytics to turn geopolitical news into measurable business-risk signals, deployed as a live Streamlit dashboard

**P11 Solar Demand Analytics**
- Modelled German solar generation and weather in DuckDB SQL (window functions, views) and exported to Power BI: summer output 4x winter, cloud cover above 75% cuts generation ~40%

**P12 Payments BI Dashboard**
- Built a 3-page Power BI dashboard over 100K e-commerce payment transactions ($15.99M revenue) covering BNPL share, delivery performance and revenue mix with DAX measures

**P13 Building Energy Efficiency Predictor**
- Predicted building heating load and EU energy class (A-E) from geometry with a tuned XGBoost model, to prioritise retrofit candidates at scale

**P15 Marketing Funnel Dashboard**
- Tracked impressions to clicks to leads to customers with CAC and CVR per channel across 5 channels and 52 weeks, in SQL plus a Python dashboard

**P16-P18 Toll / Maut suite**
- Built SQL reporting (CTEs, window functions, RANK), Z-score and Isolation Forest anomaly detection, and a scheduled weekly HTML KPI report over German highway toll data

**P20 Job-Search Automation** *(built, run daily)* — up to four bullets on a 2-page CV, two on a 1-page
- Built a versioned job-search system of four scheduled agent tasks (sourcing, outreach, daily report, LinkedIn drafts) that hand work to each other through a shared database
- Sourced roles from ATS and Arbeitsagentur feeds, government portals and job boards across 12 countries, plus funding news for startups
- Governed it as an agent harness: 37 standing rules with an ownership map, a validator that gates every run and issues receipts, and a regression test built on a real report
- Shipped it with versioned prompts and releases, snapshots and one-command rollback, and kept the LinkedIn task to drafts only

**P21 Odd-Jobs Aggregator for Students in Germany** *(current)*
- Built a multi-source aggregator that collects odd-job listings posted in the last 24 hours across Kleinanzeigen, Craigslist and further pluggable sources, for international students who cannot search them by hand
- Generates the application message and a tailored CV per listing, and applies automatically once the user approves a shortlist — a deliberate human-in-the-loop step rather than full automation

**P22 ParetoGate — cost-aware LLM gateway** *(current)*
- Built a local-first LLM gateway that classifies each request with MiniLM embeddings, predicts applicable optimisations with ten one-vs-rest logistic models, and applies deterministic safeguards before any lossy transform
- Cut retrieved context from **86,416 to 11,351 input tokens** on a frozen 25-task code-change suite while passing every reviewed change — an 80.8% modelled cost reduction
- Gated every saving behind a **task-quality floor** with automatic baseline fallback, charging rejected candidates as zero savings so reported figures include rollback cost
- Reported a **negative end-to-end result** — realised cost 25.7% worse on a live 5-task run — rather than publishing the favourable 81% input-token figure alone
- Denied semantic cache reuse for fresh, sensitive, high-stakes and exact-wording requests, with a tenant-isolated, TTL-bounded, similarity-gated SQLite + MiniLM store serving only quality-verified answers
- Served it as a **FastAPI** service with versioned conversation memory and an incremental Python code graph, benchmarked against local models via Ollama and LM Studio

**P23 Bhatia Traders SQL Inventory Alerts**
- Built MySQL queries (CASE, JOINs, UPDATE) that raise automated low-stock alerts at a 20% threshold with reorder recommendations for a sauces and condiments business

> **Tense matters on these three.** P20 and P22 are in progress — "Building", "Designing".
> P21 is built — "Built". Do not write a past-tense completion claim for work still running, and
> do not hedge finished work into the present. A reader notices the mismatch before they notice
> anything else.

---
