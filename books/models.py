from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Author(models.Model):
    name = models.CharField(_('Name'),max_length=100)
    birth_date=models.DateField(_('Birth date'))
    biography=models.TextField(_('Biography'),max_length=20000)
    slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)
    
    
class Book(models.Model):
    title=models.CharField(_('Title'),max_length=200)
    author=models.ForeignKey('Author',verbose_name=_('Author'),related_name='book_author',on_delete=models.SET_NULL,null=True,blank=True)
    publication_date=models.DateField(_('Puplication date'))
    image=models.ImageField(_('Image'),upload_to='bookimages')
    price=models.FloatField(_('Price'),)
    tags = TaggableManager()
    slug = models.SlugField(null=True,blank=True)
    
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)
    
class Review(models.Model):
    book=models.ForeignKey(Book,verbose_name=_('Book'),related_name='book_review',on_delete=models.CASCADE)
    viewer_name=models.ForeignKey(User,verbose_name=_('Viewer name'),related_name='review_author',on_delete=models.SET_NULL,null=True,blank=True)
    created_at=models.DateTimeField(_('Created at'),default=timezone.now)
    content=models.TextField(_('Content'),max_length=600)
    rating=models.IntegerField(_('Rating'))
    
    def __str__(self):
        return str(self.viewer_name)
    
    
    