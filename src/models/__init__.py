# __init__.py 
# src\models\__init__.py

"""Основные функции для программы"""

from .config import config
from .checked import Check
from .generate import generate_password as Generate

__version__ = "1.0.0"
__author__ = "skilizz"

__all__ = [
    "config",
    "Check",
    "Generate"
]