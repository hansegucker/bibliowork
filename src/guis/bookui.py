from guis.window import Window
from PyQt5.QtWidgets import QGridLayout


class BookUI(Window):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Buch bearbeiten | BiblioWork')

        self.Layouts["edit_grid"] = QGridLayout()

        self.finish_ui()
