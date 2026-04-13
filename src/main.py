from src.views.main_window import main_app
import sys
from PySide6.QtWidgets import QApplication

class main:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)

        self.window = main_app()
        self.window.show()

    def start(self) -> None:
        sys.exit(self.app.exec())

    def set_config(self, dict_config: dict) -> None:
        self.window.set_paths(dict_config)