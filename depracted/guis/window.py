from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QMainWindow,
                             QHBoxLayout, QVBoxLayout, QGridLayout,
                             QLineEdit, QPushButton, QLabel, QTextEdit,
                             QMessageBox, QComboBox,
                             QAction, QSizePolicy, QToolTip, QApplication)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import *


class Window(QMainWindow):
    def __init__(self, parent=None):
        """ Initialisiere das Fenster """

        super().__init__(parent)
        self.Labels = {}
        self.Buttons = {}
        self.Layouts = {}
        self.Icons = {}
        self.OtherWidgets = {}
        self.Edits = {}

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.Menus = {}
        self.MenuActions = {}

        # Define colors
        self.color_green = '#5cb85c'
        self.color_red = '#d9534f'

        # Define icons
        self.Icons['exit'] = QIcon('res/img/ic_exit.png')
        self.Icons['add'] = QIcon('res/img/ic_add.png')

        # Toolbar / Menubar
        self.toolbar = self.addToolBar('Toolbar')
        self.menubar = self.menuBar()

        # Initialisiere die UI und den Mainloop
        self.init_window_ui()
        self.init_must_check()

    # Allgemeine UI-Funktionen
    def init_window_ui(self):

        # Definiere eine vorgefertigte Linie
        self.BorderLine = QLabel('<hr>')

        # Initialisiere vertikales Layout
        self.Layouts['vbox'] = QVBoxLayout()

        # Setze Layout für das Fenster
        self.widget.setLayout(self.Layouts['vbox'])

        # Set window size
        self.setGeometry(200, 150, 1000, 600)

    def finish_ui(self):

        # Add stretch
        self.Layouts['vbox'].addStretch()

        # Show window
        self.show()

        # Show ready message
        self.log_user('Bereit.')

    def make_button(self, text, icon='', action=None, height='full', color=''):
        """ Erstellt einen vordefinierten Button """
        button = QPushButton(text)
        if icon != '':
            button.setIcon(self.Icons[icon])
            button.setIconSize(QSize(50, 50))
        if action != None:
            button.clicked.connect(action)
        if height != 'full':
            button.setFixedHeight(height)
        else:
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if color != '':
            button.setStyleSheet('background-color:' + color + ';');
        return button

    def make_action(self, display_text, help_text, icon, shortcut, action):
        """ Erstellt eine Aktion für eine Toolbar oder ein Menü """
        t_action = action
        action = QAction(
            self.Icons[icon], display_text, self)
        action.setShortcut(shortcut)
        action.setStatusTip(help_text)
        action.triggered.connect(t_action)
        return action

    def log_user(self, message):
        self.statusBar().showMessage(message)

    def init_must_check(self):
        """ Initialisert einen 'Mainloop' """

        self.WindowMustCheckTimer = QTimer()
        self.WindowMustCheckTimer.timeout.connect(self.must_check)
        self.WindowMustCheckTimer.start(100)

    def must_check(self):
        """ Führt den Mainloop durch """

        self.WindowMustCheckTimer.start(100)
        self.updated_must_check()

    def updated_must_check(self):
        pass
