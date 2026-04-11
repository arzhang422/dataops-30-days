# Day 1 — DataOps Overview & Environment Initialization

## What I Learned

### DataOps Fundamentals
- DataOps is not a tool — it is a methodology that applies DevOps principles
  to data engineering: version control everything, automate testing, and
  build observability into every layer of the pipeline.
- DataOps Maturity Model:
  - Level 1: Ad-hoc scripts, manual runs, no version control
  - Level 2: Scripts in Git, some scheduling, manual deployments
  - Level 3: Automated CI/CD, data quality gates, observable pipelines
  - Level 4: Self-healing pipelines, predictive monitoring (30-day target: Level 3)

### Secret Management Principles
- Never hardcode credentials in source code — even in private repos.
- Local development: load secrets from a `.env` file via `python-dotenv`.
- Production (Databricks): use Databricks Secrets Backend
  (`dbutils.secrets.get(scope, key)`) — to be wired up on Day 5.
- The `utils/config.py` module abstracts the source of secrets so the
  rest of the codebase never calls `os.environ` directly.

### GCS Medallion Path Convention
- `bronze/<dataset>/date=YYYY-MM-DD/` — raw, immutable, as-received from source
- `silver/<dataset>/date=YYYY-MM-DD/` — cleaned, typed, deduplicated
- `gold/<dataset>/date=YYYY-MM-DD/`  — business-ready aggregates and signals
- Date partitioning allows Spark/Databricks to apply partition pruning,
  dramatically reducing scan costs on large datasets.

## What I Built

| File | Purpose |
|---|---|
| `requirements.txt` | Pinned dependencies for Day 1 (alpaca-py, GCS, pandas, pyarrow) |
| `.env.example` | Template listing all required secrets — safe to commit |
| `.gitignore` | Excludes `.env`, service account JSON, `.venv`, and dbt artifacts |
| `ingestion/utils/config.py` | Env-aware config loader — single source of truth for all settings |
| `ingestion/utils/gcs_client.py` | GCS read/write wrapper with Bronze/Silver/Gold path convention |
| `docs/daily_logs/week1/day01.md` | This file |

Directory skeleton created:
ingestion/utils/
dbt/models/{staging,intermediate,marts}/
great_expectations/{expectations,checkpoints}/
.github/workflows/
data_contracts/
docs/{adr,daily_logs/{week1,week2,week3,week4}}/
notebooks/

## Blockers & How I Solved Them

*(Record any issues you hit and how you resolved them — e.g. SSH key
permissions, gcloud zone flags, pip install conflicts. Future-you will
thank you for writing this down.)*

Example format:
- **Problem**: `Permission denied (publickey)` on first SSH attempt.
- **Cause**: Private key file permissions were 644 instead of 600.
- **Fix**: `chmod 600 ~/.ssh/google_compute_engine`

## Key Takeaway

Environment setup is the foundation of the entire project. Getting SSH
config, secret management, and directory conventions right on Day 1 means
the next 29 days can stay focused on data logic — not debugging
infrastructure. A `config.py` that hides the secret source makes
promoting code from local to production a one-line change, not a
refactor.

## Tomorrow — Day 2 Preview

- Create the `dataops-30-days-lake` GCS bucket via `gsutil` / Terraform.
- Design the full Bronze / Silver / Gold directory structure.
- Write `ingestion/utils/market_calendar.py` — NYSE trading day awareness
  so the pipeline knows when NOT to run.