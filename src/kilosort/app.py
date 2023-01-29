"""Main entrypoint."""
from __future__ import annotations

from .preprocess import preprocess_data_sub


def run():
    """Run KiloSort."""
    preprocess_data_sub()
    pass
