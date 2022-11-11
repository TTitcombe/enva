# Enva

Making working with environment variables in Python slightly better.

Ever needed to get an environment variable as an integer or a boolean?
Ever needed to assert that an environment variable is set?
Stop looking at the standard library. It can't help you.
Env var utils can.


Env var utils provides utility functionality for working with environment variables in Python.
There are two main features:

* Variable retrieval (as alternative types, e.g. int)
* Variable assertion (e.g. is the variable set)

# Sponsor

This project is sponsored by [Documatic](https://app.documatic.com),
the search engine for your codebase.

# Getting started

## Requirements

* Python 3.10 or greater
* That's it

Install enva from pypi with

```
pip install enva
```

## Updates

Please refer to the [changelog](./CHANGELOG.md)
for a full breakdown of recent updates.

# Examples

## Converting env vars

```python
import os
from enva.getters import get_env_int

os.environ["SOME_VAR"] = "10"

print(get_env_int("SOME_VAR"))  # 10 (as an int)
```

## Verifying env var types

```python
import os
from enva.checkers import require_variable_as_type

os.environ["SOME_VAR"] = "10"
os.environ["ANOTHER_VAR"] = "ten"

print(require_variable_as_type("SOME_VAR", float))  # No throw
print(require_variable_as_type("ANOTHER_VAR", float))  # Will raise
```

# Developers

## Code quality

* black formatting
* isort imports
* mypy compliance

## Testing

[Unit tests](./tests/)
are run with pytest.
Please ensure that new features
and bug fixes
have an appropriate test.
There is a github action
to ensure tests pass
with sufficient coverage.


# Contributing

All contributions are welcome!
Please see the
[contributing guide](./CONTRIBUTING.md)
to get started.

# License

GPL-3.
Please read [the license](./LICENSE)
for full terms. 
