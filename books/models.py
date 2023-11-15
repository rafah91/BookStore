from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date=models.DateField()
    biography=models.TextField(max_length=20000)
    slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)
    
    
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey('Author',related_name='book_author',on_delete=models.SET_NULL,null=True,blank=True)
    publication_date=models.DateField()
    image=models.ImageField(upload_to='bookimages')
    price=models.FloatField()
    tags = TaggableManager()
    slug = models.SlugField(null=True,blank=True)
    
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)
    
class Review(models.Model):
    book=models.ForeignKey(Book,related_name='book_review',on_delete=models.CASCADE)
    viewer_name=models.ForeignKey(User,related_name='review_author',on_delete=models.SET_NULL,null=True,blank=True)
    created_at=models.DateTimeField(default=timezone.now)
    content=models.TextField(max_length=600)
    rating=models.IntegerField()
    
    def __str__(self):
        return str(self.viewer_name)
    
    
    