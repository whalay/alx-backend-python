#!/usr/bin/env python3
""" This module contains a type-annotated function sum_list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ sums a list and returns the result """

    return sum(input_list)
