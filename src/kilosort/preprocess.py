"""pyKilosrt Pre-processing."""
from __future__ import annotations

from . import options


def preprocess_data_sub(opts: options.Options):
    """Pre-process data function."""
    pass


def get_whitening_matrix(opts: options.Options):
    """Output a rotation matrix (Nchan by Nchan).

    which whitens the zero-timelag covariance of the data.
    """
    pass
