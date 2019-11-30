from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    msgbox = QMessageBox()
    msgbox.setText("Hi")
    msgbox.setWindowTitle("See!")
    msgbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
    msgbox.show()
    sys.exit(app.exec_())