from django.shortcuts import render
from django.db.models.query import QuerySet
from django.views import generic
from .models import Book , Author , Review


def mydebug(request):
    data = Book.objects.select_related('author').all()
    return render(request,'books/debug.html',{'data':data})


class BookList(generic.ListView):
    model = Book
    paginate_by = 50



class BookDetail(generic.DetailView):
    model = Book
    template_name = 'books/books_detail.html'

    def get_queryset(self):
        author = Book.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset().filter(book=Book)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(Book=self.get_object())
        return context


class AuthorList(generic.ListView):
    model = Author
    paginate_by = 50


class AuthorDetail(generic.ListView):
    model = Book
    template_name = 'books/author_detail.html'


    def get_queryset(self):
        author = Author.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset().filter(author=Author)
        return queryset
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = Author.objects.get(slug=self.kwargs['slug'])
        return context