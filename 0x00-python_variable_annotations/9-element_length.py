#!/usr/bin/env python3
""" This module contains a type-annotated function element_length """
from typing import Iterable, Sequence, List, Tuple

SeqTuple = Tuple[Sequence, int]


def element_length(lst: Iterable[Sequence]) -> List[SeqTuple]:
    """ returns a list of tuples """

    return [(i, len(i)) for i in lst]
