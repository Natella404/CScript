from setuptools import setup, find_packages, Extension
import pybind11
import sys
import os

# Configure the C++ extension
ext_modules = [
    Extension(
        "cscript.core.generator",
        ["cscript/core/generator.cpp"],
        include_dirs=[
            pybind11.get_include(),
            pybind11.get_include(user=True)
        ],
        language='c++',
        extra_compile_args=['-std=c++17'],
    )
]

setup(
    name="cscript",
    version="0.1.0",
    packages=find_packages(),
    ext_modules=ext_modules,
    install_requires=[
        'pybind11>=2.6.0',
    ],
    setup_requires=['pybind11>=2.6.0'],
    package_data={
        'cscript': ['core/*.cpp', 'core/*.h']
    },
    entry_points={
        'console_scripts': [
            'cscript=cscript.runner:main'
        ]
    }
)
# setup.py
setup(
    # ... other setup configurations ...
    package_data={
        'cscript': [
            'core/*.cpp',
            'core/*.h',
            'icons/*'  # Include icons
        ]
    },
    data_files=[
        ('icons', ['cscript/icons/cscript.ico',
                  'cscript/icons/cscript.png'])
    ]
)

setup(
    # ... andra inställningar ...
    package_data={
        'cscript': [
            'core/*.cpp',
            'core/*.h',
            'icons/*'  # Detta inkluderar alla ikonfiler
        ]
    }
)