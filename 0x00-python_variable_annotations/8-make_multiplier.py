#!/usr/bin/env python3
""" This module contains a type-annotated function make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier """

    def multiplier_function(x: float) -> float:
        """ multiplies by multiplier """

        return x * multiplier

    return multiplier_function
