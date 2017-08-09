# Python modules
import sys

# Own modules
from lib.log import *s
from lib.settings import Settings
from lib.window import Window
from lib.dataapi import BookAPI
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    log("Start application...")

    # Init application
    app = QApplication(sys.argv)

    sys.exit(app.exec_())
    log("'Start application' done.")
