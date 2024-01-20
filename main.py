#!/usr/bin/env python

from WelcomeDialog import *
from PyQt5.QtWidgets import QApplication, QDialog

class WelcomeDialog(QDialog, Ui_WelcomeDialogWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    welcome_dialog = WelcomeDialog()
    welcome_dialog.show()
    sys.exit(app.exec_())

