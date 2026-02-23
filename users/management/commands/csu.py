from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    """Команда для создания суперпользователя"""

    def handle(self, *args, **options):
        user = User(
            username="admin",
            email="",
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password("admin")
        user.save()
