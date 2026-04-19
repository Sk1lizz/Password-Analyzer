from src.views.ui import Ui_HistoryDialog

from src.utils import edit_data

import darkdetect
import re

from PySide6.QtWidgets import QApplication, QDialog, QTableWidget, QTableWidgetItem
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QMessageBox

class history_app(QDialog):

    amount: dict

    bool_entropy = True
    bool_power = True
    bool_password = True

    def __init__(self) -> None:
        super(history_app, self).__init__()
        self.ui = Ui_HistoryDialog()
        self.ui.setupUi(self)

        self.set_default_table()

        self.ui.btn_copy.clicked.connect(self.copy)
        self.ui.btn_clear.clicked.connect(self.clear)

        self.ui.table.horizontalHeader().sectionClicked.connect(self.on_header_clicked)

    def set_language(self) -> None:
        edit = edit_data(self.paths)
        lang_data = edit.get_lang()

        data = lang_data["history"]

        name_app = data["name"]
        title = data["title"]

        table = data["table"]
        date_table = table["date"]
        password_table = table["password"]
        result_table = table["result-password"]
        entropy_table = table["entropy"]

        self.result = data["name-result"]
        self.result_text = data["result"]
        self.text_bit = data["bit"]

        self.button = data["button"]

        self.message_box = data["message-box"]
        
        self.setWindowTitle(name_app)
        self.ui.lbl_name.setText(title)

        self.ui.table.setHorizontalHeaderItem(0, QTableWidgetItem(date_table))
        self.ui.table.setHorizontalHeaderItem(1, QTableWidgetItem(password_table))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem(result_table))
        self.ui.table.setHorizontalHeaderItem(3, QTableWidgetItem(entropy_table))

        self.ui.btn_copy.setText(self.button["copy"])
        self.ui.btn_clear.setText(self.button["clear"])

        self.amount = {
            "strong": 0,
            "medium": 0,
            "weak": 0,
            "bad": 0
        }

        self.start_program()



    def set_paths(self, paths: dict | None = None) -> None:
        if paths is None:
            return
        
        self.paths = paths

        self.set_language()

        self.theme()


    def set_default_table(self) -> None:
        table = self.ui.table

        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        table.setSelectionBehavior(QTableWidget.SelectRows)

    def start_program(self) -> None:
        edit = edit_data(self.paths)
        amount = int(edit.get_config(arg="history-amount"))

        history = edit.get_history(amount_history=amount)
        

        if len(history) == 0 or history == [""]: return None

        if "" in history: 
            history.remove("")

        dict_item = dict()
        amount_history = 0
        
        for history_password in history:
            list_history = str(history_password).split(" | ")
            dict_item[amount_history] = [f"{list_history[0]}", f"{list_history[1]}", \
                                        f"{self.sorting_level(int(list_history[2]))}", \
                                        f"{self.text_bit.replace("<len>", list_history[3])}"]

            amount_history += 1

        text = str(self.result_text).replace("<len_strong>", f"{self.amount["strong"]}").replace("<len_medium>", f"{self.amount["medium"]}")\
            .replace("<len_weak>", f"{self.amount["weak"]}").replace("<len_bad>", f"{self.amount["bad"]}")
        
        len_total = int(self.amount["strong"]) + int(self.amount["medium"]) + int(self.amount["weak"]) + int(self.amount["bad"])
        text = text.replace("<len_total>", f"{len_total}")
        self.ui.lbl_result.setText(text)

        self.add_string(tuple(dict_item.values()))



    def sorting_level(self, level: int | None = None) -> str | None:
        if level is None: return None

        result = ""

        if level == -1:
            pass

        elif level <= 1:
            result = self.result["bad"]
            self.amount["bad"] = int(self.amount["bad"]) + 1
        
        elif level <= 3:
            result = self.result["weak"]
            self.amount["weak"] = int(self.amount["weak"]) + 1
        
        elif level <= 5:
            result = self.result["medium"]
            self.amount["medium"] = int(self.amount["medium"]) + 1
        
        elif level <= 7:
            result = self.result["strong"]
            self.amount["strong"] = int(self.amount["strong"]) + 1
        
        return result
    

    def add_string(self, data: tuple) -> None:
        self.ui.table.setRowCount(len(data))   

        dict_value = {
            self.result["bad"]: 0,
            self.result["weak"]: 1,
            self.result["medium"]: 2,
            self.result["strong"]: 3
        }

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

                if col == 2:
                    try:
                        number = int(dict_value[value])
                    except:
                        number = 0
                    item.setData(Qt.UserRole, int(number))

                if col == 3:
                    if isinstance(value, (float, int)):
                        number = value
                    else:
                        parts = str(value).split()
                        try:
                            number = float(parts[0])
                        except (ValueError, IndexError):
                            number = 0 

                    item.setData(Qt.UserRole, number)

                self.ui.table.setItem(row, col, item)

        self.ui.table.setSortingEnabled(False)

    def on_header_clicked(self, amount) -> None:
        table = self.ui.table
        count_row = table.rowCount()

        list_row = list()

        sorted_list_row = list()
        
        for row in range(count_row):
            list_col = []
            for col in range(4):
                item = table.item(row, col)

                list_col.append(item.text())
            
            list_row.append(list_col)

        dict_sort = dict()
        sort_list = list()
        sort_list_key = list()

        count = 0

        if amount == 0:
            for password in list_row:
                dict_sort[count] = password[0]
                count += 1

            for i in dict_sort.values():
                sort_list.append(i)
            
            new_sort_list = sorted(sort_list, reverse=self.bool_password)

            self.bool_password = not self.bool_password

            for i in new_sort_list:
                for y in dict_sort.keys():
                    if dict_sort[y] == i:
                        sort_list_key.append(y)
                        dict_sort[y] = -1
                        break
            
            for i in sort_list_key:
                sorted_list_row.append(list_row[i])

            self.add_string(tuple(sorted_list_row))

        if amount == 1:
            for password in list_row:
                dict_sort[count] = len(password[1])
                count += 1

            for i in dict_sort.values():
                sort_list.append(i)
            
            new_sort_list = sorted(sort_list, reverse=self.bool_password)

            self.bool_password = not self.bool_password

            for i in new_sort_list:
                for y in dict_sort.keys():
                    if dict_sort[y] == i:
                        sort_list_key.append(y)
                        dict_sort[y] = -1
                        break
            
            for i in sort_list_key:
                sorted_list_row.append(list_row[i])

            self.add_string(tuple(sorted_list_row))


        if amount == 2:
            dict_value = {
                self.result["bad"]: 0,
                self.result["weak"]: 1,
                self.result["medium"]: 2,
                self.result["strong"]: 3
            }

            for power in list_row:
                text = power[2]
                try:
                    text = dict_value[text]
                except:
                    text = -1
                dict_sort[count] = text
                count += 1
            
            for number in dict_sort.values():
                sort_list.append(int(number))
            
            new_sort_list = sorted(sort_list, reverse=self.bool_power)

            self.bool_power = not self.bool_power

            for i in new_sort_list:
                for y in dict_sort.keys():
                    if dict_sort[y] == i:
                        sort_list_key.append(y)
                        dict_sort[y] = -1
                        break

            for i in sort_list_key:
                sorted_list_row.append(list_row[i])

            self.add_string(tuple(sorted_list_row))

        if amount == 3:
            for entropy in list_row:
                text = entropy[3].replace(f"{self.text_bit.replace("<len>", "")}", "")
                dict_sort[count] = text
                count += 1
            
            for float_number in dict_sort.values():
                sort_list.append(float(float_number))

            new_sort_list = sorted(sort_list, reverse=self.bool_entropy)

            self.bool_entropy = not self.bool_entropy

            for i in new_sort_list:
                for y in dict_sort.keys():
                    if dict_sort[y] == str(i):
                        sort_list_key.append(y)
                        dict_sort[y] = -1
                        break

            for i in sort_list_key:
                sorted_list_row.append(list_row[i])

            self.add_string(tuple(sorted_list_row))



        
    def copy(self) -> None:
        selected = self.ui.table.selectionModel().selectedRows()
        if not selected: return
        else: row = selected[0].row()

        text = self.ui.table.item(row, 1).text()
        style = "background-color: #32CD32;"

        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        
        self.ui.btn_copy.setText(self.button["successful-copy"])
        self.ui.btn_copy.setStyleSheet(style)
        QTimer.singleShot(1000, lambda: self.ui.btn_copy.setText(self.button["copy"]))
        QTimer.singleShot(1000, lambda: self.ui.btn_copy.setStyleSheet(self.style_normal))

    def clear(self) -> None:
        state = False
        reply = QMessageBox(self)

        reply.setWindowTitle(self.message_box["title"])
        reply.setText(self.message_box["text"])

        button_text = self.message_box["button"]

        yes_btn = reply.addButton(button_text["yes_btn"], QMessageBox.YesRole)
        no_btn = reply.addButton(button_text["no_btn"], QMessageBox.NoRole)

        reply.exec()

        if reply.clickedButton() == yes_btn:
            self.ui.table.setRowCount(0)

            try:
                with open(self.paths["history"], "w") as file:
                    file.write("")
            except:
                pass

        else:
            return None
        

    def theme(self) -> None:
        self.ui.btn_clear.setObjectName("dangerButton")

        light = """QDialog {
            background-color: #f5f5f5;
        }

        QLabel {
            color: #000000;
            background-color: transparent;
            font-size: 12px;
        }

        QTableWidget {
            background-color: #ffffff;
            alternate-background-color: #f9f9f9;
            gridline-color: #e0e0e0;
            border: 1px solid #d0d0d0;
            border-radius: 8px;
        }

        QTableWidget::item {
            padding: 8px;
            color: #000000;
        }

        QTableWidget::item:selected {
            background-color: #1976d2;
            color: #ffffff;
        }

        QHeaderView::section {
            background-color: #f0f0f0;
            color: #000000;
            padding: 8px;
            border: 1px solid #d0d0d0;
            font-weight: bold;
        }

        QTableCornerButton::section {
            background-color: #f0f0f0;
            border: 1px solid #d0d0d0;
        }

        QHeaderView::section:horizontal {
            background-color: #f0f0f0;
            color: #000000;
        }

        QHeaderView::section:vertical {
            background-color: #f0f0f0;
            color: #000000;
        }

        QHeaderView::down-arrow {
            image: none;
        }

        QHeaderView::up-arrow {
            image: none;
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
        
        QPushButton#dangerButton {
            color: #f44336;
            border-color: #f44336;
        }

        QPushButton#dangerButton:hover {
            background-color: #f44336;
            color: #ffffff;
        }"""

        dark = """QDialog {
            background-color: #1e1e1e;
        }

        QLabel {
            color: #ffffff;
            background-color: transparent;
            font-size: 12px;
        }

        QTableWidget {
            background-color: #2d2d2d;
            alternate-background-color: #252525;
            gridline-color: #3c3c3c;
            border: 1px solid #3c3c3c;
            border-radius: 8px;
        }

        QTableWidget::item {
            padding: 8px;
            color: #ffffff;
        }

        QTableWidget::item:selected {
            background-color: #094771;
            color: #ffffff;
        }

        QHeaderView::section {
            background-color: #252525;
            color: #ffffff;
            padding: 8px;
            border: 1px solid #3c3c3c;
            font-weight: bold;
        }

        QTableCornerButton::section {
            background-color: #252525;
            border: 1px solid #3c3c3c;
        }

        QHeaderView::section:horizontal {
            background-color: #252525;
            color: #ffffff;
        }

        QHeaderView::section:vertical {
            background-color: #252525;
            color: #ffffff;
        }

        QHeaderView::down-arrow {
            image: none;
        }

        QHeaderView::up-arrow {
            image: none;
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

        QPushButton#dangerButton {
            color: #f44336;
            border-color: #f44336;
        }

        QPushButton#dangerButton:hover {
            background-color: #f44336;
            color: #ffffff;
        }"""

        self.style_normal = "background-color: #2d2d2d;"

        edit = edit_data(self.paths)

        theme = edit.get_config("theme")

        match theme:
            case "dark":
                self.setStyleSheet(dark)
                self.style_normal = "background-color: #2d2d2d;"
            
            case "light":
                self.setStyleSheet(light)
                self.style_normal = "background-color: #ffffff;"

            case "system": 
                if darkdetect.isDark():
                    self.setStyleSheet(dark)
                    self.style_normal = "background-color: #2d2d2d;"
                else:
                    self.setStyleSheet(light)
                    self.style_normal = "background-color: #ffffff;"

            case _:
                self.setStyleSheet(dark)
                self.style_normal = "background-color: #2d2d2d;"