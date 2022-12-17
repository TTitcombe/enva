import os
from typing import Callable


def require_variable_exists(variable: str) -> None:
    if os.getenv(variable) is None:
        raise RuntimeError(f"{variable} environment variable is not set")


def require_variable_as_type(variable: str, type_conversion: Callable) -> None:
    require_variable_exists(variable)
    type_conversion(os.getenv(variable))


def check_variable_exists(variable: str) -> bool:
    return os.getenv(variable) is not None
