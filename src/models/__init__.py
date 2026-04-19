# __init__.py 
# src\models\__init__.py

# PasswordAnalyzer - анализатор надёжности паролей
# Copyright (c) 2026 skilizz
# Released under the MIT License
# https://opensource.org/licenses/MIT


"""Основные функции для программы"""

from .config import config
from .checked import Check
from .generate import generate_password as Generate

__version__ = "1.0.0"
__author__ = "skilizz"
__license__ = "MIT"

__all__ = [
    "config",
    "Check",
    "Generate"
]