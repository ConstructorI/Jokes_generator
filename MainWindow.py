# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)
import res as res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(549, 732)
        MainWindow.setMinimumSize(QSize(549, 730))
        icon = QIcon()
        icon.addFile(u":/icon/flower.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	font: 8pt \"Bahnschrift\";\n"
"	color: rgb(60, 66, 92);\n"
"	background-color: rgb(228, 255, 194);\n"
"}\n"
"\n"
"QFrame {\n"
"	color: rgb(60, 66, 92);\n"
"	background-color: rgba(255, 255, 255, 70);\n"
"	border: none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid rgb(255, 192, 133);\n"
"	border-radius: 3px;\n"
"	color: rgb(60, 66, 92);\n"
"	background-color: rgb(161, 204, 210);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgba(255, 192, 133, 70);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(255, 192, 133);\n"
"}\n"
"\n"
"QPushButton {\n"
"	font: 12pt \"Bahnschrift\";\n"
"	border-radius: 3px;\n"
"	color: rgb(60, 66, 92);\n"
"	background-color: rgb(255, 192, 133);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	font: 12pt \"Bahnschrift\";\n"
"	border: 1px solid rgb(172, 255, 120);\n"
"	border-radius: 3px;\n"
"	color: rgb(60, 66, 92);\n"
"	background-color: rgb(255, 192, 133);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	font: 12pt \"Bahnschrift\";\n"
"	color: rgb(60, 66, 92);\n"
""
                        "	border: 2px solid rgb(172, 255, 120);\n"
"	background-color: rgb(172, 255, 120);\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	font: 10pt \"Bahnschrift\";\n"
"    background-color:rgb(228, 255, 194);color:rgb(60, 66, 92);border:1px;border-style:solid;border-color:rgb(255, 192, 133);border-radius: 3px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"	font: 10pt \"Bahnschrift\";\n"
"    background-color:rgb(228, 255, 194);color:rgb(60, 66, 92);border:2px;border-style:solid;border-color:rgb(255, 192, 133);border-radius: 3px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(532, 712))
        self.tabWidget.setStyleSheet(u"QTabBar::tab:selected {background: rgb(255, 192, 133);}\n"
"QTabBar::tab {background: rgba(255, 255, 255, 70);}\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(512, 512))
        self.widget.setMaximumSize(QSize(512, 512))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 0))
        self.lineEdit_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit_2.setStyleSheet(u"font: 10pt \"Bahnschrift\";\n"
"border: none;\n"
"background-color: rgba(255, 255, 255, 70);")
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.plainTextEdit = QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(512, 0))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(512, 25))
        self.pushButton.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(512, 24))
        self.label_2.setMaximumSize(QSize(16777215, 24))
        self.label_2.setStyleSheet(u"font: 10pt \"Bahnschrift\";\n"
"background-color: none;\n"
"border: none;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plainTextEdit_2 = QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMinimumSize(QSize(512, 470))
        self.plainTextEdit_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.plainTextEdit_2.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.plainTextEdit_2)

        self.plainTextEdit_3 = QPlainTextEdit(self.tab_2)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setMinimumSize(QSize(512, 0))

        self.verticalLayout_2.addWidget(self.plainTextEdit_3)

        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(512, 30))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 24))
        self.label_3.setMaximumSize(QSize(16777215, 24))
        self.label_3.setStyleSheet(u"font: 10pt \"Bahnschrift\";\n"
"background-color: none;\n"
"border: none;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(512, 25))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.plainTextEdit_4 = QPlainTextEdit(self.tab_3)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_3.addWidget(self.plainTextEdit_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setStyleSheet(u"font: 10pt \"Bahnschrift\";\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.lineEdit = QLineEdit(self.tab_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 20))
        self.lineEdit.setStyleSheet(u"font: 10pt \"Bahnschrift\";\n"
"background-color: rgba(255, 255, 255, 70);")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setStyleSheet(u"font: 10pt \"Bahnschrift\";\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout.addWidget(self.label_4)

        self.spinBox = QSpinBox(self.tab_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(70, 20))
        self.spinBox.setStyleSheet(u"font: 10pt \"Bahnschrift\";\n"
"border: none;\n"
"background-color: rgba(255, 255, 255, 70);")
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(9999)
        self.spinBox.setValue(15)

        self.horizontalLayout.addWidget(self.spinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.pushButton_4 = QPushButton(self.tab_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 25))

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Jokes_generator", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u043f\u0440\u043e\u0441...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0436\u0438\u0434\u0430\u0439\u0442\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.plainTextEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c\u0441\u044f \u0438\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.plainTextEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u043f\u0440\u043e\u0441...", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0436\u0438\u0434\u0430\u0439\u0442\u0435", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0435\u043d\u0438\u0435 \u0441 \u0418\u0418", None))
        self.plainTextEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442. \u0414\u043b\u044f \u043d\u0430\u0438\u043b\u0443\u0447\u0448\u0438\u0445 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0432 \u0444\u0430\u0439\u043b\u0435 \u0441\u043b\u0435\u0434\u0443\u0435\u0442 \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u044c \u043f\u043e\u0441\u0442\u0440\u043e\u0447\u043d\u043e.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430:", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u043e\u043a\u043b\u044f\u0442\u043e\u0435.txt", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043b\u043e\u0432:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0443\u0447\u0430\u0439\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0438\u0437 txt", None))
    # retranslateUi

