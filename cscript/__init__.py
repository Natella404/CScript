"""
CScript - A modern programming language that generates optimized machine code.
"""

# Version and metadata
__version__ = "0.1.0"
__author__ = "Nathaniel"
__description__ = "CScript programming language"

from .runner import main

__all__ = ['main']

print(f"CScript v{__version__} initialized")