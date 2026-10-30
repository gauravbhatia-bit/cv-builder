# Project Library — Gaurav Bhatia

Every project, with tags, stack, metric and repo. Companion to `master.md`, which holds everything
else (identity, experience, education, skills). **This file is the only source of project content.**
Nothing about a project lives in `master.md` any more.

Tags: `[DA]` Data Analyst / BI · `[DS]` Data Scientist / ML · `[AI]` AI / GenAI / LLM · `[EN]` Energy / CleanTech · `[BIZ]` Business / Commercial

Pick 3 per CV using `RULES.md` §5.

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
| P20 | Job Search & Outreach Automation | AI DS BIZ | Scheduled pipeline, job ingestion, CV/letter generation, email sequencing, CRM-style tracking | 24h ingestion window across 3 geographies; in progress | **private** |
| P21 | Odd-Jobs Aggregator for Students in Germany | AI DA BIZ | Multi-source listing ingestion (Kleinanzeigen, Craigslist, extensible), dedup, draft generation, human-in-the-loop approval, auto-apply | 2 sources live, pluggable; 24h window; built | **private** |
| P22 | Self-Learning Token-Reduction Layer | AI DS | LLM gateway, exact + semantic caching, model routing, online learning from observed outcomes | 4 reduction mechanisms; results pending | **private** |

Repo URL = `https://github.com/gauravbhatia-bit/<repo>`

Live demos (link these when the JD mentions deployment, product sense or stakeholders):
- Sales Intelligence Agent — https://sales-intelligence-agent-5brv6ii7xelgzq7omewadn.streamlit.app/
- Office Energy Dashboard — https://office-energy-forecasting-dashboard-byb9cixihrwm3c779d3hpv.streamlit.app/
- Dutch Risk Radar — https://dutch-risk-radar-lu7gdrmdsmobmccabmbypw.streamlit.app/

