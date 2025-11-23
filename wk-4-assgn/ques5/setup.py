from setuptools import setup, Extension

module = Extension('arraylib', sources=['arraylib.c'])

setup(name='ArrayLib',
      version='1.0',
      description='Array management module',
      ext_modules=[module])