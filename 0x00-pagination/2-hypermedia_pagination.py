#!/usr/bin/env python3
""" A python module for class defination of Server"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    A function to calculate start and end indexes for a page
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Method to get pages"""

        assert isinstance(page, int) and isinstance(page_size, int)
        assert (page > 0) and (page_size > 0)
        indexes = index_range(page, page_size)
        start = indexes[0]
        end = indexes[1]
        # checking if the indexes are out of range
        if page > len(self.dataset()) - 1:
            return []
        else:
            return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ A method to return a detailed dictionary"""

        hyper = {}
        hyper["page_size"] = len(self.get_page(page, page_size))
        hyper["page"] = page
        hyper["data"] = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if page < total_pages:
            hyper["next_page"] = page + 1
        else:
            hyper["next_page"] = None
        if page == 1:
            hyper["prev_page"] = None
        else:
            hyper["prev_page"] = page - 1
        hyper["total_pages"] = total_pages

        return hyper