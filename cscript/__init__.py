"""
CScript - Ett modernt kodspråk som genererar optimerad maskinkod.
"""

# Version och metadata
__version__ = "0.1.0"
__author__ = "Nathaniel"
__description__ = "CScript programming language"

# Importera main-funktionen från runner.py
from .runner import main

# Definiera vilka funktioner/klasser som ska vara tillgängliga när någon importerar cscript
__all__ = ['main']

# Om du vill kan du lägga till en välkomstmeddelande som visas när paketet importeras
print(f"CScript v{__version__} initialized")