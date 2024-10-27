from setuptools import setup, find_packages

setup(
    name="cscript",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cscript=src.python.ide_setup:main',
        ],
    },
    package_data={
        'cscript': ['*.cript'],
    }
)