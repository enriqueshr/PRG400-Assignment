from setuptools import setup, Extension

module = Extension('square', sources=['square.c'])

setup(
    name='SquareModule',
    version='1.0',
    description='A simple square function',
    ext_modules=[module],
)