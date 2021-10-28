from django.shortcuts import render
from django.views import View

from .models import Book


class BookView(View):
    """Список книг"""
    def get(self, request):
        books = Book.objects.all()
        return render(request, "books/books.html", {"book_list": books})



