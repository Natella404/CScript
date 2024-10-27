# cscript/__init__.py

"""
CScript - Ett modernt kodspråk som genererar optimerad maskinkod
"""

__version__ = "0.1.0"
__author__ = "Nathaniel"
__description__ = "CScript programming language"

# Importera viktiga funktioner som ska vara tillgängliga
from .runner import main

# Definiera vad som ska vara tillgängligt när någon importerar cscript
__all__ = ['main']