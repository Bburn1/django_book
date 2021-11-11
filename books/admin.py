from django import forms
from django.contrib import admin

from django.utils.safestring import mark_safe


from .models import Category, Genre, Book, BookShots, Avtor, RatingStar, Rating, Reviews, Publishing, Country


from ckeditor_uploader.widgets import CKEditorUploadingWidget



class BookAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Book
        fields = '__all__'






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
    form = BookAdminForm
    readonly_fields = ("get_image", )
    fieldsets = (
        (None, {
            "fields": (("title", ), )
        }),
        (None, {
            "fields": (("description", ),)
        }),
        (None, {
            "fields": (("poster", "get_image",),)
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
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="100"')

    get_image.short_description = "Постер"



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
    list_display = ("name", "age", "get_image", )
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"




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

admin.site.site_title = "Digital Library"
admin.site.site_header = "Digital Library"


