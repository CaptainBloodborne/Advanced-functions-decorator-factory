#!/usr/bin/env python
from typing import Callable


def apply(func: Callable):
    """
    Create a decorators factory (decorator itself).
    The factory accepts a function (lambda) as an input and returns a decorator
    that will return the result of the function as the first argument,
    the result of the decorated function is passed.
    The function which the factory accepts (in
    the example below it is a `lambda`)
    can take one positional parameter only.

    Parameters
    ----------
    func : Callable
        function that takes as parameter decorated function

    Returns
    -------
    decorator : Callable
         actual decorator for wrapped function
    Examples
    --------

    @apply(lambda user_id: user_id + 1)
    def return_user_id():
        return 42

    return_user_id()
    43

    raise NotImplementedError('Implement me!')
    """
    def decorator(wrapped_func: Callable):
        def wrapper(*args, **kwargs):
            return func(
                wrapped_func(*args, **kwargs)
            )
        return wrapper
    return decorator


@apply(lambda user_id: user_id + 1)
def return_user_id():
    return 42
