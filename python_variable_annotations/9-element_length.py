#!/usr/bin/env python3
"""
Task 9: Let's duck type an iterable object
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return list of tuples with element and its length."""
    return [(i, len(i)) for i in lst]
