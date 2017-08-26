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

    def register_edit(self, edit_id, title, pos_y, big=False, editable=True):
        # Add title label for edit
        self.Labels[edit_id] = QLabel(title)

        # More than one line
        if big:
            self.Edits[edit_id] = QTextEdit()
        else:
            self.Edits[edit_id] = QLineEdit()

        # Read only
        if editable == False:
            self.Edits[edit_id].setReadOnly(True)

        # Add to layout
        self.Layouts['edit_grid'].addWidget(self.Labels[edit_id], pos_y, 0)
        self.Layouts['edit_grid'].addWidget(self.Edits[edit_id], pos_y, 1)

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
        self.register_edit(
            'description', title='Beschreibung', pos_y=6, big=True)

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
        self.register_edit('id', title='Datenbank-ID',
                           pos_y=10, editable=False)

        # Barcode
        self.register_edit('barcode', title='EAN-13-Barcode',
                           pos_y=11, editable=False)

        # Load data
        self.update_data()

        # Finish layout and UI
        self.Layouts['vbox'].addLayout(self.Layouts['edit_grid'])
        self.finish_ui()

    def save_data(self):
        pass

    def update_data(self):
        edit_cons = {
            'isbn': self.book.isbn,
            'title': self.book.title,
            'subtitle': self.book.subtitle,
            'description': self.book.description,
            'id': str(self.book.id),
            'barcode': self.book.barcode
        }
        for key, value in edit_cons.items():
            self.Edits[key].setText(value)

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
