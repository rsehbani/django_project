from django.core.management.base import BaseCommand
from blog.models import Post
from django.contrib.auth.models import User
 

class Command(BaseCommand):

    help = "Create a new post"

    def add_arguments(self, parser):

        # Add options for name and email

        parser.add_argument('--title', type=str, help='Name of the doctor')

        parser.add_argument('--author', type=User, help='Email of the doctor')

 
    def handle(self, *args, **options):

        # If name and email are provided via options

        title = options['title']

        author = options['author']

        if not title:

            title = input("title of post: ")

        if not author:

            author = User(input("author of post: "))

 

        # Create the doctor in the database

        Post.objects.create(title=title, author=author)

 

        # Output a success message

        self.stdout.write(self.style.SUCCESS(f"Doctor '{title}' created successfully"))

