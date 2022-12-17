from typing import Callable

from enva.checkers import require_variable_as_type, require_variable_exists


def require_variable_exists_decorator(variable_name: str):
    def outer_func(func):
        def inner_func(*args, **kwargs):
            require_variable_exists(variable_name)
            return func(*args, **kwargs)

        return inner_func

    return outer_func


def require_variable_as_type_decorator(variable_name: str, type_conversion: Callable):
    def outer_func(func):
        def inner_func(*args, **kwargs):
            require_variable_as_type(variable_name, type_conversion)
            return func(*args, **kwargs)

        return inner_func

    return outer_func
