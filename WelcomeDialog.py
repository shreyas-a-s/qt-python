#!/usr/bin/env python3

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("WelcomeDialog.ui", self)

        self.ExitButton.clicked.connect(self.exit_application)

        self.ContinueButton.clicked.connect(self.continue_application)

    def exit_application(self):
        print("User pressed 'Exit'. Exiting the script.")
        with open("exit_signal.tmp", "w") as file:
            file.write("exit")
        self.close()

    def continue_application(self):
        print("User pressed 'Continue'. Continuing with the script.")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()

