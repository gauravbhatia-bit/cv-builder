"""Builds the eight role CVs in roles/ from templates/base-2page.html (its look, header, projects).

    python scripts/build_roles.py

Each role CV is a finished, checked, two-page CV for one job family. For a real job, copy the matching
file into out/, change the headline to the ad's own job title, and render. Nothing else needs rebuilding.
Edit a role here (ROLES), not in roles/*.html, or the next run overwrites the hand edit.
Every sentence below comes from data/master.md or data/projects.md; scripts/check.py enforces it.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = (ROOT / "templates" / "base-2page.html").read_text(encoding="utf-8").replace("\r\n", "\n")
GH = "https://github.com/gauravbhatia-bit/"

# ---------- pieces copied from the base template, so the look and shared text never drift ----------
PAGE_OPEN = '<div class="page" contenteditable="true" spellcheck="false">\n'
head_end = BASE.index(PAGE_OPEN) + len(PAGE_OPEN)
HEAD = BASE[:head_end]
HEADER = BASE[head_end:BASE.index("  <h2>Data Scientist</h2>")]
TAIL = BASE[BASE.index("\n</div>\n\n<script>"):]
EDU = BASE[BASE.index("  <h2>Education</h2>"):BASE.index("  <h2>Selected Projects</h2>")]
CERTS = BASE[BASE.index("  <h2>Certifications</h2>"):BASE.index("\n</div>\n\n<script>")]
START = "  <h2>Selected Projects</h2>\n\n"
proj_text = BASE[BASE.index(START) + len(START):BASE.index("  <h2>Certifications</h2>")].strip("\n")
BLOCKS = re.split(r'\n\n(?=  <div class="entry">)', proj_text)
PARSED = {re.search(r'class="pname">(.*?)</span>', b).group(1): b for b in BLOCKS}


def from_base(fragment, n=None):
    """A project block from the base template, optionally cut to its first n bullets."""
    blk = next(b for k, b in PARSED.items() if fragment in k)
    if n is None:
        return blk
    lis = re.findall(r"      <li>.*?</li>\n", blk, re.S)
    head = blk[:blk.index("    <ul>")]
    return head + "    <ul>\n" + "".join(lis[:n]) + "    </ul>\n  </div>"


def new_project(name, stack, link, bullets, n=None):
    lis = "".join(f"      <li>{b}</li>\n" for b in bullets[:n])
    return (f'  <div class="entry">\n    <div class="prow">\n      <span class="pname">{name}</span>\n'
            f'      <span class="pstack">{stack}</span>\n      <span class="plink">{link}</span>\n    </div>\n'
            f'    <ul>\n{lis}    </ul>\n  </div>')


def src(repo):
    return f'<a href="{GH}{repo}">Source</a>'


PROJECTS = {
    "pareto": lambda n=None: from_base("ParetoGate", n),
    "thesis": lambda n=None: from_base("MSc Thesis", n),
    "jobs": lambda n=None: from_base("Job-Search", n),
    "odd": lambda n=None: from_base("Odd-Jobs", n),
    "pricing": lambda n=None: from_base("Dynamic Pricing", n),
    "sales": lambda n=None: from_base("Sales Intelligence", n),
    "demand": lambda n=None: from_base("Demand Forecasting", n),
    "office": lambda n=None: from_base("Office Energy", n),
    "dq": lambda n=None: from_base("BI Data-Quality", n),
    "pay": lambda n=None: from_base("Payments BI", n),
    "rag": lambda n=None: new_project(
        "RAG Retail Agent", "LangChain, FAISS, FastAPI, Docker, Kubernetes", src("rag-retail-agent"),
        ["Built a <strong>LangChain + FAISS</strong> retrieval pipeline over product data behind a <strong>FastAPI</strong> service, with <strong>GitHub Actions to Docker Hub to Kubernetes</strong> CI/CD"], n),
    "solar": lambda n=None: new_project(
        "Solar Power Forecasting (LSTM)", "TensorFlow/Keras, OPSD, Open-Meteo", src("solar-power-forecasting"),
        ["Forecast hourly German solar generation with an <strong>LSTM</strong> on <strong>26,280 hourly rows</strong>, using a chronological 70/15/15 split to prevent leakage",
         "Evaluated on held-out data with RMSE, MAE and MAPE"], n),
    "news": lambda n=None: new_project(
        "Energy News and Price Volatility (NLP)", "FinBERT, VADER, TF-IDF, XGBoost, SHAP", src("energy-news-volatility-nlp"),
        ["Predicted high-volatility days on EPEX Spot from <strong>4,444 energy headlines</strong> using FinBERT and VADER sentiment, TF-IDF trend signals and Google Trends attention",
         "Compared <strong>four models</strong> (dummy, FinBERT-only, default and tuned XGBoost) with SHAP attributions and Granger-causality-informed lags"], n),
    "solar_da": lambda n=None: new_project(
        "Solar Demand Analytics", "DuckDB SQL, Open-Meteo, SMARD, Power BI", src("solar-demand-analytics"),
        ["Modelled German solar generation and weather in <strong>DuckDB SQL</strong> (window functions, views) and exported to <strong>Power BI</strong>: summer output 4x winter, cloud cover above 75% cuts generation ~40%"], n),
    "toll": lambda n=None: new_project(
        "Toll Traffic Reporting and Anomaly Suite", "DuckDB, SQL, Isolation Forest, APScheduler, Jinja2", src("toll-sql-reporting-pipeline"),
        ["Built <strong>SQL reporting</strong> (CTEs, window functions, RANK), <strong>Z-score and Isolation Forest</strong> anomaly detection, and a scheduled weekly HTML KPI report over German highway toll data",
         "Covers 6 months of hourly data across 5 autobahn segments with 4 standing reports; the Monday 08:00 report is <strong>fully automated</strong>"], n),
    "funnel": lambda n=None: new_project(
        "Marketing Funnel Dashboard", "Python, SQLite, Matplotlib", src("marketing-funnel-dashboard"),
        ["Tracked impressions to clicks to leads to customers with <strong>CAC and CVR per channel</strong> across 5 channels and 52 weeks, in SQL plus a Python dashboard"], n),
    "sales_an": lambda n=None: new_project(
        "Bhatia Traders Sales Analysis", "Python, pandas, Matplotlib", src("bhatia-traders-sales-analysis"),
        ["Analysed the sales of the business he ran, using moving averages and a margin ranking by product, and sized a ~<strong>15% stockout-reduction</strong> potential",
         "The demand patterns it surfaced became the basis of the Demand Forecasting Engine"], n),
    "inv_alert": lambda n=None: new_project(
        "Inventory Alert System", "MySQL (CASE, JOINs, UPDATE)", src("bhatia_traders_inventory_alert_system"),
        ["Built MySQL queries that raise automated <strong>low-stock alerts at a 20% threshold</strong> with reorder recommendations for a sauces and condiments business"], n),
}

# ---------- experience bullets ----------
K = {
    "bench": "<strong>Benchmark LLMs against baselines</strong> and design <strong>cost-effective evaluation workflows</strong> for model selection",
    "ab": "Ran a <strong>paired A/B test on AWS</strong> comparing a fine-tuned model against the review arm: <strong>+0.0318 AUPRC</strong> (95% CI 0.022–0.0418), below the pre-set 0.05 practical-effect threshold",
    "rag": "Build <strong>RAG pipelines</strong> and <strong>multi-agent systems</strong>, and define evaluation metrics and hold-out sets so model comparisons are reproducible rather than anecdotal",
    "evalm": "Defined evaluation metrics and hold-out sets, and set the <strong>practical-effect threshold before testing</strong>, so a statistically positive result was still called correctly as not worth shipping",
}
T = {
    "inv": "Monitored inventory and demand across <strong>700+ vendors</strong> and <strong>500+ SKUs</strong> in Tally and Excel",
    "bi": "Built <strong>Power BI dashboards across 3 divisions</strong>, turning operational data into clear views for non-technical stakeholders",
    "export": "Rescued a stalled <strong>₹2.75M export order</strong> (500 units to Lithuania) by moving the shipment to <strong>air freight</strong> to hold the delivery window and renegotiating terms with the client",
    "owner": "Was handed that order <strong>end to end</strong> and ran every part: sourced and booked it at the manufacturer in person, costed it at ₹5,500/unit, arranged freight and carried the client through to delivery",
    "report": "Worked directly with operations and supply-chain stakeholders to turn recurring questions into <strong>standing reports</strong>",
}
B = {
    "own": "Ran a product business end to end for <strong>8 years</strong>, owning purchasing, pricing, stock and supplier terms across <strong>20+ suppliers</strong>",
    "inv": "Analysis-led changes cut <strong>excess-inventory cost by 10%</strong> and identified a ~<strong>15% stockout-reduction</strong> potential",
    "vent": "Ran three ventures alongside it: a <strong>home-tutoring marketplace</strong>, <strong>Shopify e-commerce stores</strong> and a restaurant",
    "fc": "Demand patterns from this business became the basis of the <strong>Demand Forecasting Engine</strong> project",
}


def job(title, dates, org, place, bullets):
    lis = "".join(f"      <li>{b}</li>\n" for b in bullets)
    return (f'  <div class="entry">\n    <div class="row"><span class="t">{title}</span><span class="r">{dates}</span></div>\n'
            f'    <div class="row"><span class="sub">{org}</span><span class="r sub">{place}</span></div>\n'
            f'    <ul>\n{lis}    </ul>\n  </div>\n')


def experience(k, t, b):
    return ("  <h2>Experience</h2>\n\n"
            + job("Data Science Intern", "Aug 2026 – Present", "KnowGuard AI", "Berlin, Germany", [K[x] for x in k]) + "\n"
            + job("Operations &amp; Supply Chain Analyst", "Mar 2024 – Jul 2025", "Troika International Pvt. Ltd.", "Panchkula, India", [T[x] for x in t]) + "\n"
            + job("Business Manager", "Nov 2015 – Jan 2024", "Bhatia Traders", "India", [B[x] for x in b]) + "\n")


# ---------- skills rows ----------
S = {
    "methods": ("Methods", "Regression (incl. log-log OLS elasticity), A/B testing, time-series (ARIMA, Prophet, LSTM, Chronos), RFM segmentation, anomaly detection, event study, Granger causality, model evaluation (MAE, RMSE, MAPE), SHAP"),
    "methods_da": ("Methods", "Regression, A/B testing, time-series forecasting (ARIMA, Prophet), RFM segmentation, anomaly detection (Z-score, Isolation Forest), funnel analysis (CAC, CVR), model evaluation (MAE, RMSE, MAPE)"),
    "methods_fc": ("Methods", "Demand forecasting (ARIMA, Prophet, XGBoost), regression and price elasticity, RFM segmentation, anomaly detection, model evaluation (MAE, RMSE, MAPE)"),
    "methods_ba": ("Methods", "Price elasticity and regression, A/B testing, RFM segmentation, funnel analysis (CAC, CVR), demand forecasting (ARIMA, Prophet), model evaluation (MAE, RMSE, MAPE)"),
    "prog": ("Programming", "Python (pandas, NumPy, statsmodels, scikit-learn, XGBoost, Optuna, TensorFlow/Keras), SQL (CTEs, window functions), DuckDB, Snowflake SQL, SQLite"),
    "prog_py": ("Programming", "Python (pandas, NumPy, statsmodels, scikit-learn, XGBoost), SQL (CTEs, window functions), DuckDB, MySQL, SQLite"),
    "sql": ("SQL &amp; data", "SQL (CTEs, window functions, CASE, JOINs), DuckDB, Snowflake SQL, MySQL, SQLite, star-schema modelling, data-quality checks, Python (pandas, NumPy)"),
    "sql_de": ("SQL &amp; modelling", "SQL (CTEs, window functions, views), DuckDB, Snowflake SQL, MySQL, SQLite, DWH / star-schema modelling, ETL processes, Python (pandas, NumPy)"),
    "bi": ("Charts &amp; reporting", "Power BI / DAX, Plotly, Streamlit dashboards, automated Markdown/HTML KPI reports, Excel, Tally"),
    "bi_da": ("Charts &amp; reporting", "Power BI / DAX, Plotly, Matplotlib, Streamlit dashboards, Jinja2 HTML reports, automated KPI reports, Excel, Tally"),
    "ml": ("Machine learning", "scikit-learn, XGBoost, TensorFlow/Keras (LSTM), Optuna hyperparameter tuning, SHAP explainability, time-series (ARIMA, Prophet, Chronos), model evaluation (MAE, RMSE, MAPE), A/B testing"),
    "serve": ("Serving &amp; delivery", "FastAPI, REST APIs, Docker, Kubernetes, GitHub Actions CI/CD, Git/GitHub, AWS (A/B testing workloads), reproducible and documented pipelines"),
    "serve_ai": ("Serving &amp; delivery", "FastAPI, REST APIs, Docker, Kubernetes, GitHub Actions CI/CD, Ollama, LM Studio, AWS, Git/GitHub"),
    "pipes": ("Pipelines &amp; delivery", "ETL processes, data-quality validation (a 45-check suite), scheduled pipelines (APScheduler), REST APIs, FastAPI, Docker, GitHub Actions CI/CD, Git/GitHub, documented and reproducible pipelines"),
    "ai_short": ("AI engineering", "LLM evaluation and quality gates, guardrails, RAG (LangChain, FAISS), agentic workflows, semantic caching and model routing, LLM cost optimisation, human-in-the-loop design, MiniLM embeddings, Hugging Face"),
    "ai_eval": ("LLM evaluation", "LLM evaluation and quality gates, benchmark and hold-out design, regression testing for LLM systems, guardrails, RAG (LangChain, FAISS), context engineering, model routing, LLM cost optimisation, FinBERT / Hugging Face"),
    "ai": ("AI engineering", "LLM evaluation and quality gates, guardrails, agentic workflows and multi-agent orchestration, agent harness engineering (validators, receipts, rollback), versioned prompts and releases, RAG (LangChain, FAISS), context engineering, semantic caching and model routing, LLM cost optimisation, human-in-the-loop design, structured outputs (JSON Schema), local model serving (Ollama, LM Studio), MiniLM embeddings, Hugging Face, Gemini"),
    "cloud": ("Cloud &amp; engineering", "AWS, Azure data platform (FutureLearn coursework), FastAPI, Docker, GitHub Actions, Git/GitHub, Agile/Jira"),
    "cloud_da": ("Platforms &amp; workflow", "Azure data platform (FutureLearn coursework), AWS fundamentals, Git/GitHub, Agile (Scrum, Kanban), Jira, stakeholder communication"),
    "cloud_de": ("Cloud &amp; platforms", "Azure data platform (FutureLearn coursework: data engineering with Microsoft Azure), AWS, Snowflake, Docker, Kubernetes, Agile/Jira"),
    "supply": ("Supply chain &amp; operations", "Inventory and demand monitoring, demand forecasting (ARIMA, Prophet, XGBoost), stock-level and reorder analysis, supplier and vendor management, export logistics and freight-mode decisions, Tally ERP"),
    "ba": ("Business analysis", "Requirements management, stakeholder communication, KPI dashboards and reporting, Agile (Scrum, Kanban), Jira, documented and reproducible analysis"),
    "lang": ("Languages", "English (C1), German (A2, improving), Hindi (native)"),
}
EDU_MODULES = "\n      <li>Relevant modules: Methods of Prediction (M507), Big Data Analytics (M508)</li>"
THESIS_SHORT = "Thesis: the US–Iran conflict's impact on the German electricity market"
AVAIL = "Available full-time in Berlin from <strong>December 2026</strong>."


def skills(keys):
    rows = "".join(f"    <dt>{S[k][0]}</dt><dd>{S[k][1]}</dd>\n" for k in keys)
    return f'  <h2>Skills</h2>\n  <dl class="skills">\n{rows}  </dl>\n\n'


def education(short, modules):
    out = EDU
    if short:
        out = re.sub(r"<li>Thesis:.*?</li>", f"<li>{THESIS_SHORT}</li>", out, flags=re.S)
    if modules:
        out = out.replace("</li>", "</li>" + EDU_MODULES, 1)
    return out


ROLES = [
    dict(file="Junior_Data_Scientist", title="Junior Data Scientist", headline="Junior Data Scientist",
         profile="MSc Data Science candidate at GISMA, finishing December 2026, with a thesis on German power prices. Builds models people can act on: price elasticity on <strong>15,000 SKUs</strong>, demand forecasts that beat ARIMA at <strong>6.07% MAPE</strong>, and a paired A/B test reported with its confidence interval. Strong in <strong>statistics</strong> and reproducible <strong>Python/SQL</strong>, after eight years running a business where the analysis had to pay for itself. " + AVAIL,
         skills=["methods", "prog", "bi", "ai_short", "cloud", "lang"],
         exp=(["ab", "rag", "bench"], ["inv", "bi", "export"], ["own", "inv"]), short=False, modules=True,
         projects=[("thesis", 2), ("pricing", 2), ("demand", 2), ("pareto", 2), ("sales", 2), ("office", 2), ("solar", 2), ("news", 2), ("dq", 2), ("jobs", 2)]),
    dict(file="Junior_ML_Engineer", title="Junior ML Engineer", headline="Junior Machine Learning Engineer",
         profile="MSc Data Science candidate at GISMA, finishing December 2026, who ships models as services. Builds with <strong>Python, scikit-learn, XGBoost and TensorFlow</strong>, tunes against hold-out data (<strong>50 Optuna trials</strong>, MAE 22.98 Wh), and serves them through <strong>FastAPI and Docker</strong>. Evaluates model variants at KnowGuard AI, and is building ParetoGate, an LLM gateway with ten trained classifiers. " + AVAIL,
         skills=["ml", "prog", "serve", "ai_short", "lang"],
         exp=(["rag", "ab", "bench"], ["inv", "bi", "export"], ["own", "inv"]), short=False, modules=True,
         projects=[("pareto", 3), ("sales", 2), ("rag", 1), ("office", 2), ("solar", 2), ("thesis", 2), ("demand", 2), ("pricing", 2), ("jobs", 2), ("news", 2)]),
    dict(file="Applied_Scientist", title="Applied Scientist", headline="Applied Scientist",
         profile="MSc Data Science candidate at GISMA, finishing December 2026. Applies <strong>experimental and statistical methods</strong> to real decisions: a paired A/B test with a pre-set effect threshold, <strong>event study and Granger causality</strong> on German power prices, and price elasticity on <strong>15,000 SKUs</strong>. Documents results that do not favour the idea, including a negative end-to-end run of ParetoGate, the LLM gateway now in development. " + AVAIL,
         skills=["methods", "prog", "ai_eval", "cloud", "bi", "lang"],
         exp=(["ab", "evalm", "bench"], ["inv", "bi", "export"], ["own", "inv"]), short=False, modules=True,
         projects=[("thesis", 2), ("pareto", 3), ("pricing", 2), ("news", 2), ("demand", 2), ("sales", 2), ("office", 2), ("solar", 2), ("jobs", 2), ("dq", 2)]),
    dict(file="AI_LLM_GenAI_Engineer", title="AI LLM GenAI Engineer", headline="AI / LLM / GenAI Engineer",
         profile="MSc Data Science candidate at GISMA, finishing December 2026, building LLM systems where cost, quality and safety are measured. ParetoGate cut retrieved context from <strong>86,416 to 11,351 input tokens</strong> behind a quality gate, and an <strong>agent harness</strong> with 37 standing rules runs four scheduled tasks. Experience with <strong>RAG</strong>, LLM evaluation at KnowGuard AI and human-in-the-loop design. " + AVAIL,
         skills=["ai", "prog", "serve_ai", "methods_da", "lang"],
         exp=(["bench", "rag", "ab"], ["bi", "export"], ["own"]), short=False, modules=True,
         projects=[("pareto", 4), ("jobs", 4), ("odd", 2), ("sales", 2), ("rag", 1), ("news", 2), ("thesis", 2), ("office", 2)]),
    dict(file="Data_Analyst_BI_Analyst", title="Data Analyst BI Analyst", headline="Data Analyst / BI Analyst",
         profile="Data analyst finishing an MSc in Data Science at GISMA in December 2026, after eight years running a business on its own numbers. Turns messy operational data into clear views: <strong>Power BI dashboards across 3 divisions</strong>, <strong>45 automated data-quality checks</strong> and <strong>SQL</strong> reporting (CTEs, window functions) over a 7-table star schema. Explains results to non-technical stakeholders. " + AVAIL,
         skills=["sql", "bi_da", "methods_da", "cloud_da", "lang"],
         exp=(["ab", "evalm"], ["bi", "report", "inv", "export"], ["own", "inv"]), short=True, modules=False,
         projects=[("pay", 1), ("dq", 2), ("solar_da", 1), ("toll", 2), ("pricing", 2), ("funnel", 1), ("thesis", 2), ("demand", 2), ("sales_an", 2), ("inv_alert", 1)]),
    dict(file="Analytics_Engineer_Data_Engineer", title="Analytics Engineer Data Engineer", headline="Analytics Engineer / Junior Data Engineer",
         profile="MSc Data Science candidate at GISMA, finishing December 2026, who builds the data layer that analysis depends on. Writes <strong>SQL</strong> (CTEs, window functions) in DuckDB and Snowflake, models <strong>star schemas</strong>, and automates validation: <strong>45 checks</strong> across 7 tables that traced two silent data losses. Schedules and ships pipelines with Python, Docker and GitHub Actions. " + AVAIL,
         skills=["sql_de", "pipes", "cloud_de", "bi", "lang"],
         exp=(["rag", "ab"], ["bi", "report", "inv"], ["own"]), short=False, modules=True,
         projects=[("dq", 2), ("toll", 2), ("solar_da", 1), ("pay", 1), ("jobs", 3), ("rag", 1), ("odd", 2), ("thesis", 2), ("inv_alert", 1)]),
    dict(file="Supply_Chain_Operations_Analyst", title="Supply Chain Operations Analyst", headline="Supply Chain &amp; Demand Planning Analyst",
         profile="Operations and supply chain analyst finishing an MSc in Data Science at GISMA in December 2026. Monitored inventory and demand across <strong>700+ vendors and 500+ SKUs</strong> at Troika, rescued a <strong>₹2.75M export order</strong> by moving it to air freight, and ran a business for eight years, cutting <strong>excess-inventory cost by 10%</strong>. Adds forecasting: Prophet at <strong>6.07% MAPE</strong> on weekly SKU demand. Works in Tally, Excel and Power BI. " + AVAIL,
         skills=["supply", "bi", "prog_py", "methods_fc", "lang"],
         exp=(["ab"], ["inv", "report", "export", "owner", "bi"], ["own", "inv", "vent", "fc"]), short=True, modules=False,
         projects=[("demand", 2), ("sales_an", 2), ("inv_alert", 1), ("pricing", 2), ("dq", 2), ("thesis", 2), ("pay", 1), ("toll", 1), ("office", 2)]),
    dict(file="Business_Analyst", title="Business Analyst", headline="Business Analyst",
         profile="Business analyst finishing an MSc in Data Science at GISMA in December 2026, after eight years owning purchasing, pricing and stock decisions. Turns business questions into analysis people act on: repricing <strong>55.7% of a catalogue</strong> from elasticity models, KPI dashboards for non-technical stakeholders across <strong>3 divisions</strong>, and funnel and payments reporting. Works in Agile teams with Jira. " + AVAIL,
         skills=["ba", "bi_da", "prog_py", "methods_ba", "lang"],
         exp=(["ab", "evalm"], ["report", "bi", "inv", "export"], ["own", "inv", "vent"]), short=True, modules=False,
         projects=[("pricing", 2), ("pay", 1), ("funnel", 1), ("demand", 2), ("odd", 2), ("dq", 2), ("thesis", 2), ("jobs", 2), ("sales_an", 2)]),
]


def build(r):
    k, t, b = r["exp"]
    projs = "\n\n".join(PROJECTS[key](n) for key, n in r["projects"])
    body = (HEADER + f"  <h2>{r['headline']}</h2>\n  <p>{r['profile']}</p>\n\n" + skills(r["skills"])
            + experience(k, t, b) + education(r["short"], r["modules"])
            + "  <h2>Selected Projects</h2>\n\n" + projs + "\n\n" + CERTS)
    head = HEAD.replace("<title>Gaurav Bhatia CV (2 page)</title>", f"<title>Gaurav Bhatia CV {r['title']}</title>")
    return head + body + TAIL


if __name__ == "__main__":
    (ROOT / "roles").mkdir(exist_ok=True)
    for r in ROLES:
        path = ROOT / "roles" / f"Gaurav_Bhatia_CV_{r['file']}.html"
        path.write_text(build(r), encoding="utf-8", newline="\n")
        print(path.relative_to(ROOT))
