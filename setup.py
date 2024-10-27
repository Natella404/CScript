from setuptools import setup, find_packages, Extension
import pybind11

ext_modules = [
    Extension(
        "cscript.core.generator",
        ["cscript/core/generator.cpp"],
        include_dirs=[pybind11.get_include()],
        language='c++'
    )
]

setup(
    name="cscript",
    version="0.1.0",
    packages=find_packages(),
    ext_modules=ext_modules,
    install_requires=[
        'pybind11>=2.6.0',
        'setuptools>=42.0.0',
        'wheel>=0.37.0'
    ],
    setup_requires=[
        'pybind11>=2.6.0'
    ],
    package_data={
        'cscript': [
            'core/*.cpp',
            'core/*.h',
            'icons/*'
        ]
    }
)