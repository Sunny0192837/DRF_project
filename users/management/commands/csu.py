from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Create superuser"

    def handle(self, *args, **kwargs):
        user = User.objects.create(email="aboba228@aboba.com")
        user.set_password("123qweasdzxc")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
