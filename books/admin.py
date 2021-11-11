from django.contrib import admin
from .models import Category, Genre, Book, BookShots, Avtor, RatingStar, Rating, Reviews, Publishing, Country

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("id", "name", "url")
    list_display_links = ("name", )


class ReviewInline(admin.TabularInline):
    """Отзывы на странице"""
    model = Reviews
    extra = 0
    readonly_fields = ("name", "email",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Книги"""
    list_display = ("title", "category",  "url", "draft",)
    list_filter = ("category", "draft", "year", )
    search_fields = ("title", )
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft", )
    fieldsets = (
        (None, {
            "fields": (("title", ), )
        }),
        (None, {
            "fields": (("description", "poster",),)
        }),
        (None, {
            "fields": (("countrys", "language", ),)
        }),
        (None, {
            "fields": (("year", "world_publishing",),)
        }),
        (None, {
            "fields": (("isbn", "pages",),)
        }),
        (None, {
            "fields": (("avtors", "publishings", "genres", "category", ),)
        }),
        ("Options", {
            "fields": (("url", "draft",),)
        }),




    )

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("name", "email", "parent", "book", "id")
    readonly_fields = ("name", "email", )

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ("name", "url")

@admin.register(Avtor)
class ActorAdmin(admin.ModelAdmin):
    """Авторы"""
    list_display = ("name", "age")

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "ip")

@admin.register(BookShots)
class BookShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ("title", "book")

@admin.register(Publishing)
class PublishingAdmin(admin.ModelAdmin):

    list_display = ("name", "image", )

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):

    list_display = ("name", "image", )








# admin.site.register(Category, CategoryAdmin)

#admin.site.register(Genre)
# admin.site.register(Book)
#admin.site.register(BookShots)
#admin.site.register(Avtor)
#admin.site.register(Rating)
admin.site.register(RatingStar)
#admin.site.register(Reviews)
#admin.site.register(Publishing)
#admin.site.register(Country)


