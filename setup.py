from setuptools import setup, find_packages, Extension
import pybind11
import sys
import platform
import os

def get_environment_config():
    compile_args = []
    link_args = []

    # Bas-inställningar för alla miljöer
    include_dirs = [
        pybind11.get_include(),
        pybind11.get_include(user=True)
    ]

    # Windows-specifika inställningar
    if platform.system() == "Windows":
        compile_args = ['/std:c++17']

    # Linux/Unix/MacOS inställningar
    else:
        compile_args = ['-std=c++17', '-fPIC']
        link_args = ['-fPIC']

    # Replit-specifika tillägg
    if os.getenv('REPL_ID') is not None:
        include_dirs.append('/nix/store/*/include')

    # VSCode-specifika tillägg
    if os.getenv('VSCODE_CLI') is not None:
        compile_args.append('-DVSCODE_ENV')

    return compile_args, link_args, include_dirs

# Hämta miljöspecifika inställningar
compile_args, link_args, include_dirs = get_environment_config()

# Definiera extensions
ext_modules = [
    Extension(
        "cscript.core.generator",
        ["cscript/core/generator.cpp"],
        include_dirs=include_dirs,
        language='c++',
        extra_compile_args=compile_args,
        extra_link_args=link_args
    ),
    Extension(
        "cscript.core.parser",
        ["cscript/core/parser.cpp"],
        include_dirs=include_dirs,
        language='c++',
        extra_compile_args=compile_args,
        extra_link_args=link_args
    ),
    Extension(
        "cscript.core.rules",
        ["cscript/core/rules.cpp"],
        include_dirs=include_dirs,
        language='c++',
        extra_compile_args=compile_args,
        extra_link_args=link_args
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
    },
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ]
)