from django.db import models


class AuthorCombination(models.Model):
    name = models.CharField(default='', max_length=200)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    shown_name = models.CharField(default='', max_length=50)
    real_name = models.CharField(default='', max_length=100, blank=True)

    def __str__(self):
        return self.shown_name


class Book(models.Model):
    title = models.CharField(default='', max_length=50)
    subtitle = models.CharField(default='', max_length=50, blank=True)
    description = models.TextField(default='', blank=True)
    authors = models.ForeignKey(
        AuthorCombination, related_name='published_books')
    publisher = models.ForeignKey(
        Publisher, related_name='published_books')
    isbn = models.CharField(default='', max_length=13, blank=True)
    barcode = models.CharField(default='', max_length=20, blank=True)
    has_own_barcode = models.BooleanField(default=False)

    def create_barcode(self):
        import lib.log

        self.barcode = log.gen_barcode(self.id)

    def __str__(self):
        return self.title
