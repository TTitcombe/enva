import os


def get_env_with_fallback(primary_variable: str, secondary_variable: str):
    """
    Retrieve an environment variable, from a priority list of variables.

    If the primary variable is not set, return the secondary variable.

    Returns
    -------
    T or None
        None if none of the provided environment variable names are set.
        Otherwise, the value assigned to the given environment variables
        in the prioritised order.
    """
    if (primary_value := os.getenv(primary_variable)) is not None:
        return primary_value
    else:
        return os.getenv(secondary_variable)


def get_env_int(
    variable: str, default_int: int | None = None, raise_typeerror: bool = False
) -> None | int:
    """
    Get an environment variable and convert to an integer.

    Optionally, a default integer may be supplied, which is returned
    if the environment variable is not set.
    If the environment variable is set, but not to an integer,
    None is returned.

    Parameters
    ----------
    variable : str
        The name of the environment variable to retrieve
    default_int : int. Optional
        An optional integer value to return if the environment variable
        is not set.

    Returns
    -------
    int or None
        The environment variable as an integer,
        or None if it is not set or not convertable to an int
    """
    return _get_env_type_wrapper(variable, default_int, int, raise_typeerror)


def get_env_float(
    variable: str, default_float: float | None = None, raise_typeerror: bool = False
) -> None | float:
    return _get_env_type_wrapper(variable, default_float, float, raise_typeerror)


def get_env_bool(
    variable: str, default_bool: bool | None = None, raise_typeerror: bool = False
) -> None | bool:
    """
    Get an environment variable and convert to an boolean.

    Optionally, a default boolean may be supplied, which is returned
    if the environment variable is not set.
    If the environment variable is set, but not to an boolean,
    None is returned.

    Parameters
    ----------
    variable : str
        The name of the environment variable to retrieve
    default_bool : bool. Optional
        An optional boolean value to return if the environment variable
        is not set.

    Returns
    -------
    bool or None
        The environment variable as a boolean,
        or None if it is not set or not convertable to a bool
    """

    def _bool_conversion_func(value):
        if isinstance(value, bool):
            return value

        if value.lower() in ("true", "1"):
            return True
        elif value.lower() in ("false", "0"):
            return False
        else:
            raise ValueError(f"{value} is not a bool-like string")

    return _get_env_type_wrapper(
        variable, default_bool, _bool_conversion_func, raise_typeerror
    )


def _get_env_type_wrapper(
    variable: str, default_value, conversion_func, raise_typeerror: bool
):
    """
    Wrapper for converting an environment variable to a particular type.
    """
    retrieved_value = os.getenv(variable, default_value)

    try:
        return conversion_func(retrieved_value)
    except (TypeError, ValueError, AttributeError):
        if raise_typeerror:
            raise TypeError(
                f"{variable} variable is not a valid type. Value: {retrieved_value}"
            )

        return None
