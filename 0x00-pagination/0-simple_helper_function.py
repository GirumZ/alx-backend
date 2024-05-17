#!/usr/bin/env python3
""" A python module for simple paginetion helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """
    A function to calculate start and end indexes for a page
    Args:
        page(int): the page number
        page_size(int): the number of items on a single page
    Returns(tuple):
        the start and end indexes
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
