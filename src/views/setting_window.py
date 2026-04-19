# PasswordAnalyzer - анализатор надёжности паролей
# Copyright (c) 2026 skilizz
# Released under the MIT License
# https://opensource.org/licenses/MIT

from src.views.ui import Ui_SettingsDialog

from src.utils import edit_data

import darkdetect
from pathlib import Path
import yaml

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QTimer, Signal

class setting_app(QDialog):

    save_setting = Signal()

    language_dict = dict()

    def __init__(self) -> None:
        super(setting_app, self).__init__()
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)

        self.ui.btn_confirm.clicked.connect(self.confirm_setting)

        self.ui.cb_system.clicked.connect(lambda function: self.toggle_setting(system=True, dark=False, light=False))
        self.ui.cb_dark.clicked.connect(lambda function: self.toggle_setting(system=False, dark=True, light=False))
        self.ui.cb_light.clicked.connect(lambda function: self.toggle_setting(system=False, dark=False, light=True))

    def set_language(self) -> None:
        edit = edit_data(self.paths)
        lang_data = edit.get_lang()
        
        data = lang_data["setting"]

        name = data["name"]
        title = data["title"]
        title_theme = data["title-theme"]

        theme = data["theme"]
        light = theme["light"]
        dark = theme["dark"]
        system = theme["system"]

        title_history = data["title-history"]
        title_lang = data["title-language"]

        waiting_message = data["waiting-message"]
        self.save = data["button-save"]
        self.successful_save = data["successful-save"]

        self.setWindowTitle(name)
        self.ui.lbl_name.setText(title)
        self.ui.lbl_theme.setText(title_theme)

        self.ui.lbl_light.setText(light)
        self.ui.lbl_dark.setText(dark)
        self.ui.lbl_system.setText(system)

        self.ui.lbl_password.setText(title_history)
        self.ui.lbl_lang.setText(title_lang)

        self.ui.comboBox.setPlaceholderText(waiting_message)
        self.ui.btn_confirm.setText(self.save)


    
    def confirm_setting(self) -> None:
        system = self.ui.cb_system.isChecked()
        light = self.ui.cb_light.isChecked()
        dark = self.ui.cb_dark.isChecked()

        language_in_box = self.ui.comboBox.currentText()
        language = self.language_dict[language_in_box]
        
        count_history = int(self.ui.sb_amount_history.text())
        
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

        self.edit_btn(state=True)

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
            self.save_setting.emit()

            style = "background-color: #32CD32;"
            self.ui.btn_confirm.setText(f"{self.successful_save}")
            self.ui.btn_confirm.setStyleSheet(style)

            QTimer.singleShot(1000, lambda: self.ui.btn_confirm.setText(self.save))
            QTimer.singleShot(1000, lambda: self.ui.btn_confirm.setStyleSheet(self.style_normal))

        self.theme()
        self.set_default_setting()
    
    def edit_data_file(self, count: int | None = None, language: str | None = None, theme: str | None = None) -> None:
        edit = edit_data(dict_path=self.paths)

        edit_args = edit.edit_config

        if not count is None:
            edit_args(name="history-amount", arg=str(count))


        if not language is None:
            try:
                path = self.paths["language"] + f"/{language}.yaml"                       
                with open(path, "r") as file:
                    pass
                edit_args(name="language", arg=language)
                self.set_language()
            except:
                lang = (edit.get_lang())["meta"]["language"]

                self.ui.comboBox.setCurrentText(lang)
        else: 
            lang = edit.get_config("language")

            self.ui.comboBox.setCurrentText(lang)                       

        if not theme is None:
            edit_args(name="theme", arg=theme)
    
    def set_paths(self, paths: dict | None = None) -> None:
        if paths is None:
            return
        
        self.paths = paths

        self.set_language()

    def set_default_setting(self) -> None:
        edit = edit_data(dict_path=self.paths)

        language = edit.get_config(arg="language")
        count = int(edit.get_config(arg="history-amount"))
        theme = edit.get_config(arg="theme")

        lang_list = self.get_lang()

        language = (edit.get_lang())["meta"]["language"]

        self.ui.comboBox.clear()

        for lang in lang_list:
            self.ui.comboBox.addItem(lang)

        self.ui.comboBox.setCurrentText(language)
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
        }
        
        QComboBox {
            background-color: #ffffff;
            color: #000000;
            border: 1px solid #d0d0d0;
            border-radius: 4px;
            padding: 5px;
        }

        QComboBox:hover {
            background-color: #f0f0f0;
        }

        QComboBox::drop-down {
            border: none;
        }

        QComboBox QAbstractItemView {
            background-color: #ffffff;
            color: #000000;
            selection-background-color: #1976d2;
            selection-color: #ffffff;
        }

        QSpinBox {
            background-color: #ffffff;
            color: #000000;
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
        }
        
        QComboBox {
            background-color: #2d2d2d;
            color: #ffffff;
            border: 1px solid #3c3c3c;
            border-radius: 4px;
            padding: 5px;
        }

        QComboBox:hover {
            background-color: #3c3c3c;
        }

        QComboBox::drop-down {
            border: none;
        }

        QComboBox QAbstractItemView {
            background-color: #2d2d2d;
            color: #ffffff;
            selection-background-color: #094771;
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
    
    def get_lang(self) -> list:
        path = Path(self.paths["language"])

        files = path.iterdir()

        name_list = list()
        result = list()

        for file in files:
            if file.suffix == ".yaml":
                name_list.append(f"{file.stem}")

        path_to_lang = self.paths["language"]

        for name_file in name_list:
            __path = path_to_lang + f"/{name_file}.yaml"
            with open(__path, "r", encoding="utf-8") as file:
                data_lang = yaml.safe_load(file)

            name = data_lang["meta"]["language"]
            code = data_lang["meta"]["code"]
            #if not name in result:
            result.append(f"{name}")
            self.language_dict[f"{name}"] = name_file
            #else:
                #result.append(f"{name} ({code})")

        return result