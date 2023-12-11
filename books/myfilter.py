from django_filters import rest_framework as filters
from .models import Book


class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact'],
            'price': ['lte', 'gte', 'range'],
            'slug': ['exact'],
            'author': ['exact'],
            'publication_date': ['exact'],
            
        }