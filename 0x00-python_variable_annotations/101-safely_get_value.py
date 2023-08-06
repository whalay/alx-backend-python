#!/usr/bin/env python3
""" This module contains a type-annotated function safely_get_value """
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ returns a value safely """

    if key in dct:
        return dct[key]
    else:
        return default
