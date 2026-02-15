#!/usr/bin/env python3
"""
Task 7: Complex types - string and int/float to tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with k and the square of v as float."""
    return (k, float(v * v))
