from django.contrib import admin

from .models import Author, Book


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # table 頁面顯示欄位
    list_display = ("id", "name", "birth_date")

    # 右側 filter Nav
    list_filter = ("name", "birth_date")

    # search bar
    search_fields = ("id", "name")

    ordering = ("id",)
    # readonly_fields = ("created",)
    filter_horizontal = ('books',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    # table 頁面顯示欄位
    list_display = ('title', 'author', 'is_published', 'price', 'publication_date')

    # 右側 filter Nav
    list_filter = ("is_published", "price")

    # search bar
    search_fields = ("title", "author__name")

    ordering = ("id",)
    # readonly_fields = ("created",)

    filter_horizontal = ('author2',)
