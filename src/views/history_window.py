from src.views.ui.history import Ui_Dialog

from src.utils.edit_data import edit_data

import darkdetect

from PySide6.QtWidgets import QApplication, QDialog, QTableWidget, QTableWidgetItem
from PySide6.QtCore import QTimer, Signal
from PySide6.QtWidgets import QHeaderView

class history_app(QDialog):

    """
    
    """

    amount: dict

    def __init__(self) -> None:
        super(history_app, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.set_default_table()

        self.ui.btn_copy.clicked.connect(self.copy)

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
        
        self.setWindowTitle(name_app)
        self.ui.lbl_name.setText(title)

        self.ui.table.setHorizontalHeaderItem(0, QTableWidgetItem(date_table))
        self.ui.table.setHorizontalHeaderItem(1, QTableWidgetItem(password_table))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem(result_table))
        self.ui.table.setHorizontalHeaderItem(3, QTableWidgetItem(entropy_table))

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

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                self.ui.table.setItem(row, col, QTableWidgetItem(str(value)))

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
        #QTimer.singleShot(1000, lambda: self.ui.btn_copy.setStyleSheet(self.style_normal))