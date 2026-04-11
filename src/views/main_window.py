from src.views.main import Ui_MainWindow
from src.views.setting import Ui_Dialog
from src.views.generate import Ui_MainWindow as generate_Ui

from src.utils.edit_data import edit_data
from src.models.generate import generate_password
from src.models.checked import Check

import sys
import darkdetect

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QDialog
from PySide6.QtCore import QTimer, Signal


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

        
        self.hide_password(change=False)

        self.ui.btn_password.clicked.connect(lambda function: self.hide_password(change=True))
        self.ui.le_password.textChanged.connect(self.start_program)
        self.ui.btn_copy.clicked.connect(self.copy)

        self.ui.btn_setting.clicked.connect(self.open_setting)
        self.ui.btn_generate.clicked.connect(self.open_generate)
    

    def set_default_text(self) -> None:
        self.result = "Результат: "
        self.result_text = self.none_text

        self.main_text = "💪 Надёжность: "
        self.text = f"""{self.result_text} Длина: 0 символов\n{self.result_text} Заглавные буквы: A-Z\n{self.result_text} Строчные буквы: a-z\n{self.result_text} Цифры: 0-9\n{self.result_text} Спецсимволы: !@#$%\n{self.result_text} Энтропия: 0 бит """
        self.text_2 = "Схожесть с популярными паролями: \nСтатус: "

        style_status = f"""
            QProgressBar::chunk {{
                background-color: #FFFFFF;
            }}
        """

        self.ui.pb_bar.setStyleSheet(style_status)
        
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

    def start_program(self) -> None:
        check = Check()

        password = self.ui.le_password.text()

        if password.replace(" ", "") in ["", " ", None]:
            self.set_default_text()
            return None
        
        first_check = check.first_check(password=password)

        message = first_check["message"]
        score_first = int(first_check["score"])
        main_text = f"symbol1 Длина: len suffix\nsymbol2 Заглавные буквы: A-Z\nsymbol3 Строчные буквы: a-z\nsymbol4 Цифры: 0-9\nsymbol5 Спецсимволы: !@#$%\nsymbol6 Энтропия: entropy бит"

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

        length = len(password)

        if length % 10 == 1 and length % 100 != 11 :
            suffix = "символ"
        elif 2 <= length % 10 <= 4 and (length % 100 < 10 or length % 100 >= 20):
            suffix = "символа"
        else:
            suffix = "символов"

        main_text = main_text.replace("suffix", f"{suffix}")

        self.ui.lbl_full_result.setText(main_text)

        edit = edit_data(self.paths)

        common_level = edit.get_config("common-level")

        if not common_level in ["1", "2", "3"]:
            common_level = "1"

        common_file = edit.get_common_file(int(common_level))

        second_check = check.second_check(password=password, common_file=common_file)

        score_second = int(second_check["score"])

        message = second_check["message"]

        text = "Схожесть с популярными паролями: \n<symbol> Статус: <status>"

        if bool(message["clear"]):
            text = text.replace("<status>", "Отсутвует").replace("<symbol>", f"{self.true_text}")
        
        elif bool(message["1in1"]):
            text = text.replace("<symbol>", f"{self.false_text}").replace("<status>", "Точное совпадение")
        
        else:
            password_liked = message["like"]

            text = text.replace("<status>", f"Похож\nПароль похож на {password_liked}").replace("<symbol>", f"{self.false_text}")

        self.ui.lbl_full_result_2.setText(text)

        score = int(score_first) + int(score_second)

        percent = score

        if score <= 10:
            status_text = "Ужасный пароль"
            status = "УЖАСНО"
            color = "#FF0000"

        elif score <= 20:
            status_text = "Очень плохой пароль"
            status = "УЖАСНО"
            color = "#FF3333"
        
        elif score <= 30:
            status_text = "Плохой пароль"
            status = "ПЛОХО"
            color = "#FF8000"
        
        elif score <= 40:
            status_text = "Нормальный пароль"
            status = "НОРМАЛЬНО"
            color = "#FFFF00"
        
        elif score <= 50:
            status_text = "Хороший пароль"
            status = "ХОРОШИЙ"
            color = "#FFFF66"
        
        elif score <= 75:
            status_text = "Отличный пароль"
            status = "ОТЛИЧНО"
            color = "#00FF80"
        
        elif score <= 95:
            status_text = "Превосходный пароль"
            status = "ОТЛИЧНО"
            color = "#80FF00"
        
        elif score == 100:
            status_text = "Самый защищеный пароль"
            status = "ПРЕВОСХОДНО"
            color = "#00FF00"
        
        else: 
            status_text = "Ошибка"
            status = "ОШИБКА"
            color = "#FFFFFF"


        style_status = f"""
            QProgressBar::chunk {{
                background-color: {color};
            }}
        """

        self.ui.pb_bar.setStyleSheet(style_status)

        if percent >= 0:
            self.ui.pb_bar.setValue(percent)

            text = self.result + f"{score}%\n"

        else:
            self.ui.pb_bar.setValue(0)
            text = self.result + f"0%\n"

        text += f"{status_text}"

        self.ui.lbl_result.setText(text)

        text = self.main_text

        text += status

        self.ui.lbl_full_result_3.setText(text)


    def set_paths(self, paths: dict | None = None) -> None:
        if paths is None:
            return
        
        self.paths = paths

        self.theme()

    
    def copy(self) -> None:

        if ((self.ui.le_password.text()).replace(" ", "")) in ["", " ", None]: return None
        style = "background-color: #32CD32;"

        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.le_password.text())
        
        self.ui.btn_copy.setText("✅ Скопировано!")
        self.ui.btn_copy.setStyleSheet(style)
        QTimer.singleShot(1000, lambda: self.ui.btn_copy.setText("📋 Скопировать"))
        QTimer.singleShot(1000, lambda: self.ui.btn_copy.setStyleSheet(self.style_normal))

        edit = edit_data(self.paths)

        password = self.ui.le_password.text()

        edit.add_history(password)

    def open_generate(self) -> None:
        generate = generate_app(self)
        generate.set_paths(paths=self.paths)
        generate.theme()

        #self.hide()
        generate.show()
        
        #generate.destroyed.connect(self.show)

        generate.destroyed.connect(self.theme)


    def open_setting(self) -> None:
        setting = setting_app()
        setting.set_paths(paths=self.paths)
        setting.set_default_setting()
        setting.theme()

        setting.exec()

        self.theme()

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
                border: none;
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
            }

            QProgressBar {
                border: 1px solid #3c3c3c;
                border-radius: 4px;
                background-color: #2d2d2d;
                color: #ffffff;
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

            QLabel {
                color: #000000;
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
                self.none_text = "🌫️"
            
            case "light":
                self.setStyleSheet(self.css_theme_light)
                self.style_normal = "background-color: #ffffff;"
                self.none_text = "⬛"

            case "system": 
                if darkdetect.isDark():
                    self.setStyleSheet(self.css_theme_dark)
                    self.style_normal = "background-color: #2d2d2d;"
                    self.none_text = "🌫️"
                else:
                    self.setStyleSheet(self.css_theme_light)
                    self.style_normal = "background-color: #ffffff;"
                    self.none_text = "⬛"

            case _:
                self.setStyleSheet(self.css_theme_dark)
                self.style_normal = "background-color: #2d2d2d;"
                self.none_text = "🌫️"
        
        self.set_default_text()
        return None


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

        if language.replace(" ", "") in [None, "", " "]:
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

        self.theme()

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

    
    def edit_btn(self, state: bool = False, *kwars, **args) -> None:
        if state:
            text = "Настройки применены!"
            text_btn = self.ui.btn_confirm.text()

            style = "background-color: #32CD32;"
            self.ui.btn_confirm.setText(text)
            self.ui.btn_confirm.setStyleSheet(style)

            QTimer.singleShot(1000, lambda: self.ui.btn_confirm.setText(text_btn))
            QTimer.singleShot(1000, lambda: self.ui.btn_confirm.setStyleSheet(self.style_normal))
    
    def edit_data_file(self, count: int | None = None, language: str | None = None, theme: str | None = None) -> None:
        edit = edit_data(dict_path=self.paths)

        edit_args = edit.edit_config

        if not count is None:
            edit_args(name="history-amount", arg=str(count))

        if not language is None:
            edit_args(name="language", arg=language)
        else: 
            lang = edit.get_config("language")

            self.ui.le_language.setText(lang)

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


    def theme(self) -> None:
        css_theme_light = """QWidget {
            color: #000000;
        }

        QDialog {
            background-color: #f5f5f5;
            color: #000000;
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

        QCheckBox {
            color: #000000;
            spacing: 8px;
            font-size: 12px;
            padding: 4px 0px;
        }"""

        css_theme_dark = """QDialog {
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

        QCheckBox {
            spacing: 8px;
            font-size: 12px;
            padding: 4px 0px;
        }"""

        self.style_normal = "background-color: #2d2d2d;"

        edit = edit_data(self.paths)

        theme = edit.get_config("theme")

        match theme:
            case "dark":
                self.setStyleSheet(css_theme_dark)
                self.style_normal = "background-color: #2d2d2d;"
            
            case "light":
                self.setStyleSheet(css_theme_light)
                self.style_normal = "background-color: #ffffff;"

            case "system": 
                if darkdetect.isDark():
                    self.setStyleSheet(css_theme_dark)
                    self.style_normal = "background-color: #2d2d2d;"
                else:
                    self.setStyleSheet(css_theme_light)
                    self.style_normal = "background-color: #ffffff;"

            case _:
                self.setStyleSheet(css_theme_dark)
                self.style_normal = "background-color: #2d2d2d;"

            
        return None



class generate_app(QMainWindow):
    
    """
    
    """

    closed = Signal()

    def __init__(self, parent=None) -> None:
        super(generate_app, self).__init__(parent)
        self.ui = generate_Ui()
        self.ui.setupUi(self)

        self.set_default()

        self.ui.btn_copy.clicked.connect(self.copy)
        self.ui.btn_setting.clicked.connect(self.open_setting)
        
        self.ui.sld_lenght.valueChanged.connect(self.edit_text)

        self.ui.btn_generate.clicked.connect(self.generate)
        



    def set_default(self) -> None:
        self.setWindowTitle("PasswordAnalyzer - generate")
        self.password_dafault = ""
        self.length = 16
        self.text_length = "16 симв."

        self.text_upper = "Использовать заглавные буквы"
        self.text_lower = "Использовать прописные буквы"
        self.text_russian = "Использовать русские буквы"
        self.text_number = "Использовать числа"
        self.text_special = "Использовать спецсимволы"

        self.ui.password.setText(self.password_dafault)
        self.ui.sld_lenght.setValue(self.length)
        self.ui.lbl_text_lenght.setText(self.text_length)
        self.ui.lbl_text_upper.setText(self.text_upper)
        self.ui.lbl_text_lower.setText(self.text_lower)
        self.ui.lbl_text_russian.setText(self.text_russian)
        self.ui.lbl_text_number.setText(self.text_number)
        self.ui.lbl_text_special.setText(self.text_special)

    
    def edit_text(self) -> None:
        length = int(self.ui.sld_lenght.value())

        if length < 10:
            length = f"{length}  "
        
        text = f"{length} симв."

        self.ui.lbl_text_lenght.setText(text)

    
    def generate(self) -> None:
        length = int(self.ui.sld_lenght.value())
        bool_upper = self.ui.cb_upper.isChecked()
        bool_lower = self.ui.cb_lower.isChecked()
        bool_russian = self.ui.cb_russian.isChecked()
        bool_number = self.ui.cb_number.isChecked()
        bool_special = self.ui.cb_special.isChecked()\
        
        module = generate_password()

        module.set_setting(length=length, upper_bool=bool_upper, lower_bool=bool_lower, russian_letters=bool_russian, special_chars_bool=bool_special, numbers_bool=bool_number)

        new_password = module.generate_password()

        self.ui.password.setText(new_password)



    def set_paths(self, paths: dict | None = None) -> None:
        if paths is None:
            return
        
        self.paths = paths

        self.theme()


    def copy(self) -> None:

        if self.ui.password.text() in ["", " ", None]: return None
        style = "background-color: #32CD32;"

        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.password.text())
        
        self.ui.btn_copy.setText("✅ Скопировано!")
        self.ui.btn_copy.setStyleSheet(style)
        QTimer.singleShot(1000, lambda: self.ui.btn_copy.setText("📋 Скопировать"))
        QTimer.singleShot(1000, lambda: self.ui.btn_copy.setStyleSheet(self.style_normal))

    def open_setting(self) -> None:
        setting = setting_app()
        setting.set_paths(paths=self.paths)
        setting.set_default_setting()
        setting.theme()

        setting.exec()

        self.theme()

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
                border: none;
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
            }

            QProgressBar {
                border: 1px solid #3c3c3c;
                border-radius: 4px;
                background-color: #2d2d2d;
                color: #ffffff;
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

            QLabel {
                color: #000000;
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
        return None
    
    def closeEvent(self, event):
        if self.parent():
            self.parent().show()
        self.closed.emit()
        event.accept()



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

    def set_config(self, dict_config: dict) -> None:
        self.window.set_paths(dict_config)
    

class gen:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)

        self.window = generate_app()
        self.window.show()

    def start(self) -> None:
        sys.exit(self.app.exec())

    def set_config(self, dict_config: dict) -> None:
        self.window.set_paths(dict_config)