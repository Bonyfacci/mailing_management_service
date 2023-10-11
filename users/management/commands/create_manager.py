from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='manager@sky.com',
            first_name='manager',
            last_name='manager',
            is_staff=True,
            is_superuser=False)
        user.set_password('qwert12345')
        user.save()
