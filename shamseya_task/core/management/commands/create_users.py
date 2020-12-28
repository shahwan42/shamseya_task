from django.core.management.base import BaseCommand

from shamseya_task.users.models import User


class Command(BaseCommand):
    help = "Create Superuser, staff user, and an active regular user"

    def handle(self, *args, **options):
        test_pass = "Awesome1"

        self.stdout.write(self.style.SUCCESS("Creating super_user"))
        super_user, created = User.objects.get_or_create(
            username="super_user", is_staff=True, is_superuser=True
        )
        if created:
            super_user.set_password(test_pass)
            super_user.save()

        self.stdout.write(self.style.SUCCESS("Creating super_only"))
        super_user, created = User.objects.get_or_create(
            username="super_only", is_superuser=True
        )
        if created:
            super_user.set_password(test_pass)
            super_user.save()

        self.stdout.write(self.style.SUCCESS("Creating staff_user"))
        staff_user, created = User.objects.get_or_create(
            username="staff_user", is_staff=True
        )
        if created:
            staff_user.set_password(test_pass)
            staff_user.save()

        self.stdout.write(self.style.SUCCESS("Creating active_user"))
        active_user, created = User.objects.get_or_create(username="active_user")
        if created:
            active_user.set_password(test_pass)
            active_user.save()

        self.stdout.write(
            self.style.SUCCESS(f"{[u.username for u in User.objects.all()]}")
        )
        self.stdout.write(self.style.SUCCESS("Done."))
