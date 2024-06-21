# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_inq.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.openButton = QPushButton(self.centralwidget)
        self.openButton.setObjectName(u"openButton")

        self.horizontalLayout.addWidget(self.openButton)

        self.requestReadCountLabel = QLabel(self.centralwidget)
        self.requestReadCountLabel.setObjectName(u"requestReadCountLabel")

        self.horizontalLayout.addWidget(self.requestReadCountLabel)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setValue(50)

        self.horizontalLayout.addWidget(self.spinBox)

        self.breakButton = QPushButton(self.centralwidget)
        self.breakButton.setObjectName(u"breakButton")

        self.horizontalLayout.addWidget(self.breakButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.mainTable = QTableWidget(self.centralwidget)
        if (self.mainTable.columnCount() < 1):
            self.mainTable.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.mainTable.setObjectName(u"mainTable")

        self.verticalLayout.addWidget(self.mainTable)

        self.sideTable = QTableWidget(self.centralwidget)
        if (self.sideTable.columnCount() < 2):
            self.sideTable.setColumnCount(2)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.sideTable.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.sideTable.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        self.sideTable.setObjectName(u"sideTable")

        self.verticalLayout.addWidget(self.sideTable)

        self.bottomLayout = QHBoxLayout()
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.structureLengthLabel = QLabel(self.centralwidget)
        self.structureLengthLabel.setObjectName(u"structureLengthLabel")

        self.bottomLayout.addWidget(self.structureLengthLabel)

        self.expertLengthLabel = QLabel(self.centralwidget)
        self.expertLengthLabel.setObjectName(u"expertLengthLabel")

        self.bottomLayout.addWidget(self.expertLengthLabel)

        self.surplusLengthLabel = QLabel(self.centralwidget)
        self.surplusLengthLabel.setObjectName(u"surplusLengthLabel")

        self.bottomLayout.addWidget(self.surplusLengthLabel)


        self.verticalLayout.addLayout(self.bottomLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
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
        self.menuFILTER = QMenu(self.menubar)
        self.menuFILTER.setObjectName(u"menuFILTER")
        self.menu_ = QMenu(self.menubar)
        self.menu_.setObjectName(u"menu_")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menuCLEAR = QMenu(self.menubar)
        self.menuCLEAR.setObjectName(u"menuCLEAR")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLOG_정의_불러오기.menuAction())
        self.menubar.addAction(self.menuFILE.menuAction())
        self.menubar.addAction(self.menuKEY_OPTION.menuAction())
        self.menubar.addAction(self.menuREAD.menuAction())
        self.menubar.addAction(self.menuFILTER.menuAction())
        self.menubar.addAction(self.menu_.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menuCLEAR.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LOG \uc870\ud68c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"FILE NAME:", None))
        self.openButton.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.requestReadCountLabel.setText(QCoreApplication.translate("MainWindow", u"Request Read Count", None))
        self.breakButton.setText(QCoreApplication.translate("MainWindow", u"BREAK", None))
        ___qtablewidgetitem = self.mainTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\ud56d\ubaa9\uba85", None));
        ___qtablewidgetitem1 = self.sideTable.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd", None));
        ___qtablewidgetitem2 = self.sideTable.horizontalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\uac12", None));
        self.structureLengthLabel.setText(QCoreApplication.translate("MainWindow", u"\uad6c\uc870\uccb4 \uae38\uc774", None))
        self.expertLengthLabel.setText(QCoreApplication.translate("MainWindow", u"\uc804\ubb38 \uae38\uc774", None))
        self.surplusLengthLabel.setText(QCoreApplication.translate("MainWindow", u"\ucd08\uacfc\ud55c \uae38\uc774", None))
        self.menuLOG_정의_불러오기.setTitle(QCoreApplication.translate("MainWindow", u"LOG_\uc815\uc758_\ubd88\ub7ec\uc624\uae30", None))
        self.menuFILE.setTitle(QCoreApplication.translate("MainWindow", u"FILE", None))
        self.menuKEY_OPTION.setTitle(QCoreApplication.translate("MainWindow", u"KEY OPTION", None))
        self.menuREAD.setTitle(QCoreApplication.translate("MainWindow", u"READ", None))
        self.menuFILTER.setTitle(QCoreApplication.translate("MainWindow", u"FILTER", None))
        self.menu_.setTitle(QCoreApplication.translate("MainWindow", u"\uc804\ubb38.\uc1a1\uc218\uc2e0", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\ubcf4\uae30", None))
        self.menuCLEAR.setTitle(QCoreApplication.translate("MainWindow", u"CLEAR", None))
    # retranslateUi

