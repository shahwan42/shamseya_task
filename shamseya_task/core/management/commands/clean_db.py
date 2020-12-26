from django.core.management.base import BaseCommand
from shamseya_task.core.models import Answer, Choice, Question, Review


class Command(BaseCommand):
    help = "Remove all model instances in the database"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Removing all Reviews"))
        Review.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Removing all Choices"))
        Choice.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Removing all Questions"))
        Question.objects.all().delete()

        self.stdout.write(
            self.style.SUCCESS(
                f"Now, db contains: {Review.objects.count()} Reviews, "
                f"{Choice.objects.count()} Choices, "
                f"{Question.objects.count()} Questions, and "
                f"{Answer.objects.count()} Answers"
            )
        )
