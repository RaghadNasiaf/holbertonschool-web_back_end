#!/usr/bin/env python3
"""
Module for pagination helper function.
This module contains a function to calculate start and end indexes.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
