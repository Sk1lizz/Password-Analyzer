# PasswordAnalyzer - анализатор надёжности паролей
# Copyright (c) 2026 skilizz
# Released under the MIT License
# https://opensource.org/licenses/MIT

import sys
from PySide6.QtWidgets import QApplication

from src.views import start
from src.utils import create_files
from src.models import config

class MainApp:
    
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = None
    
    def setup(self, paths: dict):
        self.window = start()  # создаём окно
        self.window.set_paths(paths)
        self.window.show()
    
    def run(self):
        return sys.exit(self.app.exec())


def main():
    cfg = config()
    path = cfg.get_config_path()
    
    createfiles = create_files(config_dict=path)
    createfiles.create_file()
    paths = createfiles.get_path()
    
    app = MainApp()
    app.setup(paths)
    app.run()