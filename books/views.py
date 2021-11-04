from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
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

class AddReview(View):
    """Send Review"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        book = Book.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.book = book
            form.save()
        return redirect(book.get_absolute_url())



