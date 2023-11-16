from rest_framework import serializers
from .models import Author, Book, Review
from django.db.models.aggregates import Avg

class BooktReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookListSerializer(serializers.ModelSerializer):
    book_count = serializers.SerializerMethodField()
    author = AuthorListSerializer(read_only=True)
    review_count = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()
    avg_rating2 = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_book_count(self, object):
        book_count = object.author.books.count() if object.author else 0
        return book_count
    
    def get_review_count(self, object):
        review_count = object.books_review.all().count()
        return review_count

    def get_avg_rating(self, object):
        total = 0
        reviews = object.books_review.all()
        for r in reviews:
            total += r.rating
        if len(reviews) > 0:
            return round(total / len(reviews), 2)
        else:
            return 0

    def get_avg_rating2(self, object):
        avg = object.books_review.aggregate(rating_avg=Avg('rating'))
        return round(avg['rating_avg'], 2) if avg['rating_avg'] else 0

class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorListSerializer(read_only=True)
    review_count = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()
    books_review = BooktReviewSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

    def get_review_count(self, object):
        review_count = object.books_review.all().count()
        return review_count

    def get_avg_rating(self, object):
        avg = object.books_review.aggregate(rating_avg=Avg('rating'))
        return round(avg['rating_avg'], 2) if avg['rating_avg'] else 0

    def get_book_review(self, object):
        book_review = object.books_review.all()
        return BooktReviewSerializer(book_review, many=True).data

class AuthorDetailSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    books_review = BookListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = '__all__'

    