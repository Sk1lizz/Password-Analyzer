from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)
import src.views.ui.config_setting_rc as config_setting_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(550, 611)
        Dialog.setMinimumSize(QSize(550, 600))
        icon = QIcon()
        icon.addFile(u"resources\\icons\\icon-white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(479, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

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

        self.verticalSpacer_2 = QSpacerItem(479, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.lbl_theme = QLabel(Dialog)
        self.lbl_theme.setObjectName(u"lbl_theme")
        self.lbl_theme.setFont(font)
        self.lbl_theme.setStyleSheet(u"font-size: 20pt;")
        self.lbl_theme.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_theme)

        self.verticalSpacer_3 = QSpacerItem(479, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cb_dark = QCheckBox(Dialog)
        self.cb_dark.setObjectName(u"cb_dark")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_dark.sizePolicy().hasHeightForWidth())
        self.cb_dark.setSizePolicy(sizePolicy)
        self.cb_dark.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_dark.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.cb_dark, 2, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 1, 0, 1, 3)

        self.cb_light = QCheckBox(Dialog)
        self.cb_light.setObjectName(u"cb_light")
        sizePolicy.setHeightForWidth(self.cb_light.sizePolicy().hasHeightForWidth())
        self.cb_light.setSizePolicy(sizePolicy)
        self.cb_light.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_light.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.cb_light, 0, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_9, 3, 0, 1, 3)

        self.cb_system = QCheckBox(Dialog)
        self.cb_system.setObjectName(u"cb_system")
        sizePolicy.setHeightForWidth(self.cb_system.sizePolicy().hasHeightForWidth())
        self.cb_system.setSizePolicy(sizePolicy)
        self.cb_system.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_system.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.cb_system, 4, 0, 1, 1)

        self.lbl_system = QLabel(Dialog)
        self.lbl_system.setObjectName(u"lbl_system")
        self.lbl_system.setStyleSheet(u"font-size: 14pt;")

        self.gridLayout_4.addWidget(self.lbl_system, 4, 1, 1, 2)

        self.lbl_dark = QLabel(Dialog)
        self.lbl_dark.setObjectName(u"lbl_dark")
        self.lbl_dark.setStyleSheet(u"font-size: 14pt;")

        self.gridLayout_4.addWidget(self.lbl_dark, 2, 1, 1, 2)

        self.lbl_light = QLabel(Dialog)
        self.lbl_light.setObjectName(u"lbl_light")
        self.lbl_light.setStyleSheet(u"font-size: 14pt;")

        self.gridLayout_4.addWidget(self.lbl_light, 0, 1, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(35, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer_5 = QSpacerItem(479, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.lbl_password = QLabel(Dialog)
        self.lbl_password.setObjectName(u"lbl_password")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        self.lbl_password.setFont(font1)
        self.lbl_password.setMouseTracking(False)
        self.lbl_password.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lbl_password.setStyleSheet(u"font-size: 18pt;")
        self.lbl_password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_password)

        self.verticalSpacer_10 = QSpacerItem(500, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_10)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.sb_amount_history = QSpinBox(Dialog)
        self.sb_amount_history.setObjectName(u"sb_amount_history")
        self.sb_amount_history.setMinimum(5)
        self.sb_amount_history.setMaximum(50)

        self.horizontalLayout.addWidget(self.sb_amount_history)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_6 = QSpacerItem(479, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 0, 4, 1, 1)

        self.le_language = QLineEdit(Dialog)
        self.le_language.setObjectName(u"le_language")

        self.gridLayout.addWidget(self.le_language, 0, 3, 1, 1)

        self.lbl_lang = QLabel(Dialog)
        self.lbl_lang.setObjectName(u"lbl_lang")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.lbl_lang.setFont(font2)
        self.lbl_lang.setMouseTracking(False)
        self.lbl_lang.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lbl_lang.setStyleSheet(u"font-size: 11pt;")
        self.lbl_lang.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_lang, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_7 = QSpacerItem(479, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_10, 0, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)

        self.btn_confirm = QPushButton(Dialog)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setCheckable(False)
        self.btn_confirm.setAutoRepeat(True)

        self.gridLayout_3.addWidget(self.btn_confirm, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer_11 = QSpacerItem(500, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_11)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"PasswordAnalyzer - settings", None))
        self.lbl_name.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.lbl_theme.setText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u043c\u0430 \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u044f:", None))
        self.cb_dark.setText("")
        self.cb_light.setText("")
        self.cb_system.setText("")
        self.lbl_system.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u043a \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        self.lbl_dark.setText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u043c\u043d\u0430\u044f", None))
        self.lbl_light.setText(QCoreApplication.translate("Dialog", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f", None))
        self.lbl_password.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u043a\u0430\u0437\u0430 \u0438\u0441\u0442\u043e\u0440\u0438\u0439:", None))
        self.lbl_lang.setText(QCoreApplication.translate("Dialog", u"\u042f\u0437\u044b\u043a:", None))
        self.btn_confirm.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
#if QT_CONFIG(shortcut)
        self.btn_confirm.setShortcut(QCoreApplication.translate("Dialog", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

