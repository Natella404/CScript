from setuptools import setup, find_packages, Extension

setup(
    name="cscript",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pybind11>=2.6.0',
        'setuptools>=42.0.0',
        'wheel>=0.37.0'
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