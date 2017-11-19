from django.contrib import admin

# Register your models here.
from .models import AuthorCombination, Publisher, Book

to_register = [AuthorCombination, Publisher, Book]

for i in to_register:
    admin.site.register(i)
