#!/usr/bin/env python

from ..main import apply
from typing import Callable


def test_decorator_factory():
    arg_func: Callable = lambda x: x + 1
    test_func: Callable = lambda x, y: x + y
    params: tuple = (7, 3)
    result: int = 11
    decorated_func = apply(arg_func)(test_func)
    assert result == decorated_func(*params)
