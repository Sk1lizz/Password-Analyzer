from src.views.ui.main import Ui_MainWindow

from src.utils.edit_data import edit_data
from src.models.checked import Check

import sys
import darkdetect

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import QTimer

from src.views.setting_window import setting_app
from src.views.generate_window import generate_app


class main_app(QMainWindow):
    
    """
    
    """

    true_text = "✅"
    false_text = "❌"
    none_text = "🌫️"

    password_hide: bool

    generate = None
    status_result = -1
    entropy_result = 0

    def __init__(self) -> None:
        super(main_app, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.password_hide = True

        self.ui.btn_password.clicked.connect(lambda function: self.hide_password(change=True))
        self.ui.le_password.textChanged.connect(self.start_program)
        self.ui.btn_copy.clicked.connect(self.copy)

        self.ui.btn_setting.clicked.connect(self.open_setting)
        self.ui.btn_generate.clicked.connect(self.open_generate)

    def set_language(self) -> None:
        edit = edit_data(self.paths)
        lang_data = edit.get_lang()
        
        data = lang_data["app"]

        self.name_app = data["name"]
        self.title = data["title"]
        self.waiting_text = data["waiting-message"]
        self.result = data["result-text"]
        self.full_text = data["full-text"]

        data_text = data["text-result-full"]

        len_text = data_text["len"]
        self.suffix = data_text["len-suffix"]
        upper_text = data_text["upper"]
        lower_text = data_text["lower"]
        number_text = data_text["number"]
        special_text = data_text["special"]
        entropy_text = data_text["entropy"]

        liked = data_text["liked-password"]
        result_liked = data_text["result-liked"]
        self.if_liked = data_text["if-liked"]
        self.liked_status = data_text["result-liked-password"]

        self.power = data_text["power-password"]

        self.status_text = data["status-text"]
        self.status = data["status"]

        self.button = data["button-text"]


        self.text = f"""<symbol1> {len_text}\n<symbol2> {upper_text}\n<symbol3> {lower_text}\n<symbol4> {number_text}\n<symbol5> {special_text}\n<symbol6> {entropy_text}"""
        self.liked_text = f"""{liked}\n<symbol> {result_liked}"""

        self.setWindowTitle(self.name_app)
        self.ui.lbl_name_app.setText(self.title)
        self.ui.le_password.setPlaceholderText(self.waiting_text)
        
        self.ui.btn_copy.setText(self.button["copy"])
        self.ui.btn_setting.setText(self.button["setting"])
        self.ui.btn_history.setText(self.button["history"])
        
        if not self.password_hide:
            self.ui.le_password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.btn_password.setText(self.button["hide-password"])

        else:
            self.ui.le_password.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.btn_password.setText(self.button["show-password"])

        self.ui.btn_generate.setText(self.button["generate"])

        self.start_program()
    

    def set_default_text(self) -> None:
        text = self.text.replace("<len>", "0").replace("<suffix>", self.suffix[2]).replace("<entropy>", "0")
        list_symbol = ["<symbol1>", "<symbol2>", "<symbol3>", "<symbol4>", "<symbol5>", "<symbol6>"]
        for symbol in list_symbol:
            text = text.replace(symbol, self.none_text)

        text_2 = self.liked_text.replace("<symbol>", "").replace("<status>", "")

        style_status = f"""
            QProgressBar::chunk {{
                background-color: #FFFFFF;
            }}
        """

        self.ui.pb_bar.setStyleSheet(style_status)
        self.ui.pb_bar.setValue(0)
        
        self.ui.lbl_result.setText(self.result)
        self.ui.lbl_full_result_4.setText(self.full_text)
        self.ui.lbl_full_result.setText(text)
        self.ui.lbl_full_result_2.setText(text_2)
        self.ui.lbl_full_result_3.setText(self.power)
        
        self.ui.btn_copy.setText(self.button["copy"])
        self.ui.btn_setting.setText(self.button["setting"])
        self.ui.btn_history.setText(self.button["history"])
        
        if not self.password_hide:
            self.ui.le_password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.btn_password.setText(self.button["hide-password"])

        else:
            self.ui.le_password.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.btn_password.setText(self.button["show-password"])

        self.ui.btn_generate.setText(self.button["generate"])

    def hide_password(self, change: bool = False ) -> None:
        if change: self.password_hide = not self.password_hide

        if not self.password_hide:
            self.ui.le_password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.ui.btn_password.setText(self.button["hide-password"])

        else:
            self.ui.le_password.setEchoMode(QLineEdit.EchoMode.Password)
            self.ui.btn_password.setText(self.button["show-password"])

    def start_program(self) -> None:
        check = Check()

        password = self.ui.le_password.text()

        if password.replace(" ", "") in ["", " ", None]:
            self.set_default_text()
            return None
        
        first_check = check.first_check(password=password)

        message = first_check["message"]
        score_first = int(first_check["score"])

        main_text = self.text

        len_password = str(len(password))

        self.entropy_result = float(message["entropy"]["numbers"])

        main_text = main_text.replace("<entropy>", f"{message["entropy"]["numbers"]}").replace("<len>", f"{len_password}")

        if bool(message['len-8']):
            main_text = main_text.replace("<symbol1>", f"{self.true_text}")
        else:
            main_text = main_text.replace("<symbol1>", f"{self.false_text}")

        if bool(message["A-Z"]):
            main_text = main_text.replace("<symbol2>", f"{self.true_text}")
        else:
            main_text = main_text.replace("<symbol2>", f"{self.false_text}")
        
        if bool(message["a-z"]):
            main_text = main_text.replace("<symbol3>", f"{self.true_text}")
        else:
            main_text = main_text.replace("<symbol3>", f"{self.false_text}")

        if bool(message["!@$"]):
            main_text = main_text.replace("<symbol5>", f"{self.true_text}")
        else:
            main_text = main_text.replace("<symbol5>", f"{self.false_text}")
        
        if bool(message["0-9"]):
            main_text = main_text.replace("<symbol4>", f"{self.true_text}")
        else:
            main_text = main_text.replace("<symbol4>", f"{self.false_text}")

        if bool(message["entropy"]["result"]):
            main_text = main_text.replace("<symbol6>", f"{self.true_text}")
        else:
            main_text = main_text.replace("<symbol6>", f"{self.false_text}")

        length = len(password)

        if length % 10 == 1 and length % 100 != 11 :
            suffix = self.suffix[0]
        elif 2 <= length % 10 <= 4 and (length % 100 < 10 or length % 100 >= 20):
            suffix = self.suffix[1]
        else:
            suffix = self.suffix[2]

        main_text = main_text.replace("<suffix>", f"{suffix}")

        self.ui.lbl_full_result.setText(main_text)

        edit = edit_data(self.paths)

        common_level = edit.get_config("common-level")

        if not common_level in ["1", "2", "3"]:
            common_level = "1"

        common_file = edit.get_common_file(int(common_level))

        second_check = check.second_check(password=password, common_file=common_file)

        score_second = int(second_check["score"])

        message = second_check["message"]

        text = self.liked_text

        if bool(message["clear"]):
            text = text.replace("<symbol>", f"{self.true_text}").replace("<status>", f"{self.liked_status[0]}")
        
        elif bool(message["1in1"]):
            text = text.replace("<symbol>", f"{self.false_text}").replace("<status>", f"{self.liked_status[2]}")
        
        else:
            password_liked = message["like"]

            text = text.replace("<symbol>", f"{self.false_text}").replace("<status>", f"{self.liked_status[1]}")
            text += f"\n{self.if_liked} {password_liked}"

        self.ui.lbl_full_result_2.setText(text)

        score = int(score_first) + int(score_second)

        percent = score

        if score <= 10:
            status_text = self.status_text[0]
            status = self.status[0]
            self.status_result = 0
            color = "#FF0000"

        elif score <= 20:
            status_text = self.status_text[1]
            status = self.status[1]
            self.status_result = 1
            color = "#FF3333"
        
        elif score <= 30:
            status_text = self.status_text[2]
            status = self.status[2]
            self.status_result = 2
            color = "#FF8000"
        
        elif score <= 40:
            status_text = self.status_text[3]
            status = self.status[3]
            self.status_result = 3
            color = "#FFFF00"
        
        elif score <= 50:
            status_text = self.status_text[4]
            status = self.status[4]
            self.status_result = 4
            color = "#FFFF66"
        
        elif score <= 75:
            status_text = self.status_text[5]
            status = self.status[5]
            self.status_result = 5
            color = "#00FF80"
        
        elif score <= 95:
            status_text = self.status_text[6]
            status = self.status[6]
            self.status_result = 6
            color = "#80FF00"
        
        elif score == 100:
            status_text = self.status_text[7]
            status = self.status[7]
            self.status_result = 7
            color = "#00FF00"
        
        else: 
            status_text = self.status_text[-1]
            status = self.status[-1]
            self.status_result = -1
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

        text = self.power

        text += status

        self.ui.lbl_full_result_3.setText(text)


    def set_paths(self, paths: dict | None = None) -> None:
        if paths is None:
            return
        
        self.paths = paths

        self.set_language()
        self.theme()

    
    def copy(self) -> None:

        if ((self.ui.le_password.text()).replace(" ", "")) in ["", " ", None]: return None
        style = "background-color: #32CD32;"

        clipboard = QApplication.clipboard()
        clipboard.setText(self.ui.le_password.text())
        
        self.ui.btn_copy.setText(self.button["successful-copy"])
        self.ui.btn_copy.setStyleSheet(style)
        QTimer.singleShot(1000, lambda: self.ui.btn_copy.setText(self.button["copy"]))
        QTimer.singleShot(1000, lambda: self.ui.btn_copy.setStyleSheet(self.style_normal))

        edit = edit_data(self.paths)

        password = self.ui.le_password.text()

        edit.add_history(message=password, status=self.status_result, entropy=self.entropy_result)

    def open_generate(self) -> None:
        generate = generate_app(self)
        generate.set_paths(paths=self.paths)
        generate.theme()

        self.generate = generate

        generate.closed.connect(self.theme)
        generate.save.connect(self.theme)

        generate.closed.connect(self.set_language)
        generate.save.connect(self.set_language)

        generate.show()


    def open_setting(self) -> None:
        if self.generate is None:
            setting = setting_app()
            setting.set_paths(paths=self.paths)
            setting.set_default_setting()
            setting.theme()

            setting.save_setting.connect(self.theme)
            setting.save_setting.connect(self.set_language)

            setting.finished.connect(self.theme)
            setting.finished.connect(self.set_language)

            setting.exec()

            self.theme()

        else:
            self.generate.open_setting()
        

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

        self.start_program()
        return None


class main:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)

        self.window = main_app()
        self.window.show()

    def start(self) -> None:
        sys.exit(self.app.exec())

    def set_config(self, dict_config: dict) -> None:
        self.window.set_paths(dict_config)
    