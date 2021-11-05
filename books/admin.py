from django.contrib import admin
from .models import Category, Genre, Book, BookShots, Avtor, RatingStar, Rating, Reviews, Publishing, Country

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name", )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "draft", "year", )
    search_fields = ("title", )


# admin.site.register(Category, CategoryAdmin)

admin.site.register(Genre)
# admin.site.register(Book)
admin.site.register(BookShots)
admin.site.register(Avtor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
admin.site.register(Publishing)
admin.site.register(Country)


