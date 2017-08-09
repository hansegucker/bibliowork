from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget,
                             QHBoxLayout, QVBoxLayout,
                             QLineEdit, QPushButton, QLabel, QListWidget,
                             QMessageBox,
                             QApplication, QDialog,
                             QGridLayout, QSizePolicy,
                             QTextEdit, QMessageBox)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import *


class Window(QDialog):
    def __init__(self, parent=None):
        """ Initialisiere das Fenster """

        super().__init__(parent)
        self.Labels = {}
        self.Buttons = {}
        self.Layouts = {}
        self.Icons = {}
        self.OtherWidgets = {}
        self.TextEdits = {}

        self.color_green = "#5cb85c"
        self.color_red = "#d9534f"

        # Initialisiere die UI und den Mainloop
        self.init_window_ui()
        self.init_must_check()

    # Allgemeine UI-Funktionen
    def init_window_ui(self):
        # Definiere eine vorgefertigte Linie
        self.BorderLine = QLabel("<hr>")

        # Initialisiere vertikales Layout
        self.Layouts["vbox"] = QVBoxLayout()

        # Setze Layout für das Fenster
        self.setLayout(self.Layouts["vbox"])

    def finish_ui(self):
        self.Layouts["vbox"].addStretch()
        self.show()

    def make_button(self, text, icon="", action=None, height="full", color=""):
        """ Erstellt einen vordefinierten Button """
        button = QPushButton(text)
        if icon != "":
            button.setIcon(self.Icons[icon])
            button.setIconSize(QSize(50, 50))
        if action != None:
            button.clicked.connect(action)
        if height != "full":
            button.setFixedHeight(height)
        else:
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if color != "":
            button.setStyleSheet("background-color:" + color + ";");
        return button

    def init_must_check(self):
        """ Initialisert einen "Mainloop" """

        self.WindowMustCheckTimer = QTimer()
        self.WindowMustCheckTimer.timeout.connect(self.must_check)
        self.WindowMustCheckTimer.start(100)

    def must_check(self):
        """ Führt den Mainloop durch """

        self.WindowMustCheckTimer.start(100)
        self.updated_must_check()

    def updated_must_check(self):
        pass
