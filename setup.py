from setuptools import setup, find_packages

setup(
    name="cscript",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    package_data={
        'cscript': ['core/*.cpp', 'core/*.h'],
    },
    entry_points={
        'console_scripts': [
            'cscript=cscript.python.ide_setup:main',
        ],
    }
)