from guis.window import Window


class MainUI(Window):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('BiblioWork')

        self.finish_ui()
