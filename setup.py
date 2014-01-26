from setuptools import setup, find_packages
from distutils.extension import Extension
from Cython.Build import cythonize

extension_defaults = {
    'extra_compile_args': [
        '-std=gnu++11',
        '-O3',
        '-Wall',
        '-Wextra',
        '-Wconversion',
        '-fno-strict-aliasing'
    ],
    'language': 'c++',
    'libraries': [
        'rocksdb',
        'snappy',
        'bz2',
        'z'
    ]
}

mod1 = Extension(
    'rocksdb._rocksdb',
    ['rocksdb/_rocksdb.pyx'],
    **extension_defaults
)

setup(
    name="pyrocksdb",
    install_requires=[
        'setuptools',
        'Cython>=0.20',
    ],
    package_dir={'rocksdb': 'rocksdb'},
    packages=find_packages('.'),
    ext_modules=cythonize([mod1]),
    test_suite='rocksdb.tests',
    include_package_data=True
)
