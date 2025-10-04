from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a demo user (idempotent) with username 'demo' and password 'demo1234'"

    def handle(self, *args, **options):
        User = get_user_model()
        username = "demo"
        password = "demo1234"
        email = "demo@example.com"

        user, created = User.objects.get_or_create(username=username, defaults={"email": email})
        if created:
            user.set_password(password)
            user.is_active = True
            user.save()
            self.stdout.write(self.style.SUCCESS("Created demo user 'demo' with password 'demo1234'"))
        else:
            # Ensure password is set to known value on each run (optional safety)
            user.set_password(password)
            user.is_active = True
            user.email = email
            user.save()
            self.stdout.write(self.style.WARNING("Demo user already exists; password reset to 'demo1234'"))