# Python modules
import sys
from PyQt5.QtWidgets import QApplication

# Own modules
from lib.log import *
from lib.settings import Settings
from lib.dataapi import BookAPI

from guis.mainui import MainUI

if __name__ == '__main__':
    log("Start application...")

    # Init application
    app = QApplication(sys.argv)

    mainui = MainUI()

    sys.exit(app.exec_())
    log("'Start application' done.")
