import peewee

db = peewee.SqliteDatabase("data/data.db")


class AuthorCombination(peewee.Model):
    name = peewee.CharField()


class Publisher(peewee.Model):
    name = peewee.CharField()


class Book(peewee.Model):
    title = peewee.CharField()
    subtitle = peewee.CharField()
    description = peewee.TextField()
    authors = peewee.ForeignKeyField(
        AuthorCombination, related_name=published_books)
    publisher = peewee.ForeignKeyField(Publisher, related_name=published_books)
    isbn = peewee.IntegerField()
    barcode = peewee.IntegerField()
    has_barcode = peewee.BooleanField()


# Connect to DB
db.connect()

# Create tables
db.create_tables([Author, Book], safe=True)

# Close connection
db.close()
