from django.urls import path
from .views import mydebug , BookList , BookDetail , AuthorList , AuthorDetail
from .api import   BookListAPI , BookDetailAPI , AuthorListAPI , AuthorDetailAPI

urlpatterns = [
    path('debug' , mydebug),
    path('' , BookList.as_view()) ,
    path('<slug:slug>', BookDetail.as_view()) ,

    path('author/', AuthorList.as_view()),
    path('author/<slug:slug>' , AuthorDetail.as_view()),

    # api
    path('api/list' , BookListAPI.as_view()),
    path('api/list/<int:pk>' , BookDetailAPI.as_view()),
    path('api/list/author' , AuthorListAPI.as_view()),
    path('api/list/author/<int:pk>' , AuthorDetailAPI.as_view()),
]