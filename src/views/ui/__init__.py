# __init__.py 
# src\views\ui\__init__.py

# PasswordAnalyzer - анализатор надёжности паролей
# Copyright (c) 2026 skilizz
# Released under the MIT License
# https://opensource.org/licenses/MIT


"""Все ui классы и config_rc файлы"""

from .setting import Ui_Dialog as Ui_SettingsDialog
from .history import Ui_Dialog as Ui_HistoryDialog
from .main import Ui_MainWindow as Ui_MainWindow
from .generate import Ui_MainWindow as Ui_GenerateWindow

__version__ = "1.0.0"
__author__ = "skilizz"
__license__ = "MIT"

__all__ = [
    "Ui_MainWindow",
    "Ui_GenerateWindow",
    "Ui_SettingsDialog",
    "Ui_HistoryDialog"
]