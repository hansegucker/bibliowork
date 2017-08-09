import peewee

db = peewee.SqliteDatabase("data.db")


class Author(peewee.Model):
    name = peewee.CharField()


class Book(peewee.Model):
    title = peewee.CharField()
    description = peewee.TextField()
    authors = peewee.ForeignKeyField(Author, related_name=published_books)


# Connect to DB
db.connect()

# Create tables
db.create_tables([Author, Book], safe=True)

# Close connection
db.close()
