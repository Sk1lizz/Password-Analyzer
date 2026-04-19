# __init__.py 
# src\views\__init__.py

"""Корень проекта"""

from .main import main

from .utils import create_files
from .utils import edit_data

from .models import config


__version__ = "1.0.0"
__author__ = "skilizz"

__all__ = [
    "main",
    "create_files",
    "edit_data",
    "config"
]