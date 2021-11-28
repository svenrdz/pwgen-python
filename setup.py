from setuptools import setup

setup(
    name="pwgen-python",
    version="0.1.0",
    py_modules=["pwgen-python"],
    install_requires=["Click"],
    entry_points={"console_scripts": ["pwgen-python=pwgen_python:cli"]},
)
