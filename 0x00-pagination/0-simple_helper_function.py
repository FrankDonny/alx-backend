#!/usr/bin/env python3
"""a helper function module"""


def index_range(page: int, page_size: int) -> tuple:
    """a helper function"""
    start: int = (page - 1) * page_size
    return (start, start + page_size)
