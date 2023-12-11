from django.contrib import admin
from .models import Author, Book , Review


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'tags', 'slug')
    search_fields = ['title', 'author', 'tags']
    list_filter = ['title', 'author', 'tags', 'slug']

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)