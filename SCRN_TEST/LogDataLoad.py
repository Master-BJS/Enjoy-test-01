import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from LogDataLoad_ui import Ui_LogViewerWidget

class LogViewerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LogViewerWidget()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LogViewerApp()
    window.show()
    sys.exit(app.exec())
