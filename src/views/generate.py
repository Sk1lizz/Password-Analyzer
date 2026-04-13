from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 750)
        MainWindow.setMinimumSize(QSize(500, 750))
        icon = QIcon()
        icon.addFile(u"resources\\icons\\icon-white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lbl_name_app = QLabel(self.centralwidget)
        self.lbl_name_app.setObjectName(u"lbl_name_app")
        self.lbl_name_app.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_name_app)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.password = QLabel(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.password)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.btn_generate = QPushButton(self.centralwidget)
        self.btn_generate.setObjectName(u"btn_generate")
        self.btn_generate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btn_generate)

        self.horizontalSpacer_13 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_7 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.cb_upper = QCheckBox(self.centralwidget)
        self.cb_upper.setObjectName(u"cb_upper")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_upper.sizePolicy().hasHeightForWidth())
        self.cb_upper.setSizePolicy(sizePolicy)
        self.cb_upper.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_upper.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.cb_upper)

        self.lbl_text_upper = QLabel(self.centralwidget)
        self.lbl_text_upper.setObjectName(u"lbl_text_upper")
        self.lbl_text_upper.setStyleSheet(u"font-size: 14pt;")

        self.horizontalLayout_6.addWidget(self.lbl_text_upper)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 1, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(10, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.horizontalSpacer_29, 6, 1, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(10, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.horizontalSpacer_33, 8, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cb_russian = QCheckBox(self.centralwidget)
        self.cb_russian.setObjectName(u"cb_russian")
        sizePolicy.setHeightForWidth(self.cb_russian.sizePolicy().hasHeightForWidth())
        self.cb_russian.setSizePolicy(sizePolicy)
        self.cb_russian.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_russian.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.cb_russian)

        self.lbl_text_russian = QLabel(self.centralwidget)
        self.lbl_text_russian.setObjectName(u"lbl_text_russian")
        self.lbl_text_russian.setStyleSheet(u"font-size: 14pt;")

        self.horizontalLayout_8.addWidget(self.lbl_text_russian)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 7, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.cb_lower = QCheckBox(self.centralwidget)
        self.cb_lower.setObjectName(u"cb_lower")
        sizePolicy.setHeightForWidth(self.cb_lower.sizePolicy().hasHeightForWidth())
        self.cb_lower.setSizePolicy(sizePolicy)
        self.cb_lower.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_lower.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.cb_lower)

        self.lbl_text_lower = QLabel(self.centralwidget)
        self.lbl_text_lower.setObjectName(u"lbl_text_lower")
        self.lbl_text_lower.setStyleSheet(u"font-size: 14pt;")

        self.horizontalLayout_7.addWidget(self.lbl_text_lower)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 5, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(35, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_11, 0, 2, 15, 1)

        self.horizontalSpacer_34 = QSpacerItem(10, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.horizontalSpacer_34, 10, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.cb_special = QCheckBox(self.centralwidget)
        self.cb_special.setObjectName(u"cb_special")
        sizePolicy.setHeightForWidth(self.cb_special.sizePolicy().hasHeightForWidth())
        self.cb_special.setSizePolicy(sizePolicy)
        self.cb_special.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_special.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.cb_special)

        self.lbl_text_special = QLabel(self.centralwidget)
        self.lbl_text_special.setObjectName(u"lbl_text_special")
        self.lbl_text_special.setStyleSheet(u"font-size: 14pt;")

        self.horizontalLayout_11.addWidget(self.lbl_text_special)


        self.gridLayout_2.addLayout(self.horizontalLayout_11, 11, 1, 1, 1)

        self.horizontalSpacer_37 = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.horizontalSpacer_37, 0, 1, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(10, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.horizontalSpacer_26, 2, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sld_lenght = QSlider(self.centralwidget)
        self.sld_lenght.setObjectName(u"sld_lenght")
        self.sld_lenght.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sld_lenght.setMinimum(2)
        self.sld_lenght.setMaximum(50)
        self.sld_lenght.setValue(16)
        self.sld_lenght.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.sld_lenght)

        self.horizontalSpacer_36 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_36)

        self.lbl_text_lenght = QLabel(self.centralwidget)
        self.lbl_text_lenght.setObjectName(u"lbl_text_lenght")
        self.lbl_text_lenght.setStyleSheet(u"font-size: 14pt;")

        self.horizontalLayout_3.addWidget(self.lbl_text_lenght)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.cb_number = QCheckBox(self.centralwidget)
        self.cb_number.setObjectName(u"cb_number")
        sizePolicy.setHeightForWidth(self.cb_number.sizePolicy().hasHeightForWidth())
        self.cb_number.setSizePolicy(sizePolicy)
        self.cb_number.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_number.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.cb_number)

        self.lbl_text_number = QLabel(self.centralwidget)
        self.lbl_text_number.setObjectName(u"lbl_text_number")
        self.lbl_text_number.setStyleSheet(u"font-size: 14pt;")

        self.horizontalLayout_9.addWidget(self.lbl_text_number)


        self.gridLayout_2.addLayout(self.horizontalLayout_9, 9, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(35, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 15, 1)

        self.horizontalSpacer_35 = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.horizontalSpacer_35, 12, 1, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(10, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.horizontalSpacer_28, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer_6 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.btn_history = QPushButton(self.centralwidget)
        self.btn_history.setObjectName(u"btn_history")
        self.btn_history.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.btn_history, 2, 6, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_7, 2, 7, 1, 1)

        self.btn_main = QPushButton(self.centralwidget)
        self.btn_main.setObjectName(u"btn_main")
        self.btn_main.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.btn_main, 2, 4, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_8, 2, 5, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_9, 2, 3, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_10, 2, 0, 1, 1)

        self.btn_setting = QPushButton(self.centralwidget)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_6.addWidget(self.btn_setting, 2, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_6, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_14 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_14)

        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btn_copy)

        self.horizontalSpacer_15 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_15)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_name_app.setText(QCoreApplication.translate("MainWindow", u"\U0001f510 \U00000413\U00000435\U0000043d\U00000435\U00000440\U00000430\U00000442\U0000043e\U00000440 \U0000043f\U00000430\U00000440\U0000043e\U0000043b\U00000435\U00000439 \U0001f510", None))
        self.password.setText(QCoreApplication.translate("MainWindow", u"QdRkRsZo]IxCf]Cl8Wd5Le~0Ae5Wb9Sa[4", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u"\U0001f3b2 \U00000413\U00000435\U0000043d\U00000435\U00000440\U00000430\U00000446\U00000438\U0000044f", None))
        self.cb_upper.setText("")
        self.lbl_text_upper.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u0433\u043b\u0430\u0432\u043d\u044b\u0435 \u0431\u0443\u043a\u0432\u044b", None))
        self.cb_russian.setText("")
        self.lbl_text_russian.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0440\u0443\u0441\u0441\u043a\u0438\u0435 \u0431\u0443\u043a\u0432\u044b", None))
        self.cb_lower.setText("")
        self.lbl_text_lower.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u043f\u0440\u043e\u043f\u0438\u0441\u043d\u044b\u0435 \u0431\u0443\u043a\u0432\u044b", None))
        self.cb_special.setText("")
        self.lbl_text_special.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0441\u043f\u0435\u0446\u0441\u0438\u043c\u0432\u043e\u043b\u044b", None))
        self.lbl_text_lenght.setText(QCoreApplication.translate("MainWindow", u"16 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432", None))
        self.cb_number.setText("")
        self.lbl_text_number.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0447\u0438\u0441\u043b\u0430", None))
        self.btn_history.setText(QCoreApplication.translate("MainWindow", u"\U0001f4dc \U00000418\U00000441\U00000442\U0000043e\U00000440\U00000438\U0000044f", None))
        self.btn_main.setText(QCoreApplication.translate("MainWindow", u"\U0001f510 \U00000410\U0000043d\U00000430\U0000043b\U00000438\U00000437\U00000430\U00000442\U0000043e\U00000440", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"\u2699\ufe0f \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.btn_copy.setText(QCoreApplication.translate("MainWindow", u"\U0001f4cb \U00000421\U0000043a\U0000043e\U0000043f\U00000438\U00000440\U0000043e\U00000432\U00000430\U00000442\U0000044c", None))
    # retranslateUi

