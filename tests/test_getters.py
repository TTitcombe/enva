import os
from unittest import mock

import pytest

from enva.getters import (get_env_bool, get_env_float, get_env_int,
                          get_env_with_fallback)


class TestGetEnvWithFallback:
    @mock.patch.dict(os.environ, {"TEST_ENV1": "value1", "TEST_ENV2": "value2"})
    def test_retrieves_primary_value_if_set(self):
        assert get_env_with_fallback("TEST_ENV1", "TEST_ENV2") == "value1"

    @mock.patch.dict(os.environ, {"TEST_ENV2": "value2"})
    def test_retrieves_secondary_value_if_primary_not_set(self):
        assert get_env_with_fallback("TEST_ENV1", "TEST_ENV2") == "value2"

    def test_returns_None_if_no_variables_Set(self):
        assert get_env_with_fallback("TEST_ENV1", "TEST_ENV2") is None


class TestGetEnvInt:
    @mock.patch.dict(os.environ, {"SOME_VAR": "10"})
    def test_get_env_int_returns_value_as_int_if_valid(self):
        assert get_env_int("SOME_VAR") == 10

    def test_get_env_int_returns_None_if_var_non_existent(self):
        assert get_env_int("SOME_VAR") is None

    @mock.patch.dict(os.environ, {"SOME_VAR": "10"})
    def test_get_env_int_returns_env_var_value_over_default(self):
        assert get_env_int("SOME_VAR", 12) == 10

    def test_get_env_int_returns_default_if_var_non_existent_and_default_provided(self):
        assert get_env_int("SOME_VAR", 12) == 12

    @mock.patch.dict(os.environ, {"SOME_VAR": "ten"})
    def test_get_env_int_raises_if_conversion_error_and_raise_flag_provided(self):
        with pytest.raises(TypeError):
            get_env_int("SOME_VAR", raise_typeerror=True)

    def test_get_env_int_raises_if_env_var_non_existent_and_raise_flag_provided(self):
        with pytest.raises(TypeError):
            get_env_int("SOME_VAR", raise_typeerror=True)

    def test_get_env_int_returns_default_even_if_raise_flag_provided(self):
        assert get_env_int("SOME_VAR", 15, raise_typeerror=True) == 15


class TestGetEnvFloat:
    @mock.patch.dict(os.environ, {"SOME_VAR": "10.8"})
    def test_get_env_float_returns_value_as_float_if_valid(self):
        assert get_env_float("SOME_VAR") == 10.8

    def test_get_env_float_returns_None_if_var_non_existent(self):
        assert get_env_float("SOME_VAR") is None

    @mock.patch.dict(os.environ, {"SOME_VAR": "10"})
    def test_get_env_float_returns_env_var_value_over_default(self):
        assert get_env_float("SOME_VAR", 12.2) == 10.0

    def test_get_env_float_returns_default_if_var_non_existent_and_default_provided(
        self,
    ):
        assert get_env_float("SOME_VAR", 12.5) == 12.5

    @mock.patch.dict(os.environ, {"SOME_VAR": "ten"})
    def test_get_env_float_raises_if_conversion_error_and_raise_flag_provided(self):
        with pytest.raises(TypeError):
            get_env_float("SOME_VAR", raise_typeerror=True)

    def test_get_env_float_raises_if_env_var_non_existent_and_raise_flag_provided(self):
        with pytest.raises(TypeError):
            get_env_float("SOME_VAR", raise_typeerror=True)

    def test_get_env_float_returns_default_even_if_raise_flag_provided(self):
        assert get_env_float("SOME_VAR", 15.5, raise_typeerror=True) == 15.5


class TestGetEnvBool:
    @mock.patch.dict(os.environ, {"SOME_VAR": "True"})
    def test_get_env_bool_returns_value_as_bool_if_valid(self):
        assert get_env_bool("SOME_VAR") is True

    @mock.patch.dict(os.environ, {"SOME_VAR": "1"})
    def test_get_env_bool_returns_1_as_True(self):
        assert get_env_bool("SOME_VAR") is True

    @mock.patch.dict(os.environ, {"SOME_VAR": "False"})
    def test_get_env_bool_returns_False_string_as_False(self):
        assert get_env_bool("SOME_VAR") is False

    @mock.patch.dict(os.environ, {"SOME_VAR": "0"})
    def test_get_env_bool_returns_0_as_False(self):
        assert get_env_bool("SOME_VAR") is False

    @mock.patch.dict(os.environ, {"SOME_VAR": "10"})
    def test_get_env_bool_returns_string_as_None(self):
        assert get_env_bool("SOME_VAR") is None

    def test_get_env_bool_returns_None_if_var_non_existent(self):
        assert get_env_bool("SOME_VAR") is None

    @mock.patch.dict(os.environ, {"SOME_VAR": "True"})
    def test_get_env_bool_returns_env_var_value_over_default(self):
        assert get_env_bool("SOME_VAR", False) is True

    def test_get_env_bool_returns_default_if_var_non_existent_and_default_provided(
        self,
    ):
        assert get_env_bool("SOME_VAR", False) == False

    @mock.patch.dict(os.environ, {"SOME_VAR": "ten"})
    def test_get_env_bool_raises_if_conversion_error_and_raise_flag_provided(self):
        with pytest.raises(TypeError):
            get_env_bool("SOME_VAR", raise_typeerror=True)

    def test_get_env_bool_raises_if_env_var_non_existent_and_raise_flag_provided(self):
        with pytest.raises(TypeError):
            get_env_bool("SOME_VAR", raise_typeerror=True)

    def test_get_env_bool_returns_default_even_if_raise_flag_provided(self):
        assert get_env_bool("SOME_VAR", False, raise_typeerror=True) == False
