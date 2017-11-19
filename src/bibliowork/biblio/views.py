from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book
# Create your views here.


def index(request):
    books = Book.objects.order_by('title')
    context = {'books': books}
    return render(request, 'book/index.html', context)


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'book': book}
    return render(request, 'book/detail.html', context)


def edit(request, book_id):
    return HttpResponse("EDIT BOOK")


def save(request, book_id):
    return HttpResponse("SAVED")
