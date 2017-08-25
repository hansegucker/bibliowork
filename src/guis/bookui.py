from guis.window import *


class BookUI(Window):

    def __init__(self, parent=None, new_book=False, book_id=0):
        super().__init__(parent)
        if (new_book):
            self.load_new_book()
        else:
            self.load_book(book_id=book_id)
        self.init_ui()

    def get_data_from_edit(edit_id):
        return self.Edits[edit_id].Text()

    def register_edit(self, edit_id, title, pos_y, big=False, db_con=None):
        self.Labels[edit_id] = QLabel(title)
        if big:
            self.Edits[edit_id] = QTextEdit()
        else:
            self.Edits[edit_id] = QLineEdit()
        self.Layouts['edit_grid'].addWidget(self.Labels[edit_id], pos_y, 0)
        self.Layouts['edit_grid'].addWidget(self.Edits[edit_id], pos_y, 1)

        # DB connection
        self.EditDBCons[edit_id] = db_con

    def init_ui(self):
        # Make list for db connections
        self.EditDBCons = {}

        # Set window title
        self.setWindowTitle('Buch bearbeiten | BiblioWork')

        # Grid layout
        self.Layouts['edit_grid'] = QGridLayout()
        self.Layouts['edit_grid'].setSpacing(10)

        # ISBN
        self.register_edit('isbn', title='ISBN', pos_y=0)

        # Title
        self.register_edit('title', title='Titel', pos_y=1)

        # Thumbnail
        self.Labels['thumbnail'] = QLabel()
        self.Labels['thumbnail'].setScaledContents(True)
        self.Labels['thumbnail'].setFixedSize(200, 300)
        self.load_thumbnail('res/img/placeholder.jpg')
        self.Layouts['edit_grid'].addWidget(
            self.Labels['thumbnail'], 1, 2, 15, 1)

        # Subtitle
        self.register_edit('subtitle', title='Untertitel', pos_y=2)

        ###########
        # Authors #
        ###########

        self.Labels['authors'] = QLabel('Bestehende(r) Autor(en)')
        self.OtherWidgets['authors'] = QComboBox()
        self.OtherWidgets['authors'].addItems(['Unbekannt', 'mehrere Autoren'])
        self.Layouts['edit_grid'].addWidget(self.Labels['authors'], 3, 0)
        self.Layouts['edit_grid'].addWidget(self.OtherWidgets['authors'], 3, 1)

        self.Labels['authors_or_new_authors'] = QLabel('- oder -')
        self.Layouts['edit_grid'].addWidget(
            self.Labels['authors_or_new_authors'], 4, 1)

        self.Labels['new_authors'] = QLabel('Neue(r) Autor(en)')
        self.Edits['new_authors'] = QLineEdit()
        self.Layouts['edit_grid'].addWidget(self.Labels['new_authors'], 5, 0)
        self.Layouts['edit_grid'].addWidget(self.Edits['new_authors'], 5, 1)

        #######
        #######

        # Description
        self.Labels['description'] = QLabel('Beschreibung')
        self.Edits['description'] = QTextEdit()
        self.Layouts['edit_grid'].addWidget(
            self.Labels['description'], 6, 0)
        self.Layouts['edit_grid'].addWidget(
            self.Edits['description'], 6, 1)

        #############
        # Publisher #
        #############

        self.Labels['publisher'] = QLabel('Bestehender Verlag')
        self.OtherWidgets['publisher'] = QComboBox()
        self.OtherWidgets['publisher'].addItems(
            ['Unbekannt', 'mehrere Verlage'])
        self.Layouts['edit_grid'].addWidget(self.Labels['publisher'], 7, 0)
        self.Layouts['edit_grid'].addWidget(
            self.OtherWidgets['publisher'], 7, 1)

        self.Labels['publisher_or_new_publisher'] = QLabel('- oder -')
        self.Layouts['edit_grid'].addWidget(
            self.Labels['publisher_or_new_publisher'], 8, 1)

        self.Labels['new_publisher'] = QLabel('Neuer Verlag')
        self.Edits['new_publisher'] = QLineEdit()
        self.Layouts['edit_grid'].addWidget(self.Labels['new_publisher'], 9, 0)
        self.Layouts['edit_grid'].addWidget(self.Edits['new_publisher'], 9, 1)

        ######
        ######

        # ID
        self.Labels['id'] = QLabel('Datenbank-ID')
        self.Edits['id'] = QLineEdit()
        self.Edits['id'].setReadOnly(True)
        self.Layouts['edit_grid'].addWidget(self.Labels['id'], 10, 0)
        self.Layouts['edit_grid'].addWidget(self.Edits['id'], 10, 1)

        # Barcode
        self.Labels['barcode'] = QLabel('EAN-13-Barcode')
        self.Edits['barcode'] = QLineEdit()
        self.Edits['barcode'].setReadOnly(True)
        self.Layouts['edit_grid'].addWidget(self.Labels['barcode'], 11, 0)
        self.Layouts['edit_grid'].addWidget(self.Edits['barcode'], 11, 1)

        # Load data
        self.update_data()

        # Finish layout and UI
        self.Layouts['vbox'].addLayout(self.Layouts['edit_grid'])
        self.finish_ui()

    def save_data(self):
        pass

    def update_data(self):
        self.Edits['isbn'].setText(self.book.isbn)
        self.Edits['title'].setText(self.book.title)
        self.Edits['subtitle'].setText(self.book.subtitle)
        self.Edits['description'].setText(self.book.description)
        self.Edits['id'].setText(str(self.book.id))
        self.Edits['barcode'].setText(self.book.barcode)

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
        self.book.save()
