# setup.py
from setuptools import setup, find_packages, Extension

# Notera: Vi tar bort pybind11-importen här eftersom den inte finns än

setup(
    name="cscript",
    version="0.1.0",
    packages=find_packages(),
    setup_requires=[
        'pybind11>=2.6.0',
        'setuptools>=42.0.0',
        'wheel>=0.37.0'
    ],
    install_requires=[
        'pybind11>=2.6.0',
    ],
    package_data={
        'cscript': [
            'core/*.cpp',
            'core/*.h',
            'icons/*'
        ]
    },
    entry_points={
        'console_scripts': [
            'cscript=cscript.runner:main'
        ]
    }
)