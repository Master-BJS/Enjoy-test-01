# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_test.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(832, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 0, 831, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 81, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 20, 131, 16))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 20, 151, 21))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(480, 20, 61, 21))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 20, 75, 24))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(580, 20, 75, 24))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 50, 831, 21))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 90, 256, 441))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(0, 70, 113, 21))
        self.horizontalScrollBar = QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setGeometry(QRect(0, 510, 251, 16))
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)
        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(240, 90, 16, 421))
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 70, 91, 21))
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(300, 90, 256, 441))
        self.horizontalScrollBar_2 = QScrollBar(self.centralwidget)
        self.horizontalScrollBar_2.setObjectName(u"horizontalScrollBar_2")
        self.horizontalScrollBar_2.setGeometry(QRect(300, 510, 251, 16))
        self.horizontalScrollBar_2.setOrientation(Qt.Orientation.Horizontal)
        self.verticalScrollBar_2 = QScrollBar(self.centralwidget)
        self.verticalScrollBar_2.setObjectName(u"verticalScrollBar_2")
        self.verticalScrollBar_2.setGeometry(QRect(540, 90, 16, 421))
        self.verticalScrollBar_2.setOrientation(Qt.Orientation.Vertical)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 832, 33))
        self.menuLOG = QMenu(self.menubar)
        self.menuLOG.setObjectName(u"menuLOG")
        self.menuFILE = QMenu(self.menubar)
        self.menuFILE.setObjectName(u"menuFILE")
        self.menuKEY_OPTION = QMenu(self.menubar)
        self.menuKEY_OPTION.setObjectName(u"menuKEY_OPTION")
        self.menuFILTER = QMenu(self.menubar)
        self.menuFILTER.setObjectName(u"menuFILTER")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menuCLEAR = QMenu(self.menubar)
        self.menuCLEAR.setObjectName(u"menuCLEAR")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLOG.menuAction())
        self.menubar.addAction(self.menuFILE.menuAction())
        self.menubar.addAction(self.menuKEY_OPTION.menuAction())
        self.menubar.addAction(self.menuFILTER.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menuCLEAR.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"FILE NAME : ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Request Read Count", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"BREAK", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"LOG STRUCT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"FILE DATA", None))
        self.menuLOG.setTitle(QCoreApplication.translate("MainWindow", u"LOG_STRUCT_\uc5f4\uae30", None))
        self.menuFILE.setTitle(QCoreApplication.translate("MainWindow", u"FILE", None))
        self.menuKEY_OPTION.setTitle(QCoreApplication.translate("MainWindow", u"KEY OPTION", None))
        self.menuFILTER.setTitle(QCoreApplication.translate("MainWindow", u"FILTER", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\uc804\ubb38_\uc1a1\uc218\uc2e0", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\ubcf4\uae30", None))
        self.menuCLEAR.setTitle(QCoreApplication.translate("MainWindow", u"CLEAR", None))
    # retranslateUi

