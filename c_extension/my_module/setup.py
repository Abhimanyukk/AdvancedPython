from setuptools import setup, Extension

module = Extension('my_module', sources=['my_module.c'])

setup(
    name='my_module',
    version='1.0',
    description='A simple example module',
    ext_modules=[module]
)
