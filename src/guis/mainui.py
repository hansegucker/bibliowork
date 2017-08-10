from guis.window import Window
from guis.bookui import BookUI


class MainUI(Window):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def handler_add_book(self):
        new_book_screen = BookUI(self)

    def init_ui(self):
        self.setWindowTitle('BiblioWork')

        # Actions
        self.MenuActions['exit'] = self.make_action(
            display_text='Programm beenden', help_text='Beendet \'BiblioWork\'.',
            icon='exit', action=self.close, shortcut='Ctrl+Q')
        self.MenuActions['add'] = self.make_action(
            display_text='Neues Buch hinzufügen', help_text='Fügt ein neues Buch zur Datenbank hinzu.',
            icon='add', action=self.handler_add_book, shortcut='Ctrl+N')

        # File menu
        self.Menus['file'] = self.menubar.addMenu('&Datei')
        self.Menus['file'].addAction(self.MenuActions['add'])
        self.Menus['file'].addAction(self.MenuActions['exit'])

        # Toolbar
        self.toolbar.addAction(self.MenuActions['add'])
        self.toolbar.addAction(self.MenuActions['exit'])

        self.finish_ui()
