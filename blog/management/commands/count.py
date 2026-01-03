from django.core.management.base import BaseCommand, CommandError
from blog.models import Post

class Command(BaseCommand):
    help = 'Prints the count of MyModel instances'

    def handle(self, *args, **options):
        try:
            count = Post.objects.count()
            self.stdout.write(f'There are {count} instances of MyModel.')
        except Exception as e:
            raise CommandError(f'An error occurred: {e}')