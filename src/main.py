from src.views import start
import sys
from PySide6.QtWidgets import QApplication

class main:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)

        self.window = start()
        self.window.show()

    def start(self) -> None:
        sys.exit(self.app.exec())

    def set_config(self, dict_config: dict) -> None:
        self.window.set_paths(dict_config)