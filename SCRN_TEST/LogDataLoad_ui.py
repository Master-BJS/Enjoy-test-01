# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogDataLoad.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_LogDataLoad(object):
    def setupUi(self, LogDataLoad):
        if not LogDataLoad.objectName():
            LogDataLoad.setObjectName(u"LogDataLoad")
        LogDataLoad.resize(800, 600)
        self.actionFILTER = QAction(LogDataLoad)
        self.actionFILTER.setObjectName(u"actionFILTER")
        self.centralwidget = QWidget(LogDataLoad)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_file_name = QLabel(self.centralwidget)
        self.label_file_name.setObjectName(u"label_file_name")

        self.gridLayout.addWidget(self.label_file_name, 0, 0, 1, 1)

        self.lineEdit_file_name = QLineEdit(self.centralwidget)
        self.lineEdit_file_name.setObjectName(u"lineEdit_file_name")

        self.gridLayout.addWidget(self.lineEdit_file_name, 0, 1, 1, 1)

        self.pushButton_open = QPushButton(self.centralwidget)
        self.pushButton_open.setObjectName(u"pushButton_open")

        self.gridLayout.addWidget(self.pushButton_open, 0, 2, 1, 1)

        self.label_request_read_count = QLabel(self.centralwidget)
        self.label_request_read_count.setObjectName(u"label_request_read_count")

        self.gridLayout.addWidget(self.label_request_read_count, 0, 3, 1, 1)

        self.request_read_count_edit = QLineEdit(self.centralwidget)
        self.request_read_count_edit.setObjectName(u"request_read_count_edit")

        self.gridLayout.addWidget(self.request_read_count_edit, 0, 4, 1, 1)

        self.pushButton_break = QPushButton(self.centralwidget)
        self.pushButton_break.setObjectName(u"pushButton_break")

        self.gridLayout.addWidget(self.pushButton_break, 0, 5, 1, 1)

        self.pushButton_read = QPushButton(self.centralwidget)
        self.pushButton_read.setObjectName(u"pushButton_read")

        self.gridLayout.addWidget(self.pushButton_read, 0, 6, 1, 1)

        self.pushButton_next = QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName(u"pushButton_next")

        self.gridLayout.addWidget(self.pushButton_next, 0, 7, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_table = QHBoxLayout()
        self.horizontalLayout_table.setObjectName(u"horizontalLayout_table")
        self.tableWidget_left = QTableWidget(self.centralwidget)
        self.tableWidget_left.setObjectName(u"tableWidget_left")

        self.horizontalLayout_table.addWidget(self.tableWidget_left)

        self.verticalLayout_right = QVBoxLayout()
        self.verticalLayout_right.setObjectName(u"verticalLayout_right")
        self.tableWidget_right = QTableWidget(self.centralwidget)
        if (self.tableWidget_right.columnCount() < 2):
            self.tableWidget_right.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_right.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_right.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_right.setObjectName(u"tableWidget_right")

        self.verticalLayout_right.addWidget(self.tableWidget_right)

        self.gridLayout_footer = QGridLayout()
        self.gridLayout_footer.setObjectName(u"gridLayout_footer")
        self.label_struct_length = QLabel(self.centralwidget)
        self.label_struct_length.setObjectName(u"label_struct_length")

        self.gridLayout_footer.addWidget(self.label_struct_length, 0, 0, 1, 1)

        self.lineEdit_struct_length = QLineEdit(self.centralwidget)
        self.lineEdit_struct_length.setObjectName(u"lineEdit_struct_length")

        self.gridLayout_footer.addWidget(self.lineEdit_struct_length, 0, 1, 1, 1)

        self.label_message_length = QLabel(self.centralwidget)
        self.label_message_length.setObjectName(u"label_message_length")

        self.gridLayout_footer.addWidget(self.label_message_length, 1, 0, 1, 1)

        self.lineEdit_message_length = QLineEdit(self.centralwidget)
        self.lineEdit_message_length.setObjectName(u"lineEdit_message_length")

        self.gridLayout_footer.addWidget(self.lineEdit_message_length, 1, 1, 1, 1)

        self.label_exceeded_length = QLabel(self.centralwidget)
        self.label_exceeded_length.setObjectName(u"label_exceeded_length")

        self.gridLayout_footer.addWidget(self.label_exceeded_length, 2, 0, 1, 1)

        self.lineEdit_exceeded_length = QLineEdit(self.centralwidget)
        self.lineEdit_exceeded_length.setObjectName(u"lineEdit_exceeded_length")

        self.gridLayout_footer.addWidget(self.lineEdit_exceeded_length, 2, 1, 1, 1)


        self.verticalLayout_right.addLayout(self.gridLayout_footer)


        self.horizontalLayout_table.addLayout(self.verticalLayout_right)


        self.verticalLayout.addLayout(self.horizontalLayout_table)

        LogDataLoad.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(LogDataLoad)
        self.statusBar.setObjectName(u"statusBar")
        LogDataLoad.setStatusBar(self.statusBar)
        self.menubar = QMenuBar(LogDataLoad)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuLOG_정의_불러오기 = QMenu(self.menubar)
        self.menuLOG_정의_불러오기.setObjectName(u"menuLOG_\uc815\uc758_\ubd88\ub7ec\uc624\uae30")
        self.menuFILE = QMenu(self.menubar)
        self.menuFILE.setObjectName(u"menuFILE")
        self.menuKEY_OPTION = QMenu(self.menubar)
        self.menuKEY_OPTION.setObjectName(u"menuKEY_OPTION")
        self.menuREAD = QMenu(self.menubar)
        self.menuREAD.setObjectName(u"menuREAD")
        self.menu전문_송수신 = QMenu(self.menubar)
        self.menu전문_송수신.setObjectName(u"menu\uc804\ubb38_\uc1a1\uc218\uc2e0")
        self.menu보기 = QMenu(self.menubar)
        self.menu보기.setObjectName(u"menu\ubcf4\uae30")
        LogDataLoad.setMenuBar(self.menubar)

        self.menubar.addAction(self.actionFILTER)
        self.menubar.addAction(self.menuLOG_정의_불러오기.menuAction())
        self.menubar.addAction(self.menuFILE.menuAction())
        self.menubar.addAction(self.menuKEY_OPTION.menuAction())
        self.menubar.addAction(self.menuREAD.menuAction())
        self.menubar.addAction(self.menu전문_송수신.menuAction())
        self.menubar.addAction(self.menu보기.menuAction())

        self.retranslateUi(LogDataLoad)

        QMetaObject.connectSlotsByName(LogDataLoad)
    # setupUi

    def retranslateUi(self, LogDataLoad):
        LogDataLoad.setWindowTitle(QCoreApplication.translate("LogDataLoad", u"LOG \uc870\ud68c", None))
        self.actionFILTER.setText(QCoreApplication.translate("LogDataLoad", u"FILTER", None))
        self.label_file_name.setText(QCoreApplication.translate("LogDataLoad", u"FILE NAME :", None))
        self.pushButton_open.setText(QCoreApplication.translate("LogDataLoad", u"OPEN", None))
        self.label_request_read_count.setText(QCoreApplication.translate("LogDataLoad", u"Request Read Count", None))
        self.pushButton_break.setText(QCoreApplication.translate("LogDataLoad", u"BREAK", None))
        self.pushButton_read.setText(QCoreApplication.translate("LogDataLoad", u"READ", None))
        self.pushButton_next.setText(QCoreApplication.translate("LogDataLoad", u"NEXT", None))
        ___qtablewidgetitem = self.tableWidget_right.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LogDataLoad", u"\ud56d\ubaa9\uba85", None));
        ___qtablewidgetitem1 = self.tableWidget_right.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LogDataLoad", u"\uac12", None));
        self.label_struct_length.setText(QCoreApplication.translate("LogDataLoad", u"\uad6c\uc870\uccb4 \uae38\uc774", None))
        self.label_message_length.setText(QCoreApplication.translate("LogDataLoad", u"\uc804\ubb38 \uae38\uc774", None))
        self.label_exceeded_length.setText(QCoreApplication.translate("LogDataLoad", u"\ucd08\uacfc\ud55c \uae38\uc774", None))
        self.menuLOG_정의_불러오기.setTitle(QCoreApplication.translate("LogDataLoad", u"LOG_\uc815\uc758_\ubd88\ub7ec\uc624\uae30", None))
        self.menuFILE.setTitle(QCoreApplication.translate("LogDataLoad", u"FILE", None))
        self.menuKEY_OPTION.setTitle(QCoreApplication.translate("LogDataLoad", u"KEY_OPTION", None))
        self.menuREAD.setTitle(QCoreApplication.translate("LogDataLoad", u"READ", None))
        self.menu전문_송수신.setTitle(QCoreApplication.translate("LogDataLoad", u"\uc804\ubb38_\uc1a1\uc218\uc2e0", None))
        self.menu보기.setTitle(QCoreApplication.translate("LogDataLoad", u"\ubcf4\uae30", None))
    # retranslateUi

