#!/usr/bin/env python3
"""included hypermedia pagination to the module"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """a helper function"""
    start: int = (page - 1) * page_size
    return (start, start + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "./Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """initialize the instance"""
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
        """that takes two integer arguments page with default
        value 1 and page_size with default value 10"""
        assert isinstance(page, int) and page > 0, []
        assert isinstance(page_size, int) and page_size > 0, []
        res: tuple = index_range(page, page_size)
        dataset = self.dataset()
        if res[0] > len(dataset):
            return []
        return dataset[res[0]: res[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns the details of a page"""
        dataset = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset())/page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            "page_size": page_size,
            "page": page,
            "data": dataset,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
