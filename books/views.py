from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Book


class BookView(ListView):
    """Список книг"""
    model = Book
    queryset = Book.objects.filter(draft=False)
    #template_name = "books/book_list.html"


class BookDetailView(DetailView):
    """Страница с отображением книги"""
    model = Book
    slug_field = "url"



