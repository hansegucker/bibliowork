import peewee

db = peewee.SqliteDatabase("data/data.db")


def update_db(tables):
    # Connect to DB
    db.connect()

    # Create tables
    db.create_tables(tables, safe=True)

    # Close connection
    db.close()


class AuthorCombination(peewee.Model):
    name = peewee.CharField()


class Publisher(peewee.Model):
    name = peewee.CharField()


# Create start data
update_db([AuthorCombination, Publisher])
undefined_authors = AuthorCombination.create(name='Unbekannt')
undefined_publisher = Publisher.create(name='Unbekannt')


class Book(peewee.Model):
    title = peewee.CharField(default='')
    subtitle = peewee.CharField(default='')
    description = peewee.TextField(default='')
    authors = peewee.ForeignKeyField(
        AuthorCombination, related_name='published_books', default=undefined_authors)
    publisher = peewee.ForeignKeyField(
        Publisher, related_name='published_books', default=undefined_publisher)
    isbn = peewee.CharField(default='')
    barcode = peewee.CharField(default='')
    has_barcode = peewee.BooleanField(default=False)

    def create_barcode(self):
        import lib.log

        self.barcode = log.gen_barcode(self.id)


update_db([Book])
