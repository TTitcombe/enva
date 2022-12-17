import os
from unittest import mock

import pytest

from enva.decorators import (
    require_variable_as_type_decorator,
    require_variable_exists_decorator,
)


class TestRequireVariableAsType:
    @mock.patch.dict(os.environ, {"SOME_VAR": "5"})
    def test_return_wrapped_func_return(self):
        @require_variable_as_type_decorator("SOME_VAR", int)
        def wrapped_func():
            return 10

        assert wrapped_func() == 10

    @mock.patch.dict(os.environ, {"SOME_VAR": "ten"})
    def test_return_wrapped_raises_if_cant_convert_variable(self):
        @require_variable_as_type_decorator("SOME_VAR", int)
        def wrapped_func():
            return 10

        with pytest.raises(ValueError):
            wrapped_func()

    @mock.patch.dict(os.environ, {"SOME_VAR": "5"})
    def test_return_wrapped_gets_passed_args(self):
        @require_variable_as_type_decorator("SOME_VAR", int)
        def wrapped_func(a, b):
            return a + b

        assert wrapped_func(1, 2) == 3

    @mock.patch.dict(os.environ, {"SOME_VAR": "5"})
    def test_return_wrapped_gets_passed_kwargs(self):
        @require_variable_as_type_decorator("SOME_VAR", int)
        def wrapped_func(a=15):
            return a

        assert wrapped_func(a=25) == 25


class TestRequireVariableExists:
    @mock.patch.dict(os.environ, {"SOME_VAR": "value"})
    def test_decorator_returns_wrapped_func_return(self):
        @require_variable_exists_decorator("SOME_VAR")
        def wrapped_func():
            return 5

        assert wrapped_func() == 5

    @mock.patch.dict(os.environ, {"ANOTHER_VAR": "value"})
    def test_decorator_raises_if_environment_variable_does_not_exist(self):
        @require_variable_exists_decorator("SOME_VAR")
        def wrapped_func():
            return 5

        with pytest.raises(RuntimeError):
            wrapped_func()

    @mock.patch.dict(os.environ, {"SOME_VAR": "value"})
    def test_decorator_passes_args_to_func(self):
        @require_variable_exists_decorator("SOME_VAR")
        def wrapped_func(a, b, c):
            return a + b + c

        assert wrapped_func(-1, 1, 10) == 10

    @mock.patch.dict(os.environ, {"SOME_VAR": "value"})
    def test_decorator_passes_kwargs_to_func(self):
        @require_variable_exists_decorator("SOME_VAR")
        def wrapped_func(a=5, b=10):
            return a + b

        assert wrapped_func(b=15, a=10) == 25

    @mock.patch.dict(os.environ, {"SOME_VAR": "value"})
    def test_decorator_passes_args_and_kwargs_to_func(self):
        @require_variable_exists_decorator("SOME_VAR")
        def wrapped_func(a, b, c=10):
            return a + b + c

        assert wrapped_func(-1, 1) == 10
