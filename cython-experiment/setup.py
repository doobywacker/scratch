import numpy
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("astarx.pyx", annotate=True),
    include_dirs=[numpy.get_include()],
)
