from src.views.main import Ui_MainWindow
from src.views.setting import Ui_Dialog

import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog
from PySide6.QtCore import QTimer

class main_app(QMainWindow):
    
    """
    
    """

    def __init__(self) -> None:
        super(main_app, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        


class setting_app(QDialog):
    
    """
    
    """

    def __init__(self) -> None:
        super(setting_app, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

def main() -> None:
    app = QApplication(sys.argv)

    window = main_app()
    window.show()

    sys.exit(app.exec())

def setting() -> None:
    app = QApplication(sys.argv)

    window = setting_app()
    window.show()

    sys.exit(app.exec())