from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.


def index(request):
    books = Book.objects.order_by('title')
    context = {'books': books}
    return render(request, 'book/index.html', context)


def detail(request, book_id):
    return HttpResponse("SHOW BOOK")


def edit(request, book_id):
    return HttpResponse("EDIT BOOK")
