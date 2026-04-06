from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import src.views.config_rc as config_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 700)
        MainWindow.setMinimumSize(QSize(500, 700))
        icon = QIcon()
        icon.addFile(u"resources\icons\icon-white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #1e1e1e;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #2d2d2d;\n"
"    color: #ffffff;\n"
"    border: 1px solid #3c3c3c;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #094771;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #2d2d2d;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c3c3c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1e1e1e;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #094771;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid #3c3c3c;\n"
"    border-radius: 4px;\n"
"    background-color: #2d2d2d;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #4caf50;\n"
"    border-radius: 3px;\n"
"}")
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

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.le_password = QLineEdit(self.centralwidget)
        self.le_password.setObjectName(u"le_password")

        self.gridLayout_2.addWidget(self.le_password, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_11 = QSpacerItem(35, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(35, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_12, 0, 2, 1, 1)

        self.pb_bar = QProgressBar(self.centralwidget)
        self.pb_bar.setObjectName(u"pb_bar")
        self.pb_bar.setValue(50)
        self.pb_bar.setTextVisible(False)

        self.gridLayout_7.addWidget(self.pb_bar, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_7)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.lbl_result = QLabel(self.centralwidget)
        self.lbl_result.setObjectName(u"lbl_result")
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_result)

        self.verticalSpacer_5 = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_13 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_13, 3, 2, 1, 1)

        self.lbl_full_result_3 = QLabel(self.centralwidget)
        self.lbl_full_result_3.setObjectName(u"lbl_full_result_3")
        self.lbl_full_result_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lbl_full_result_3, 5, 1, 1, 3)

        self.lbl_full_result = QLabel(self.centralwidget)
        self.lbl_full_result.setObjectName(u"lbl_full_result")
        self.lbl_full_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lbl_full_result, 3, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.horizontalSpacer_17, 1, 1, 1, 3)

        self.lbl_full_result_2 = QLabel(self.centralwidget)
        self.lbl_full_result_2.setObjectName(u"lbl_full_result_2")
        self.lbl_full_result_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lbl_full_result_2, 3, 3, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.horizontalSpacer_16, 4, 1, 1, 3)

        self.lbl_full_result_4 = QLabel(self.centralwidget)
        self.lbl_full_result_4.setObjectName(u"lbl_full_result_4")
        self.lbl_full_result_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.lbl_full_result_4, 0, 1, 1, 3)

        self.horizontalSpacer_4 = QSpacerItem(35, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 4, 6, 1)

        self.horizontalSpacer_3 = QSpacerItem(35, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 0, 6, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer_6 = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.btn_history = QPushButton(self.centralwidget)
        self.btn_history.setObjectName(u"btn_history")

        self.gridLayout_6.addWidget(self.btn_history, 2, 6, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_6, 2, 7, 1, 1)

        self.btn_generate = QPushButton(self.centralwidget)
        self.btn_generate.setObjectName(u"btn_generate")

        self.gridLayout_6.addWidget(self.btn_generate, 2, 4, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_8, 2, 5, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_7, 2, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)

        self.btn_setting = QPushButton(self.centralwidget)
        self.btn_setting.setObjectName(u"btn_setting")

        self.gridLayout_6.addWidget(self.btn_setting, 2, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_6, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_9 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_10, 0, 2, 1, 1)

        self.btn_password = QPushButton(self.centralwidget)
        self.btn_password.setObjectName(u"btn_password")

        self.gridLayout_5.addWidget(self.btn_password, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_5)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_14 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_14)

        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")

        self.horizontalLayout.addWidget(self.btn_copy)

        self.horizontalSpacer_15 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_15)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_9)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PasswordAnalyzer", None))
        self.lbl_name_app.setText(QCoreApplication.translate("MainWindow", u"\U0001f510 \U00000410\U0000043d\U00000430\U0000043b\U00000438\U00000437\U00000430\U00000442\U0000043e\U00000440 \U0000043f\U00000430\U00000440\U0000043e\U0000043b\U00000435\U00000439 \U0001f510", None))
        self.le_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c...", None))
        self.pb_bar.setFormat("")
        self.lbl_result.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442: 40%\n"
"\u041d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u044b\u0439", None))
        self.lbl_full_result_3.setText(QCoreApplication.translate("MainWindow", u"\U0001f4aa \U0000041d\U00000430\U00000434\U00000451\U00000436\U0000043d\U0000043e\U00000441\U00000442\U0000044c: \U00000421\U00000420\U00000415\U00000414\U0000041d\U00000418\U00000419", None))
        self.lbl_full_result.setText(QCoreApplication.translate("MainWindow", u"\u2705 \u0414\u043b\u0438\u043d\u0430: 12 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432\n"
"\u2705 \u0417\u0430\u0433\u043b\u0430\u0432\u043d\u044b\u0435 \u0431\u0443\u043a\u0432\u044b: A-Z\n"
" \u2705 \u0421\u0442\u0440\u043e\u0447\u043d\u044b\u0435 \u0431\u0443\u043a\u0432\u044b: a-z\n"
"\u2705 \u0426\u0438\u0444\u0440\u044b: 0-9\n"
"\u274c \u0421\u043f\u0435\u0446\u0441\u0438\u043c\u0432\u043e\u043b\u044b: !@#$%\n"
"\u042d\u043d\u0442\u0440\u043e\u043f\u0438\u044f: 12.312 \u0431\u0438\u0442 ", None))
        self.lbl_full_result_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0445\u043e\u0436\u0435\u0441\u0442\u044c \u0441 \u043f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u044b\u043c\u0438 \u043f\u0430\u0440\u043e\u043b\u044f\u043c\u0438: \n"
"\u0421\u0442\u0430\u0442\u0443\u0441: \u043e\u0442\u0441\u0443\u0442\u0441\u0432\u0443\u0435\u0442", None))
        self.lbl_full_result_4.setText(QCoreApplication.translate("MainWindow", u"\U0001f4ca \U00000414\U00000435\U00000442\U00000430\U0000043b\U0000044c\U0000043d\U0000044b\U00000439 \U00000430\U0000043d\U00000430\U0000043b\U00000438\U00000437:", None))
        self.btn_history.setText(QCoreApplication.translate("MainWindow", u"\U0001f4dc \U00000418\U00000441\U00000442\U0000043e\U00000440\U00000438\U0000044f", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u"\U0001f3b2 \U00000413\U00000435\U0000043d\U00000435\U00000440\U00000430\U00000446\U00000438\U0000044f", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"\u2699\ufe0f \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.btn_password.setText(QCoreApplication.translate("MainWindow", u"\U0001f513 \U0000041f\U0000043e\U0000043a\U00000430\U00000437\U00000430\U00000442\U0000044c \U0000043f\U00000430\U00000440\U0000043e\U0000043b\U0000044c", None))
        self.btn_copy.setText(QCoreApplication.translate("MainWindow", u"\U0001f4cb \U00000421\U0000043a\U0000043e\U0000043f\U00000438\U00000440\U0000043e\U00000432\U00000430\U00000442\U0000044c", None))
    # retranslateUi

