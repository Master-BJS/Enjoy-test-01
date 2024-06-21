from PySide6 import QtCore, QtGui, QtWidgets

class Ui_LogViewerWidget(object):
    def setupUi(self, LogViewerWidget):
        LogViewerWidget.setObjectName("LogViewerWidget")
        LogViewerWidget.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(LogViewerWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        self.label_file_name = QtWidgets.QLabel(self.centralwidget)
        self.label_file_name.setObjectName("label_file_name")
        self.gridLayout.addWidget(self.label_file_name, 0, 0, 1, 1)
        
        self.lineEdit_file_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_file_name.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.lineEdit_file_name.setObjectName("lineEdit_file_name")
        self.gridLayout.addWidget(self.lineEdit_file_name, 0, 1, 1, 1)
        
        self.pushButton_open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButton_open.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_open.setObjectName("pushButton_open")
        self.gridLayout.addWidget(self.pushButton_open, 0, 2, 1, 1)
        
        self.label_request_read_count = QtWidgets.QLabel(self.centralwidget)
        self.label_request_read_count.setObjectName("label_request_read_count")
        self.gridLayout.addWidget(self.label_request_read_count, 0, 3, 1, 1)
        
        self.request_read_count_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.request_read_count_edit.setMinimumSize(QtCore.QSize(50, 0))
        self.request_read_count_edit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.request_read_count_edit.setObjectName("request_read_count_edit")
        self.gridLayout.addWidget(self.request_read_count_edit, 0, 4, 1, 1)
        
        self.pushButton_break = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_break.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButton_break.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_break.setObjectName("pushButton_break")
        self.gridLayout.addWidget(self.pushButton_break, 0, 5, 1, 1)
        
        self.pushButton_read = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_read.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButton_read.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_read.setObjectName("pushButton_read")
        self.gridLayout.addWidget(self.pushButton_read, 0, 6, 1, 1)
        
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButton_next.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_next.setObjectName("pushButton_next")
        self.gridLayout.addWidget(self.pushButton_next, 0, 7, 1, 1)
        
        self.verticalLayout.addLayout(self.gridLayout)
        
        self.horizontalLayout_table = QtWidgets.QHBoxLayout()
        self.horizontalLayout_table.setObjectName("horizontalLayout_table")
        
        self.tableWidget_left = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_left.setObjectName("tableWidget_left")
        self.horizontalLayout_table.addWidget(self.tableWidget_left)
        
        self.verticalLayout_right = QtWidgets.QVBoxLayout()
        self.verticalLayout_right.setObjectName("verticalLayout_right")
        
        self.tableWidget_right = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_right.setObjectName("tableWidget_right")
        self.tableWidget_right.setColumnCount(2)
        self.tableWidget_right.setHorizontalHeaderLabels(["항목명", "값"])
        self.tableWidget_right.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalLayout_right.addWidget(self.tableWidget_right)
        
        self.gridLayout_footer = QtWidgets.QGridLayout()
        self.gridLayout_footer.setObjectName("gridLayout_footer")
        
        self.label_struct_length = QtWidgets.QLabel(self.centralwidget)
        self.label_struct_length.setObjectName("label_struct_length")
        self.gridLayout_footer.addWidget(self.label_struct_length, 0, 0, 1, 1)
        
        self.lineEdit_struct_length = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_struct_length.setObjectName("lineEdit_struct_length")
        self.gridLayout_footer.addWidget(self.lineEdit_struct_length, 0, 1, 1, 1)
        
        self.label_message_length = QtWidgets.QLabel(self.centralwidget)
        self.label_message_length.setObjectName("label_message_length")
        self.gridLayout_footer.addWidget(self.label_message_length, 1, 0, 1, 1)
        
        self.lineEdit_message_length = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_message_length.setObjectName("lineEdit_message_length")
        self.gridLayout_footer.addWidget(self.lineEdit_message_length, 1, 1, 1, 1)
        
        self.label_exceeded_length = QtWidgets.QLabel(self.centralwidget)
        self.label_exceeded_length.setObjectName("label_exceeded_length")
        self.gridLayout_footer.addWidget(self.label_exceeded_length, 2, 0, 1, 1)
        
        self.lineEdit_exceeded_length = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_exceeded_length.setObjectName("lineEdit_exceeded_length")
        self.gridLayout_footer.addWidget(self.lineEdit_exceeded_length, 2, 1, 1, 1)
        
        self.verticalLayout_right.addLayout(self.gridLayout_footer)
        self.horizontalLayout_table.addLayout(self.verticalLayout_right)
        self.verticalLayout.addLayout(self.horizontalLayout_table)
        
        LogViewerWidget.setCentralWidget(self.centralwidget)
        
        self.statusBar = QtWidgets.QStatusBar(LogViewerWidget)
        self.statusBar.setObjectName("statusBar")
        LogViewerWidget.setStatusBar(self.statusBar)

        self.menubar = QtWidgets.QMenuBar(LogViewerWidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        
        self.menuLOG_정의_불러오기 = QtWidgets.QMenu(self.menubar)
        self.menuLOG_정의_불러오기.setObjectName("menuLOG_정의_불러오기")
        
        self.menuFILE = QtWidgets.QMenu(self.menubar)
        self.menuFILE.setObjectName("menuFILE")
        
        self.menuKEY_OPTION = QtWidgets.QMenu(self.menubar)
        self.menuKEY_OPTION.setObjectName("menuKEY_OPTION")
        
        self.menuREAD = QtWidgets.QMenu(self.menubar)
        self.menuREAD.setObjectName("menuREAD")
        
        self.menuFILTER = QtWidgets.QMenu(self.menubar)
        self.menuFILTER.setObjectName("menuFILTER")
        
        self.menu전문_송수신 = QtWidgets.QMenu(self.menubar)
        self.menu전문_송수신.setObjectName("menu전문_송수신")
        
        self.menu보기 = QtWidgets.QMenu(self.menubar)
        self.menu보기.setObjectName("menu보기")
        
        self.menubar.addAction(self.menuLOG_정의_불러오기.menuAction())
        self.menubar.addAction(self.menuFILE.menuAction())
        self.menubar.addAction(self.menuKEY_OPTION.menuAction())
        self.menubar.addAction(self.menuREAD.menuAction())
        self.menubar.addAction(self.menuFILTER.menuAction())
        self.menubar.addAction(self.menu전문_송수신.menuAction())
        self.menubar.addAction(self.menu보기.menuAction())
        
        LogViewerWidget.setMenuBar(self.menubar)
        
        self.retranslateUi(LogViewerWidget)
        QtCore.QMetaObject.connectSlotsByName(LogViewerWidget)

    def retranslateUi(self, LogViewerWidget):
        _translate = QtCore.QCoreApplication.translate
        LogViewerWidget.setWindowTitle(_translate("LogViewerWidget", "LOG 조회"))
        self.label_file_name.setText(_translate("LogViewerWidget", "FILE NAME :"))
        self.pushButton_open.setText(_translate("LogViewerWidget", "OPEN"))
        self.label_request_read_count.setText(_translate("LogViewerWidget", "Request Read Count"))
        self.pushButton_break.setText(_translate("LogViewerWidget", "BREAK"))
        self.pushButton_read.setText(_translate("LogViewerWidget", "READ"))
        self.pushButton_next.setText(_translate("LogViewerWidget", "NEXT"))
        self.label_struct_length.setText(_translate("LogViewerWidget", "구조체 길이"))
        self.label_message_length.setText(_translate("LogViewerWidget", "전문 길이"))
        self.label_exceeded_length.setText(_translate("LogViewerWidget", "초과한 길이"))
        self.menuLOG_정의_불러오기.setTitle(_translate("LogViewerWidget", "LOG_정의_불러오기"))
        self.menuFILE.setTitle(_translate("LogViewerWidget", "FILE"))
        self.menuKEY_OPTION.setTitle(_translate("LogViewerWidget", "KEY_OPTION"))
        self.menuREAD.setTitle(_translate("LogViewerWidget", "READ"))
        self.menuFILTER.setTitle(_translate("LogViewerWidget", "FILTER"))
        self.menu전문_송수신.setTitle(_translate("LogViewerWidget", "전문_송수신"))
        self.menu보기.setTitle(_translate("LogViewerWidget", "보기"))
