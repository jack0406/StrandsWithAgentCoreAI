import logging
from typing import Optional


def configure_logging(level: int = logging.INFO, format: Optional[str] = None) -> None:
    """Configure basic logging for the package."""
    logging.basicConfig(level=level, format=format)
