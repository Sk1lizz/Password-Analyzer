from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGridLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 700)
        Dialog.setMinimumSize(QSize(600, 700))
        icon = QIcon()
        icon.addFile(u"resources/icons/icon-white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lbl_name = QLabel(Dialog)
        self.lbl_name.setObjectName(u"lbl_name")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lbl_name.setFont(font)
        self.lbl_name.setStyleSheet(u"font-size: 20pt; ")
        self.lbl_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_name)

        self.verticalSpacer_2 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.table = QTableWidget(Dialog)
        if (self.table.columnCount() < 4):
            self.table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table.setObjectName(u"table")
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setTabKeyNavigation(False)
        self.table.setProperty(u"showDropIndicator", False)
        self.table.setDragDropOverwriteMode(False)
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        self.table.setRowCount(0)
        self.table.setColumnCount(4)
        self.table.setSupportedDragActions(Qt.DropAction.IgnoreAction)

        self.gridLayout.addWidget(self.table, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_16, 0, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_15, 0, 2, 1, 1)

        self.lbl_result = QLabel(Dialog)
        self.lbl_result.setObjectName(u"lbl_result")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lbl_result.setFont(font1)
        self.lbl_result.setCursor(QCursor(Qt.CursorShape.UpArrowCursor))
        self.lbl_result.setStyleSheet(u"font-size: 12pt;")
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.lbl_result, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_13, 0, 2, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_14, 0, 0, 1, 1)

        self.btn_clear = QPushButton(Dialog)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_3.addWidget(self.btn_clear, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_12, 1, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)

        self.btn_copy = QPushButton(Dialog)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_copy, 1, 1, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_12, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer_11 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_11)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"PasswordAnalyzer - history", None))
        self.lbl_name.setText(QCoreApplication.translate("Dialog", u"\U0001f4dc \U00000418\U00000441\U00000442\U0000043e\U00000440\U00000438\U0000044f \U0000043f\U00000440\U0000043e\U00000432\U00000435\U00000440\U0000043e\U0000043a \U0001f4dc", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\U0001f550 \U00000414\U00000430\U00000442\U00000430/\U00000412\U00000440\U00000435\U0000043c\U0000044f", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\U0001f512 \U0000041f\U00000430\U00000440\U0000043e\U0000043b\U0000044c", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\U0001f4aa \U0000041e\U00000446\U00000435\U0000043d\U0000043a\U00000430", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\U0001f4ca \U0000042d\U0000043d\U00000442\U00000440\U0000043e\U0000043f\U00000438\U0000044f", None));
        self.lbl_result.setText(QCoreApplication.translate("Dialog", u"\U0001f4ca \U00000412\U00000441\U00000435\U00000433\U0000043e: 0  \U00002502 \U0001f4aa 0  \U00002502 \U0001f538 0  \U00002502 \U000026a0\U0000fe0f 0 \U00002502 \U0001f4a9 0", None))
        self.btn_clear.setText(QCoreApplication.translate("Dialog", u"\U0001f5d1\U0000fe0f \U0000041e\U00000447\U00000438\U00000441\U00000442\U00000438\U00000442\U0000044c \U00000438\U00000441\U00000442\U0000043e\U00000440\U00000438\U0000044e", None))
        self.btn_copy.setText(QCoreApplication.translate("Dialog", u"\U0001f4cb \U0000041a\U0000043e\U0000043f\U00000438\U00000440\U0000043e\U00000432\U00000430\U00000442\U0000044c", None))
    # retranslateUi

