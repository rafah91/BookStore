from rest_framework import generics , filters
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.permissions import IsAuthenticated
from .serializers import BookListSerializer , BookDetailSerializer , AuthorListSerializer , AuthorDetailSerializer
from .models import Book , Author
from .mypagination import MyPagination
from .myfilter import BookFilter


class BookListAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['slug', 'name']
    search_fields = ['title', 'tags', 'publication_date']
    ordering_fields = ['price']
    filterset_class = BookFilter
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagination

class BookDetailAPI(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class AuthorListAPI(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer
    pagination_class = MyPagination

class AuthorDetailAPI(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer