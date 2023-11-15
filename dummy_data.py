import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()

from faker import Faker
import random
from django.contrib.auth.models import User 
from books.models import Author , Book , Review


def add_authors(n):
    fake = Faker()

    for x in range(n):
        Author.objects.create(
            name = fake.name() ,
            birth_date=fake.date() ,
            biography=fake.text() ,
        )
    print(f'{n} authors was created successfully')

#def add_books(n):
    #fake = Faker()

    #for x in range(n):
        #Book.objects.create(
            #n
        #)

add_authors(50)
