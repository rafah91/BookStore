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
            biography=fake.text(max_nb_chars=1000) ,
        )
    print(f'{n} authors was created successfully')

def add_books(n):
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg']
    for x in range(n):
        Book.objects.create(
            title = fake.text(max_nb_chars = 10) ,
            publication_date= fake.date() ,
            image= f"bookimages/{images[random.randint(0,6)]}",
            price= round(random.uniform(19.99,99.99),2) ,
            author = Author.objects.get(id=random.randint(1,50)),
        )
        
    print(f'{n} books was created successfully')



def add_reviews(n):
    fake = Faker()

    for x in range(n):
        Review.objects.create(
            viewer_name = User.objects.get(id=random.randint(1,5)),
            book = Book.objects.get(id=random.randint(1,1029)) , 
            rating = random.randint(1,5) , 
            content = fake.text(max_nb_chars=200)
        )

    print(f'{n} Reviews was created successfully')

#add_authors()
#add_books(18)
#add_reviews(3000)
