"""Configuration for jupyter-ml."""

from typing import Optional


class Config:
    """Runtime configuration."""

    kernel: str = "python3"
    timeout: Optional[int] = None
    allow_errors: bool = False
