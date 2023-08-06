#!/usr/bin/env python3
""" This module contains a type-annotated function safe_first_element """
from typing import Sequence, Any, Union


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ returns lst[0] is lst else none """

    if lst:
        return lst[0]
    else:
        return None
