from guis.window import *


class BookUI(Window):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Buch bearbeiten | BiblioWork')

        self.Layouts["edit_grid"] = QGridLayout()
        self.Layouts["edit_grid"].setSpacing(10)

        self.Labels['title'] = QLabel('Titel')
        self.Edits['title'] = QLineEdit()
        self.Layouts["edit_grid"].addWidget(self.Labels['title'], 1, 0)
        self.Layouts["edit_grid"].addWidget(self.Edits['title'], 1, 1)

        self.Labels['thumbnail'] = QLabel()
        self.Labels['thumbnail'].setScaledContents(True)
        self.Labels['thumbnail'].setFixedSize(200, 300)
        self.load_thumbnail('res/img/placeholder.jpg')
        self.Layouts["edit_grid"].addWidget(
            self.Labels['thumbnail'], 1, 2, 15, 1)

        self.Labels['subtitle'] = QLabel('Untertitel')
        self.Edits['subtitle'] = QLineEdit()
        self.Layouts["edit_grid"].addWidget(self.Labels['subtitle'], 2, 0)
        self.Layouts["edit_grid"].addWidget(self.Edits['subtitle'], 2, 1)

        self.Layouts["vbox"].addLayout(self.Layouts["edit_grid"])
        self.finish_ui()

    def load_thumbnail(self, file_name):
        pixmap = QPixmap(file_name)
        self.Labels['thumbnail'].setPixmap(pixmap)

    def load_book(self, book_id):
        import model

        self.book = model.Book.get().where(model.Book.id == book_id)

    def update_book(self):
        pass

    def load_new_book(self):
        import model

        self.book = model.Book()
