# 📈 30-Day DataOps Learning Journey
### Building a Production-Grade US Stock Market Analytics Pipeline

> *A hands-on journey from DataOps fundamentals to a fully automated, CI/CD-driven stock market data pipeline — documented day by day.*

---

## 🧭 About This Repository

This repo documents my **30-day intensive DataOps learning path**, combining engineering best practices with real-world US stock market data analysis. Every day includes theory notes, hands-on code, and personal reflections.

**The goal:** Go from DataOps Level 1 (ad-hoc scripts) to Level 3 (automated, tested, observable pipelines) in 30 days.

---

## 🏗️ Final Architecture

```
Alpaca Market Data API
        │
        ▼  (Python ingestion — scheduled daily)
┌───────────────────┐
│   GCS Data Lake   │  raw / staging / marts
└───────────────────┘
        │
        ▼  (Databricks + Delta Lake)
┌───────────────────┐
│  Delta Tables     │  ACID, time-travel, incremental
└───────────────────┘
        │
        ▼  (dbt Core)
┌───────────────────────────────────┐
│  Transformation Layers            │
│  staging → intermediate → marts   │
└───────────────────────────────────┘
        │
        ▼  (mart_stock_signals)
   SMA / RSI / MACD / Golden Cross signals
        │
        ├──▶  Great Expectations (quality gates)
        ├──▶  Databricks Workflows (orchestration)
        └──▶  GitHub Actions CI/CD (automated deploy)
```

---

## 🛠️ Tech Stack

| Layer | Tool | Purpose |
|---|---|---|
| **Data Source** | Alpaca API (Paper Trading) | US equity historical & real-time data |
| **Remote Dev** | GCP Compute Engine + VS Code Remote SSH | Production-like development environment |
| **Data Lake** | Google Cloud Storage (GCS) | Raw / Staging / Marts storage layers |
| **Compute** | Databricks on GCP | Spark processing & job orchestration |
| **Table Format** | Delta Lake | ACID transactions, time travel |
| **Transformation** | dbt Core + dbt-databricks | SQL modeling, docs, lineage |
| **Data Quality** | Great Expectations | Automated data quality gates |
| **CI/CD** | GitHub Actions | Automated testing & deployment |
| **Version Control** | GitHub | Code, configs, and this journal |
| **IDE** | VS Code (Remote SSH to GCP VM) | Real-world remote dev workflow |

---

## 📅 30-Day Roadmap

### Week 1 — Foundation (Day 1–7)
> *Stand up the environment, ingest the first stock data pipeline*

| Day | Focus | Status |
|---|---|---|
| Day 1 | DataOps overview · GCP + GitHub project init | ⬜ |
| Day 2 | GCS data lake design · Bronze/Silver/Gold layers | ⬜ |
| Day 3 | Alpaca API ingestion · S&P 500 historical bars | ⬜ |
| Day 4 | Delta Lake fundamentals · ACID & time travel | ⬜ |
| Day 5 | Databricks Workflows · first scheduled job | ⬜ |
| Day 6 | Git workflow · branch strategy · PR conventions | ⬜ |
| Day 7 | Week 1 review · architecture diagram | ⬜ |

### Week 2 — Transformation Layer (Day 8–14)
> *Build dbt models, compute technical indicators*

| Day | Focus | Status |
|---|---|---|
| Day 8 | dbt setup · connect to Databricks | ⬜ |
| Day 9 | Staging models · data cleaning & type casting | ⬜ |
| Day 10 | Moving averages · SMA 20 / 60 / 200 in SQL | ⬜ |
| Day 11 | RSI 14-day · window functions deep dive | ⬜ |
| Day 12 | Incremental models · merge strategy | ⬜ |
| Day 13 | Marts layer · `mart_stock_signals` wide table | ⬜ |
| Day 14 | dbt docs · lineage graph · schema.yml | ⬜ |

### Week 3 — Quality & Observability (Day 15–21)
> *Make the pipeline trustworthy — catch bad data automatically*

| Day | Focus | Status |
|---|---|---|
| Day 15 | dbt tests · 5 dimensions of data quality | ⬜ |
| Day 16 | Great Expectations · expectation suites | ⬜ |
| Day 17 | Data freshness · SLA monitoring · market calendar | ⬜ |
| Day 18 | Alerting · Databricks job failure notifications | ⬜ |
| Day 19 | Anomaly detection · Z-score on price data | ⬜ |
| Day 20 | Data contracts · schema.yml as API contract | ⬜ |
| Day 21 | Chaos day · fault injection & monitoring drill | ⬜ |

### Week 4 — CI/CD & Full Automation (Day 22–30)
> *Wire everything together into a production-grade DataOps system*

| Day | Focus | Status |
|---|---|---|
| Day 22 | GitHub Actions CI · dbt compile + test on PR | ⬜ |
| Day 23 | Multi-environment · dev / staging / prod isolation | ⬜ |
| Day 24 | CD pipeline · auto-deploy on merge to main | ⬜ |
| Day 25 | End-to-end integration test | ⬜ |
| Day 26 | Performance tuning · OPTIMIZE / ZORDER / partitioning | ⬜ |
| Day 27 | Stress test · simulate earnings season data spike | ⬜ |
| Day 28 | Expand coverage · add 10 new symbols incrementally | ⬜ |
| Day 29 | Documentation · ADRs · final README | ⬜ |
| Day 30 | Demo & retrospective | ⬜ |

---

## 📁 Repository Structure

