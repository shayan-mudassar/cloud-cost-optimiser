from dataclasses import dataclass
import os

@dataclass
class Config:
    """Application configuration loaded from environment variables."""
    aws_key: str = os.getenv("AWS_KEY", "")
    azure_key: str = os.getenv("AZURE_KEY", "")
    gcp_key: str = os.getenv("GCP_KEY", "")
    budget_limit: float = float(os.getenv("BUDGET_LIMIT", "1000"))


config = Config()
