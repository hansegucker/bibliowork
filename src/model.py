import peewee

db = peewee.SqliteDatabase("data/data.db")


class AuthorCombination(peewee.Model):
    name = peewee.CharField()


class Publisher(peewee.Model):
    name = peewee.CharField()


class Book(peewee.Model):
    title = peewee.CharField(default='')
    subtitle = peewee.CharField(default='')
    description = peewee.TextField(default='')
    authors = peewee.ForeignKeyField(
        AuthorCombination, related_name='published_books')
    publisher = peewee.ForeignKeyField(
        Publisher, related_name='published_books')
    isbn = peewee.IntegerField(default='0')
    barcode = peewee.IntegerField(default='0')
    has_barcode = peewee.BooleanField(default=False)

    def create_barcode(self):
        import lib.log

        self.barcode = log.gen_barcode(self.id)


# Connect to DB
db.connect()

# Create tables
db.create_tables([AuthorCombination, Publisher, Book], safe=True)

# Close connection
db.close()
