from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Book, Category




class BookView(ListView):
    """Список книг"""
    model = Book
    queryset = Book.objects.filter(draft=False)
    #template_name = "books/book_list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context


class BookDetailView(DetailView):
    """Страница с отображением книги"""
    model = Book
    slug_field = "url"

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context

class AddReview(View):
    """Send Review"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        book = Book.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.book = book
            form.save()
        return redirect(book.get_absolute_url())



