# PasswordAnalyzer - анализатор надёжности паролей
# Copyright (c) 2026 skilizz
# Released under the MIT License
# https://opensource.org/licenses/MIT

from src.views.ui import Ui_GenerateWindow

from src.utils import edit_data
from src.models import Generate

import darkdetect
import base64

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, Signal, QByteArray
from PySide6.QtGui import QKeySequence, QShortcut, QPixmap, QIcon

from src.views.setting_window import setting_app
from src.views.history_window import history_app


class generate_app(QMainWindow):

    closed = Signal()
    save = Signal()

    def __init__(self, parent=None) -> None:
        super(generate_app, self).__init__(parent)
        self.ui = Ui_GenerateWindow()
        self.ui.setupUi(self)

        self.set_shortcut()

        self.ui.password.setText("")

        self.ui.btn_copy.clicked.connect(self.copy)
        self.ui.btn_setting.clicked.connect(self.open_setting)
        
        self.ui.sld_lenght.valueChanged.connect(self.edit_text)

        self.ui.btn_generate.clicked.connect(self.generate)
        self.ui.btn_main.clicked.connect(self.close)
        self.ui.btn_history.clicked.connect(self.open_history)


    def set_shortcut(self) -> None:
        QShortcut(QKeySequence("Ctrl+C"), self).activated.connect(self.copy)

        QShortcut(QKeySequence("Ctrl+H"), self).activated.connect(self.open_history)

        QShortcut(QKeySequence("Ctrl+S"), self).activated.connect(self.open_setting)

        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(self.close)
        

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

        self.text_length = self.len_password.replace("<len>", f"{self.ui.sld_lenght.value()}")
        
        self.ui.btn_copy.setText(self.button["copy"])
        self.ui.btn_setting.setText(self.button["setting"])
        self.ui.btn_main.setText(self.button["main-app"])
        self.ui.btn_history.setText(self.button["history"])
        self.ui.btn_generate.setText(self.button["generate"])

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
        self.theme()
        self.save.emit()


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
        self.theme()
        self.save.emit()


        history = history_app()

        history.set_paths(paths=self.paths)

        self.theme()
        
        self.save.emit()

        history.exec()

        self.theme()
        
        self.save.emit()

    def theme(self) -> None:
        self.css_theme_dark = """
            QWidget {
                color: #ffffff;
            }

            QMainWindow {
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

            QCheckBox {
                color: #ffffff;
                spacing: 8px;
                font-size: 12px;
                padding: 4px 0px;
            }

            QCheckBox::indicator {
                border-radius: 4px;
                border: 1px solid #ffffff;
            }
            
            QCheckBox::indicator:checked {
                background-color: #9966CC;
                border-color: #ffffff;
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

            QCheckBox {
                color: #000000;
                spacing: 8px;
                font-size: 12px;
                padding: 4px 0px;
            }
            
            QCheckBox::indicator {
                border-radius: 4px;
                border: 1px solid #000000;
            }
            
            QCheckBox::indicator:checked {
                background-color: #9966CC;
                border-color: #000000;
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

        self.set_icon()

        self.ui.btn_copy.setStyleSheet(self.style_normal)
        return None
    
    def set_icon(self) -> None:
        if darkdetect.isLight():
            icon_base64 = "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAABXUlEQVR4AeyTsTIEQRCGh4hMSEZGRkYmwxPwBqSegEe4kDfgDYiEZGRkhDIlIuP7xvbV7FC1d1t1ibqr/rv7753tf6dnbjZN+DcV6Bzw/xzRIfv+qrAP72X1iGx89kenC2ofYGwrBWweDVZIZhqsEbU53NgiIeBYeD+bjV9y9uOeCNYISRE/pAsnLhYhEGNZsgjWQTQxh6YN3Yg4ZV0WCQF4ttfsU7pvoiHyB4g76cIe67QsUgv4oA92ipc+i/y9FlhsHsbBSmM0m5AYm/EGrr3hrsAz2AZRPyYfhIAEnlxkjIN1HI7G2q2ugM0UWmhqy8RWc3gKgYEEeEu8ii6GZlvF24iQ3L6iwtya5yaPm+fHRr+hgAtdZFTEndhUPFoENpwnhpnvQuLm+d/Zgg+bk7cE5IocmVQ4gNuQ0LLrFkvpruK/BHx+jlOoxCW1XhZn0OvlUV6aCnROaeIj+gYAAP//mYnelwAAAAZJREFUAwDP20IxigFiUgAAAABJRU5ErkJggg=="

        else:
            icon_base64 =  "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAABr0lEQVR4AexTO07DQBC1rRSJlNi4gy7poIMOunTACeAGoeUEcARKuAHcACpK6KCDzpTpLH+kpLC8vDfyWmsDcbCUJkq0T/PZmfd2xxvHWvFvI9A44DUcUZIkE0DVcNY4iz8KKiMiKepugfq6x96snlwmLgVAoHRDlmWjwWBgE0qpvSLfRc2/RUQAjZOCxCKp7/tfOnZd95O5IqZIfXy/xVdFvSUCCGQstm3vwLfCMNyHqDTSZw63OqBdEtfoFxEtIH39fn9Kp9PpvNES2set3nmTJuR5fso+QEQqAki2WmmaHutGCMwNP6oIoHCbm8aHtfRooig6xLVlbIV9Zi38EPWPcRwHGOcYN5Y8hC49z7sRAQYsRmFAqz8sx8HRMOc4zgutgTHI+fK2mMP3G9bJmRcBKjEA+EpmOMkQviycbLcgYjynKIFAj2LKWCklL4+HNfjKVyTPE01cXZwkICmBk30wCZC8BysLpD3sncDKy8OtRyA/MslZKDegQ6DYhr0A6usceyW53sSre9I+LchfaU1UBLgBojtA/sWGfeBeG/wQaEOyqGcjsGg6srfyEX0DAAD///zVChAAAAAGSURBVAMAURz2McPXH7wAAAAASUVORK5CYII="
        
        image_data = base64.b64decode(icon_base64)

        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(image_data))

        icon = QIcon(pixmap)

        self.setWindowIcon(icon)
    
    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
