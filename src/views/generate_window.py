# PasswordAnalyzer - анализатор надёжности паролей
# Copyright (c) 2026 skilizz
# Released under the MIT License
# https://opensource.org/licenses/MIT

from src.views.ui import Ui_GenerateWindow

from src.utils import edit_data
from src.models import Generate

import darkdetect

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, Signal

from src.views.setting_window import setting_app
from src.views.history_window import history_app


class generate_app(QMainWindow):

    closed = Signal()
    save = Signal()

    def __init__(self, parent=None) -> None:
        super(generate_app, self).__init__(parent)
        self.ui = Ui_GenerateWindow()
        self.ui.setupUi(self)

        self.ui.btn_copy.clicked.connect(self.copy)
        self.ui.btn_setting.clicked.connect(self.open_setting)
        
        self.ui.sld_lenght.valueChanged.connect(self.edit_text)

        self.ui.btn_generate.clicked.connect(self.generate)
        self.ui.btn_main.clicked.connect(self.close)
        self.ui.btn_history.clicked.connect(self.open_history)
        

    def set_language(self) -> None:
        edit = edit_data(self.paths)
        lang_data = edit.get_lang()
        
        data = lang_data["generate"]
        self.name = data["name"]
        self.title = data["title"]
        self.button = data["button"]



        self.setWindowTitle(self.name)
        self.ui.lbl_name_app.setText(self.title)

        data_text = data["text-result-full"]

        self.len_password = data_text["len"]
        self.text_upper = data_text["upper"]
        self.text_lower = data_text["lower"]
        self.text_custom = data_text["custom"]
        self.text_number = data_text["number"]
        self.text_special = data_text["special"]

        self.error_message = data_text["error"]

        self.text_length = self.len_password.replace("<len>", "16")
        
        self.ui.btn_copy.setText(self.button["copy"])
        self.ui.btn_setting.setText(self.button["setting"])
        self.ui.btn_main.setText(self.button["main-app"])
        self.ui.btn_history.setText(self.button["history"])
        self.ui.btn_generate.setText(self.button["generate"])

        self.ui.password.setText("")
        self.ui.lbl_text_lenght.setText(self.text_length)
        self.ui.lbl_text_upper.setText(self.text_upper)
        self.ui.lbl_text_lower.setText(self.text_lower)
        self.ui.lbl_text_russian.setText(self.text_custom)
        self.ui.lbl_text_number.setText(self.text_number)
        self.ui.lbl_text_special.setText(self.text_special)


    def set_default(self) -> None:
        self.password_dafault = ""
        self.length = 16

        self.ui.password.setText(self.password_dafault)
        self.ui.sld_lenght.setValue(self.length)
        self.ui.lbl_text_lenght.setText(self.text_length)
        self.ui.lbl_text_upper.setText(self.text_upper)
        self.ui.lbl_text_lower.setText(self.text_lower)
        self.ui.lbl_text_russian.setText(self.text_custom)
        self.ui.lbl_text_number.setText(self.text_number)
        self.ui.lbl_text_special.setText(self.text_special)

    
    def edit_text(self) -> None:
        length = int(self.ui.sld_lenght.value())

        if length < 10:
            length = f"{length}  "
        
        text = self.len_password.replace("<len>", f"{length}")

        self.ui.lbl_text_lenght.setText(text)

    
    def generate(self) -> None:
        length = int(self.ui.sld_lenght.value())
        bool_upper = self.ui.cb_upper.isChecked()
        bool_lower = self.ui.cb_lower.isChecked()
        bool_russian = self.ui.cb_russian.isChecked()
        bool_number = self.ui.cb_number.isChecked()
        bool_special = self.ui.cb_special.isChecked()\
        
        module = Generate()

        if not (bool_upper or bool_lower or bool_special or bool_number): 
            self.ui.password.setText(self.error_message)
            return None

        module.set_setting(length=length, upper_bool=bool_upper, lower_bool=bool_lower, russian_letters=bool_russian, special_chars_bool=bool_special, numbers_bool=bool_number)
        
        try:
            new_password = module.generate_password()
        except Exception as e:
            new_password = f"{self.error_message}"

        self.ui.password.setText(new_password)



    def set_paths(self, paths: dict | None = None) -> None:
        if paths is None:
            return
        
        self.paths = paths

        self.set_language()

        self.theme()


    def copy(self) -> None:

        if self.ui.password.text() in ["", "Невозможно сгенировать пароль.", "❌ Невозможно сгенировать пароль.", self.error_message, None]: return None
        style = "background-color: #32CD32;"

        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.password.text())
        
        self.ui.btn_copy.setText(self.button["successful-copy"])
        self.ui.btn_copy.setStyleSheet(style)
        QTimer.singleShot(1000, lambda: self.ui.btn_copy.setText(self.button["copy"]))
        QTimer.singleShot(1000, lambda: self.ui.btn_copy.setStyleSheet(self.style_normal))

    def open_setting(self) -> None:
        setting = setting_app()
        setting.set_paths(paths=self.paths)
        setting.set_default_setting()
        setting.theme()

        setting.save_setting.connect(self.theme)
        setting.save_setting.connect(self.save.emit)
        setting.save_setting.connect(self.set_language)

        setting.finished.connect(lambda: self.theme())
        setting.finished.connect(lambda: self.save.emit())
        setting.finished.connect(lambda: self.set_language())
        setting.exec()

        self.theme()

    def open_history(self) -> None:
        history = history_app()

        history.set_paths(paths=self.paths)

        history.exec()

    def theme(self) -> None:
        self.css_theme_dark = """QMainWindow {
                background-color: #1e1e1e;
            }

            QLineEdit {
                background-color: #2d2d2d;
                color: #ffffff;
                border: 1px solid #3c3c3c;
                border-radius: 4px;
                padding: 5px;
            }

            QLineEdit:focus {
                border: 2px solid #094771;
            }

            QPushButton {
                background-color: #2d2d2d;
                color: #ffffff;
                border: 1px solid #3c3c3c;
                border-radius: 4px;
                padding: 8px 16px;
            }

            QPushButton:hover {
                background-color: #3c3c3c;
            }

            QPushButton:pressed {
                background-color: #1e1e1e;
            }

            QPushButton:checked {
                background-color: #094771;
                color: #ffffff;
                border: none;
            }

            QProgressBar {
                border: 1px solid #3c3c3c;
                border-radius: 4px;
                background-color: #2d2d2d;
                color: #ffffff;
                text-align: center;
            }

            QProgressBar::chunk {
                background-color: #4caf50;
                border-radius: 3px;
            }"""

        self.css_theme_light = """QWidget {
                color: #000000;
            }

            QMainWindow {
                background-color: #f5f5f5;
            }

            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 1px solid #d0d0d0;
                border-radius: 4px;
                padding: 5px;
            }

            QLineEdit:focus {
                border: 2px solid #1976d2;
            }

            QPushButton {
                background-color: #ffffff;
                color: #000000; 
                border: 1px solid #d0d0d0;
                border-radius: 4px;
                padding: 8px 16px;
            }

            QPushButton:hover {
                background-color: #f0f0f0;
            }

            QPushButton:pressed {
                background-color: #e0e0e0;
            }

            QPushButton:checked {
                background-color: #1976d2;
                color: #ffffff; 
                border: none;
            }

            QProgressBar {
                border: 1px solid #d0d0d0;
                border-radius: 4px;
                background-color: #ffffff;
                color: #000000; 
                text-align: center;
            }

            QProgressBar::chunk {
                background-color: #4caf50;
                border-radius: 3px;
            }"""
        
        self.style_normal = "background-color: #2d2d2d;"

        edit = edit_data(self.paths)

        theme = edit.get_config("theme")

        match theme:
            case "dark":
                self.setStyleSheet(self.css_theme_dark)
                self.style_normal = "background-color: #2d2d2d;"
            
            case "light":
                self.setStyleSheet(self.css_theme_light)
                self.style_normal = "background-color: #ffffff;"

            case "system": 
                if darkdetect.isDark():
                    self.setStyleSheet(self.css_theme_dark)
                    self.style_normal = "background-color: #2d2d2d;"
                else:
                    self.setStyleSheet(self.css_theme_light)
                    self.style_normal = "background-color: #ffffff;"

            case _:
                self.setStyleSheet(self.css_theme_dark)
                self.style_normal = "background-color: #2d2d2d;"

        self.ui.btn_copy.setStyleSheet(self.style_normal)
        return None
    
    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