```
stock-dataops/
│
├── ingestion/                  # Python scripts — Alpaca API → GCS
│   ├── alpaca_daily_bars.py
│   ├── alpaca_intraday.py
│   └── utils/
│       ├── gcs_client.py
│       └── market_calendar.py
│
├── dbt/                        # dbt project
│   ├── models/
│   │   ├── staging/            # stg_stock_bars.sql
│   │   ├── intermediate/       # int_moving_averages.sql, int_rsi.sql
│   │   └── marts/              # mart_stock_signals.sql
│   ├── tests/                  # Custom dbt tests
│   ├── macros/
│   └── dbt_project.yml
│
├── great_expectations/         # Data quality suites
│   ├── expectations/
│   │   ├── alpaca_raw_suite.json
│   │   └── mart_signals_suite.json
│   └── checkpoints/
│
├── .github/
│   └── workflows/
│       ├── ci.yml              # PR: dbt compile + test
│       └── cd.yml              # Merge to main: deploy to prod
│
├── data_contracts/             # Schema contracts for downstream consumers
│   └── mart_stock_signals.yaml
│
├── docs/                       # Architecture diagrams, ADRs
│   ├── architecture.md
│   ├── adr/
│   │   ├── ADR-001-databricks-workflows-vs-airflow.md
│   │   └── ADR-002-delta-lake-storage-format.md
│   └── daily_logs/             # Daily learning notes (Week 1–4)
│
├── notebooks/                  # Databricks notebooks for exploration
│
└── README.md
```

---

## 📓 Daily Learning Log

Each day has a dedicated note under `docs/daily_logs/`:

```
docs/daily_logs/
├── week1/
│   ├── day01.md
│   ├── day02.md
│   └── ...
├── week2/
├── week3/
└── week4/
```

**Log template per day:**

```markdown
# Day N — [Title]

## What I Learned
...

## What I Built
...

## Blockers & How I Solved Them
...

## Key Takeaway
...
```

---

## 🚀 Getting Started

### Prerequisites

- GCP account with Compute Engine + GCS + BigQuery APIs enabled
- Databricks workspace on GCP
- Alpaca Paper Trading account → [Sign up free](https://alpaca.markets)
- VS Code with **Remote - SSH** extension installed

### 1. Connect VS Code to GCP VM

```bash
# On your local machine — add to ~/.ssh/config
Host gcp-dataops
    HostName <YOUR_VM_EXTERNAL_IP>
    User <YOUR_USERNAME>
    IdentityFile ~/.ssh/gcp_key

# Then in VS Code: Ctrl+Shift+P → "Remote-SSH: Connect to Host" → gcp-dataops
```

### 2. Clone & Setup on the VM

```bash
git clone https://github.com/<your-username>/stock-dataops.git
cd stock-dataops

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Secrets

```bash
cp .env.example .env
# Fill in:
# ALPACA_API_KEY=...
# ALPACA_SECRET_KEY=...
# GCS_BUCKET=...
# DATABRICKS_HOST=...
# DATABRICKS_TOKEN=...
```

### 4. Run First Ingestion

```bash
python ingestion/alpaca_daily_bars.py --symbols AAPL MSFT NVDA SPY --start 2022-01-01
```

---

## 📊 Stock Universe

Initial coverage: **Top 20 S&P 500 components by market cap**

```
AAPL  MSFT  NVDA  AMZN  META
GOOGL GOOG  BRK.B LLY   JPM
V     UNH   XOM   TSLA  MA
PG    JNJ   AVGO  HD    MRK
```

Index ETF benchmark: **SPY** (S&P 500), **QQQ** (Nasdaq 100)

---

## 🔑 Key Concepts Covered

**DataOps**
- DataOps maturity model (Level 1 → Level 4)
- Data contracts and SLA definition
- Observability: lineage, freshness, anomaly detection

**Data Engineering**
- Data lake architecture (Bronze / Silver / Gold)
- Delta Lake: ACID, time travel, schema evolution
- Incremental loading patterns (merge, append, insert-overwrite)
- Orchestration: Databricks Workflows, DAG design principles

**dbt**
- Layered modeling: staging → intermediate → marts
- Incremental materializations
- Testing, documentation, and lineage graphs

**Data Quality**
- Great Expectations: Expectation Suites & Checkpoints
- Multi-layer quality gates (dbt tests + GE)
- Z-score based anomaly detection

**CI/CD**
- GitHub Actions: PR validation pipeline
- Multi-environment isolation (dev / staging / prod)
- Automated deployment on merge

---

## 📈 Target Output — `mart_stock_signals`

| Column | Description |
|---|---|
| `symbol` | Ticker (e.g. AAPL) |
| `trade_date` | NYSE trading date |
| `open_price` | Adjusted open |
| `close_price` | Adjusted close |
| `volume` | Daily volume |
| `vwap` | Volume-weighted avg price |
| `sma_20` | 20-day simple moving average |
| `sma_60` | 60-day simple moving average |
| `sma_200` | 200-day simple moving average |
| `rsi_14` | 14-day RSI (0–100) |
| `signal_type` | `GOLDEN_CROSS` / `DEATH_CROSS` / null |

---

## 🧠 Reflections

> *This section is updated at the end of each week.*

**Week 1:** *(coming soon)*

**Week 2:** *(coming soon)*

**Week 3:** *(coming soon)*

**Week 4:** *(coming soon)*

---

## 📚 References & Resources

- [Alpaca Market Data API Docs](https://docs.alpaca.markets/reference/stockbars)
- [dbt Core Documentation](https://docs.getdbt.com)
- [Great Expectations Docs](https://docs.greatexpectations.io)
- [Databricks Delta Lake Guide](https://docs.databricks.com/delta/index.html)
- [DataOps Manifesto](https://dataopsmanifesto.org)
- [The DataOps Cookbook](https://datakitchen.io/the-dataops-cookbook/)

---

## 📄 License

MIT License — feel free to fork, adapt, and build on this for your own learning journey.

---

*Started: April 2026 · Built on GCP + Databricks + dbt + Great Expectations*
