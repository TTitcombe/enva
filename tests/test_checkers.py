import os
from unittest import mock

import pytest

from enva.checkers import (check_variable_exists, require_variable_as_type,
                           require_variable_exists)


class TestRequireVariableExists:
    def test_require_variable_exists_raises_if_does_not_exist(self):
        with pytest.raises(RuntimeError):
            require_variable_exists("SOME_NONEXISTENT_VAR")

    @mock.patch.dict(os.environ, {"A_REAL_VAR": "somevalue"})
    def test_require_variable_exists_does_not_raise_if_exists(self):
        require_variable_exists("A_REAL_VAR")


class TestCheckVariableExists:
    @mock.patch.dict(os.environ, {"A_REAL_VAR": "somevalue"})
    def test_check_variable_exists_returns_True_if_exists(self):
        assert check_variable_exists("A_REAL_VAR") is True

    def test_check_variable_exists_returns_False_if_does_not_exist(self):
        assert check_variable_exists("INVALID_VAR") is False


class TestRequireVariableAsType:
    def test_require_variable_as_type_raises_if_does_not_exist(self):
        with pytest.raises(RuntimeError):
            require_variable_as_type("INVALID_VAR", int)

    @mock.patch.dict(os.environ, {"SOME_VAR": "10"})
    def test_require_variable_as_type_does_not_throw_if_can_convert_type(self):
        require_variable_as_type("SOME_VAR", int)
        require_variable_as_type("SOME_VAR", float)

    @mock.patch.dict(os.environ, {"SOME_VAR": "ten"})
    def test_require_variable_as_type_raises_if_cannot_convert_type(self):
        with pytest.raises(ValueError):
            require_variable_as_type("SOME_VAR", int)
