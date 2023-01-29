"""Simple test for version."""
from __future__ import annotations

import kilosort


def test_version():
    """Test version is sensible."""
    assert len(kilosort.__version__.split(".")) == 3
