from django.shortcuts import render
from django.views.generic.base import View

from .models import Book


class BookView(View):
    """Список книг"""
    def get(self, request):
        books = Book.objects.all()
        return render(request, "books/books.html", {"book_list": books})

class BookDetailView(View):
    """Страница с отображением книги"""
    def get(self, request, slug):
        book = Book.objects.get(url=slug)
        return render(request, "books/book_detail.html", {"book": book})



