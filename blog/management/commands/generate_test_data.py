
from django.core.management.base import BaseCommand
from blog.models import Post
from faker import Faker
import random
from django.contrib.auth.models import User
# Create your views here.

class Command(BaseCommand):
    help = 'Generate test data using Faker'

    def handle(self, *args, **kwargs):
        fake = Faker()
        authors = User.objects.all()
        
    
        for _ in range(10):  
            random_author = random.choice(authors)   
            Post.objects.create(
                title=fake.name(),
                content=fake.name(),
                published_at=fake.date_time(),
                author=random_author,)
        self.stdout.write(self.style.SUCCESS('Successfully generated test data'))
                