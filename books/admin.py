from django.contrib import admin
from .models import Category, Genre, Book, BookShots, Avtor, RatingStar, Rating, Reviews

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookShots)
admin.site.register(Avtor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)