**Do not list:** `testing1`, `testing.`, `pappu`, `machine-learning-practice`, `Machine-learning-intro`, `Churn-Analysis` (empty README), `berlin-football-analystics` (fun, not professional), `iran-energy-impact-analyzer` (superseded by P4), `ds-intern-challenge-submission` (someone else's brief).

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

**All three repos are private as of 30 Oct 2026** (Gaurav, confirmed). Do not go looking for them,
do not guess a slug, and never link a repo that 404s — a dead link costs more than no link.

On a CV they carry **"Private repo"** in the link column rather than a blank. A blank reads as an
oversight; "Private repo" says the code exists and is simply not open. It also sets up the obvious
interview question with an easy answer: it is live work.

> **Worth doing, and it is the cheapest win available.** Every other project here is verifiable in
> one click, and these three — the most impressive work in the library — are the only ones a reader
> has to take on trust. Making even one public changes that. P21 is the best candidate: it is
> built rather than in progress, and a sanitised version without credentials or scraping keys
> would be enough. Failing that, a README with screenshots in a public repo carries most of the
> benefit for an hour of effort. Raise this once; it is Gaurav's call, not a blocker.

### Numbers to add the moment they land

Not gates. These just turn a good line into a strong one, and P22's are days away.

| # | Add when available | Why that one |
|---|---|---|
| P20 | Reply or interview rate vs. his manual baseline | Volume proves a cron job runs. A reply rate proves the targeting and the generated documents work, which is the actual engineering. |
| P21 | Users, and listings ingested per day | Users is the one metric nothing else in this library has. One user outside himself changes what the project means. |
| P22 | **% token reduction at equal task quality**, with the quality guard named | A router can always cut tokens by downgrading the model. The pairing is the whole claim. |

### P20 — Job Search & Outreach Automation

Scheduled pipeline: pulls roles posted in the last 24h on LinkedIn across his city, Germany and
neighbouring European countries; identifies recently funded startups; generates a tailored CV and
cover letter per target; sends cold outreach with timed follow-ups; tracks who connects back on
LinkedIn. Runs unattended.

> **Flag this one before it goes near a German employer.** Two separate risks, and they are not
> theoretical.
>
> 1. **Platform terms.** LinkedIn's User Agreement prohibits automated scraping and automated
>    connection or messaging, and LinkedIn enforces it with account restrictions and bans. The
>    LinkedIn profile at risk is the one printed on his CV.
> 2. **German law on automated outreach.** Unsolicited commercial email to individuals is tightly
>    restricted under UWG §7, and processing scraped personal contact data engages GDPR Art. 6 and
>    the Art. 14 notice duty. A genuine job application is on far safer ground than marketing, but
>    *bulk automated sending to scraped personal addresses with automated follow-ups* is where the
>    distinction stops protecting him. This is a flag, not legal advice.
>
> **Practical mitigations**, all of which also make the CV line stronger rather than weaker: send to
> role-based addresses (`jobs@`, `careers@`) rather than scraped personal ones; keep volume
> human-scale; state plainly in every message that it is a job application; cap follow-ups at one
> or two; use LinkedIn's official Jobs API or exported data rather than scraping where possible;
> honour robots.txt and rate limits.
>
> **How to describe it on a CV.** Lead with the *system* — scheduling, deduplication, document
> generation, state tracking, human-in-the-loop — not with "scrapes LinkedIn and sends automated
> cold emails". The first is an engineer who ships. The second reads to a German hiring manager as
> a compliance problem walking through the door. Same project, and only one of the two descriptions
> is doing him a favour.

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

### P22 — Self-Learning Token-Reduction Layer

A gateway between application and LLM that cuts token spend through exact caching, semantic
caching and model routing. The stated differentiator is that it **learns over time**, improving its
own savings from observed traffic rather than from fixed rules.

**Status 30 Oct 2026:** final round of testing. Results expected within days — ask Gaurav for the
measured reduction and the quality guard before the next CV goes out, and put the number in here.

> **The architecture is well-trodden; the learning claim is the whole project.** Semantic caching
> and routing exist in GPTCache, semantic-router, LiteLLM and Portkey — an interviewer who works in
> this area will know that within one sentence, and will go straight to the differentiator. Three
> questions will come, and he should have answers ready:
> **learning from what signal, optimising what objective, and measured against what baseline.**
>
> The trap is that a router can always cut tokens by sending everything to the cheapest model. The
> claim only means something paired with a quality guard. Gaurav already knows how to do this
> properly and has done it once: the KnowGuard A/B test, where he set a practical-effect threshold
> *before* running and reported against it. **Same discipline here** — fix a quality metric and a
> floor, measure baseline spend, then report the reduction at or above that floor, with an interval.
> "Cut token spend 43% with no measurable drop in task accuracy (n=…, 95% CI …)" would be his best
> technical line on any CV. Until the tests land, describe the **mechanisms** — exact caching,
> semantic caching, routing, online adaptation — which is factual and specific, and keep the word
> "self-learning" next to what it actually learns from, so it reads as engineering rather than
> marketing.

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

**P20 Job Search & Outreach Automation** *(current — present tense)*
- Building an end-to-end job-search pipeline that ingests roles posted in the last 24 hours across his city, Germany and neighbouring European markets, scores them against a rule-governed content library, and generates a tailored CV and cover letter per target
- Automated the outreach and follow-up sequence with contact-state tracking, so each target is approached once and followed up on schedule rather than manually

**P21 Odd-Jobs Aggregator for Students in Germany** *(current)*
- Built a multi-source aggregator that collects odd-job listings posted in the last 24 hours across Kleinanzeigen, Craigslist and further pluggable sources, for international students who cannot search them by hand
- Generates the application message and a tailored CV per listing, and applies automatically once the user approves a shortlist — a deliberate human-in-the-loop step rather than full automation

**P22 Self-Learning Token-Reduction Layer** *(current — results pending)*
- Building an LLM gateway that cuts token spend through exact caching, semantic caching and model routing, with an online learning loop that adapts its routing from observed traffic instead of fixed rules
- Designing the evaluation so savings are reported against a measured baseline **and** a task-quality floor, since a router can always cut tokens by downgrading the model

> **Tense matters on these three.** P20 and P22 are in progress — "Building", "Designing".
> P21 is built — "Built". Do not write a past-tense completion claim for work still running, and
> do not hedge finished work into the present. A reader notices the mismatch before they notice
> anything else.

---
