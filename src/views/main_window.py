from src.views.main import Ui_MainWindow
from src.views.setting import Ui_Dialog

from src.utils.edit_data import edit_data
from src.models.checked import Check

import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog
from PySide6.QtCore import QTimer

class main_app(QMainWindow):
    
    """
    
    """

    true_text = "✅"
    false_text = "❌"
    none_text = "🌫️"

    password_hide: bool

    def __init__(self) -> None:
        super(main_app, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.password_hide = True

        self.set_default_text()
        self.hide_password(change=False)

        self.ui.btn_password.clicked.connect(lambda function: self.hide_password(change=True))
        self.ui.le_password.textChanged.connect(self.start_program)
        self.ui.btn_copy.clicked.connect()
    

    def set_default_text(self) -> None:
        self.result = "Результат: "
        self.true_text = "✅"
        self.false_text = "❌"
        self.none_text = "🌫️"
        self.result_text = self.none_text

        self.main_text = "💪 Надёжность:"
        self.text = f""" {self.result_text} Длина: 12 символов\n{self.result_text} Заглавные буквы: A-Z\n{self.result_text} Строчные буквы: a-z\n{self.result_text} Цифры: 0-9\n{self.result_text} Спецсимволы: !@#$%\n{self.result_text} Энтропия: 0 бит """
        self.text_2 = "Схожесть с популярными паролями: \nСтатус:"
        
        self.ui.lbl_result.setText(self.result)
        self.ui.lbl_full_result.setText(self.text)
        self.ui.lbl_full_result_2.setText(self.text_2)
        self.ui.lbl_full_result_3.setText(self.main_text)
        self.ui.pb_bar.setValue(0)

    def hide_password(self, change: bool = False ) -> None:
        if change: self.password_hide = not self.password_hide

        if not self.password_hide:
            self.ui.le_password.setEchoMode(QLineEdit.EchoMode.Normal)

        else:
            self.ui.le_password.setEchoMode(QLineEdit.EchoMode.Password)

    def start_program(self):
        check = Check()

        password = self.ui.le_password.text()

        if password in ["", " ", None]:
            self.set_default_text()
            return None
        
        first_check = check.first_check(password=password)

        message = first_check["message"]
        print(message)
        main_text = f"symbol1 Длина: len символов\nsymbol2 Заглавные буквы: A-Z\nsymbol3 Строчные буквы: a-z\nsymbol4 Цифры: 0-9\nsymbol5 Спецсимволы: !@#$%\nsymbol6 Энтропия: entropy бит"

        len_password = str(len(password))

        main_text = main_text.replace("entropy", f"{message["entropy"]["numbers"]}").replace("len", f"{len_password}")

        if bool(message['len-8']):
            main_text = main_text.replace("symbol1", f"{self.true_text}")
        else:
            main_text = main_text.replace("symbol1", f"{self.false_text}")

        if bool(message["A-Z"]):
            main_text = main_text.replace("symbol2", f"{self.true_text}")
        else:
            main_text = main_text.replace("symbol2", f"{self.false_text}")
        
        if bool(message["a-z"]):
            main_text = main_text.replace("symbol3", f"{self.true_text}")
        else:
            main_text = main_text.replace("symbol3", f"{self.false_text}")

        if bool(message["!@$"]):
            main_text = main_text.replace("symbol5", f"{self.true_text}")
        else:
            main_text = main_text.replace("symbol5", f"{self.false_text}")
        
        if bool(message["0-9"]):
            main_text = main_text.replace("symbol4", f"{self.true_text}")
        else:
            main_text = main_text.replace("symbol4", f"{self.false_text}")

        if bool(message["entropy"]["result"]):
            main_text = main_text.replace("symbol6", f"{self.true_text}")
        else:
            main_text = main_text.replace("symbol6", f"{self.false_text}")

        self.ui.lbl_full_result.setText(main_text)

    




class setting_app(QDialog):
    
    """
    
    """

    def __init__(self) -> None:
        super(setting_app, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btn_confirm.clicked.connect(self.confirm_setting)

        self.ui.cb_system.clicked.connect(lambda function: self.toggle_setting(system=True, dark=False, light=False))
        self.ui.cb_dark.clicked.connect(lambda function: self.toggle_setting(system=False, dark=True, light=False))
        self.ui.cb_light.clicked.connect(lambda function: self.toggle_setting(system=False, dark=False, light=True))

    
    def confirm_setting(self) -> None:
        system = self.ui.cb_system.isChecked()
        light = self.ui.cb_light.isChecked()
        dark = self.ui.cb_dark.isChecked()

        language = self.ui.le_language.text()

        count_history = int(self.ui.sb_amount_history.text())

        if language in [None, "", " "]:
            language = None
        
        if system:
            theme = "system"
        elif light:
            theme = "light"
        elif dark:
            theme = "dark"
        else:
            print("????")
            theme = None

        self.edit_data_file(theme=theme, language=language, count=int(count_history))


        self.edit_btn(state=True, style_dark=True)

    def toggle_setting(self, system: bool = False, dark: bool = False, light: bool = False) -> None:
        if system:
            self.ui.cb_system.setChecked(True)
            self.ui.cb_dark.setChecked(False)
            self.ui.cb_light.setChecked(False)

        if light:
            self.ui.cb_system.setChecked(False)
            self.ui.cb_dark.setChecked(False)
            self.ui.cb_light.setChecked(True)

        if dark:
            self.ui.cb_system.setChecked(False)
            self.ui.cb_dark.setChecked(True)
            self.ui.cb_light.setChecked(False)

    
    def edit_btn(self, state: bool = False, style_dark: bool = True) -> None:
        if state:
            text = "Настройки применены!"
            text_btn = self.ui.btn_confirm.text()

            style = "background-color: #44944A;"
            self.ui.btn_confirm.setText(text)
            self.ui.btn_confirm.setStyleSheet(style)


            css_style_dark = "background-color: #1e1e1e;"

            css_style_light = """"""

            if style_dark:
                style = css_style_dark

            else:
                style = css_style_light

            QTimer.singleShot(1000, lambda: self.ui.btn_confirm.setText(text_btn))
            QTimer.singleShot(1000, lambda: self.ui.btn_confirm.setStyleSheet(style))
    
    def edit_data_file(self, count: int | None = None, language: str | None = None, theme: str | None = None) -> None:
        edit = edit_data(dict_path=self.paths)

        edit_args = edit.edit_config

        if not count is None:
            edit_args(name="history-amount", arg=str(count))

        if not language is None:
            edit_args(name="language", arg=language)

        if not theme is None:
            edit_args(name="theme", arg=theme)
    
    def set_paths(self, paths: dict | None = None) -> None:
        if paths is None:
            return
        
        self.paths = paths

    def set_default_setting(self) -> None:
        edit = edit_data(dict_path=self.paths)

        language = edit.get_config(arg="language")
        count = int(edit.get_config(arg="history-amount"))
        theme = edit.get_config(arg="theme")

        self.ui.le_language.setText(language)
        self.ui.sb_amount_history.setValue(count)

        match theme:
            case "system":
                self.ui.cb_system.setChecked(True)
                self.ui.cb_dark.setChecked(False)
                self.ui.cb_light.setChecked(False)

            case "light":
                self.ui.cb_system.setChecked(False)
                self.ui.cb_dark.setChecked(False)
                self.ui.cb_light.setChecked(True)

            case "dark":
                self.ui.cb_system.setChecked(False)
                self.ui.cb_dark.setChecked(True)
                self.ui.cb_light.setChecked(False)




"""
def main() -> None:
    app = QApplication(sys.argv)

    window = main_app()
    window.show()

    sys.exit(app.exec())"""

class setting:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)

        self.window = setting_app()
        self.window.show()


    def start(self) -> None:
        self.window.set_default_setting()
        sys.exit(self.app.exec())

    def set_config(self, dict_config: dict) -> None:
        self.window.set_paths(dict_config)

class main:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)

        self.window = main_app()
        self.window.show()

    def start(self) -> None:
        sys.exit(self.app.exec())