#!/usr/bin/env python3
""" Type-annotated suum_mixed_list function """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns the sum of a list as float"""

    return float(sum(mxd_lst))
