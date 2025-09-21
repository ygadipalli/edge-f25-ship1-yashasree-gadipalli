"""Stats helpers."""
from __future__ import annotations
from typing import Iterable
import numpy as np

def mean_length(items: Iterable[str]) -> float:
    """Return the mean character length of strings in `items`.
    Use NumPy arrays; return 0.0 for empty iterables.
    """
    items_list = list(items)
    if not items_list:
        return 0.0
    lengths = np.array([len(item) for item in items_list])
    return float(np.mean(lengths))
