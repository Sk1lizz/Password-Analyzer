# __init__.py 
# src\views\__init__.py

# PasswordAnalyzer - анализатор надёжности паролей
# Copyright (c) 2026 skilizz
# Released under the MIT License
# https://opensource.org/licenses/MIT


"""Классы с прописанной логикой ui"""

from .main_window import main_app as start

__version__ = "1.0.0"
__author__ = "skilizz"
__license__ = "MIT"

__all__ = [
    "start"
]