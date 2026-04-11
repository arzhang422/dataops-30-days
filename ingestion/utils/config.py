"""
config.py — 统一配置加载器

规则：
- 本地开发：从 .env 文件读取
- Databricks 生产环境：从 Databricks Secrets Backend 读取（Day 5 升级）
- 代码里永远只 import config，不直接用 os.environ
"""

import os
from dotenv import load_dotenv

load_dotenv()  # 本地读 .env；生产环境无副作用


class Config:
    # ── Alpaca ──────────────────────────────────────────
    ALPACA_API_KEY: str = os.environ["ALPACA_API_KEY"]
    ALPACA_SECRET_KEY: str = os.environ["ALPACA_SECRET_KEY"]
    ALPACA_BASE_URL: str = "https://paper-api.alpaca.markets"

    # ── GCP / GCS ───────────────────────────────────────
    GCS_BUCKET: str = os.environ["GCS_BUCKET"]
    GCP_PROJECT_ID: str = os.environ["GCP_PROJECT_ID"]

    # Bronze/Silver/Gold 路径前缀
    GCS_BRONZE_PREFIX: str = "bronze"
    GCS_SILVER_PREFIX: str = "silver"
    GCS_GOLD_PREFIX: str = "gold"

    # ── Databricks (Day 5 启用) ─────────────────────────
    DATABRICKS_HOST: str = os.environ.get("DATABRICKS_HOST", "")
    DATABRICKS_TOKEN: str = os.environ.get("DATABRICKS_TOKEN", "")


config = Config()
