import re

from setuptools import setup


def get_version():
    result = re.search(
        r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', open("enva/__init__.py").read()
    )
    return result.group(1)


setup(
    version=get_version(),
)
