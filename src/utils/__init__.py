# __init__.py
# src\utils\__init__.py

# PasswordAnalyzer - анализатор надёжности паролей
# Copyright (c) 2026 skilizz
# Released under the MIT License
# https://opensource.org/licenses/MIT


from .create_files import create_files
from .edit_data import edit_data

__version__ = "1.0.0"
__author__ = "skilizz"
__license__ = "MIT"

__all__ = [
    "create_files",
    "edit_data"
]