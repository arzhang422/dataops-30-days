"""
gcs_client.py — GCS 读写工具

封装 google-cloud-storage，提供：
- upload_dataframe()  : pandas DataFrame → GCS Parquet
- download_dataframe(): GCS Parquet → pandas DataFrame
- file_exists()       : 检查文件是否存在（用于幂等写入）
"""

import io
import logging
from datetime import date

import pandas as pd
from google.cloud import storage

from ingestion.utils.config import config

logger = logging.getLogger(__name__)


class GCSClient:
    def __init__(self):
        # 使用 GCP VM 的 Service Account（VM 上无需额外鉴权）
        self.client = storage.Client(project=config.GCP_PROJECT_ID)
        self.bucket = self.client.bucket(config.GCS_BUCKET)

    def upload_dataframe(
        self,
        df: pd.DataFrame,
        layer: str,  # "bronze" / "silver" / "gold"
        dataset: str,  # e.g. "stock_bars"
        partition_date: date,
        filename: str = "data.parquet",
    ) -> str:
        """
        上传 DataFrame 到 GCS，按日期分区。

        路径格式：
          bronze/stock_bars/date=2024-01-15/data.parquet
        """
        gcs_path = f"{layer}/{dataset}/date={partition_date.isoformat()}/{filename}"
        blob = self.bucket.blob(gcs_path)

        # DataFrame → Parquet bytes（内存中转换，不落本地磁盘）
        buffer = io.BytesIO()
        df.to_parquet(buffer, index=False, engine="pyarrow")
        buffer.seek(0)

        blob.upload_from_file(buffer, content_type="application/octet-stream")
        logger.info(f"Uploaded {len(df)} rows → gs://{config.GCS_BUCKET}/{gcs_path}")
        return f"gs://{config.GCS_BUCKET}/{gcs_path}"

    def file_exists(self, gcs_path: str) -> bool:
        """幂等写入前先检查文件是否存在。"""
        blob = self.bucket.blob(gcs_path)
        return blob.exists()

    def download_dataframe(self, gcs_path: str) -> pd.DataFrame:
        """从 GCS 下载 Parquet → DataFrame。"""
        blob = self.bucket.blob(gcs_path)
        buffer = io.BytesIO(blob.download_as_bytes())
        return pd.read_parquet(buffer, engine="pyarrow")
