from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension

ext_modules = [
    Pybind11Extension("concat", ["concat.cpp"]),
]

setup(
    name="concat",
    ext_modules=ext_modules,
)