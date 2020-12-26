import random

from django.core.management.base import BaseCommand
from shamseya_task.core.models import Answer, Choice, Question, Review
from shamseya_task.core.tests.factories import (
    ReviewFactory,
    ChoiceFactory,
    QuestionFactory,
    AnswerFactory,
)


class Command(BaseCommand):
    help = "Populate Database"

    def handle(self, *args, **options):

        q1_ch1 = ChoiceFactory()
        q1_ch2 = ChoiceFactory()
        q1 = QuestionFactory()
        q1.choices.set([q1_ch1, q1_ch2])
        self.stdout.write(self.style.SUCCESS("Q1 and its choices"))

        q2_ch1 = ChoiceFactory()
        q2_ch2 = ChoiceFactory()
        q2 = QuestionFactory()
        q2.choices.set([q2_ch1, q2_ch2])
        self.stdout.write(self.style.SUCCESS("Q2 and its choices"))

        q3_ch1 = ChoiceFactory()
        q3_ch2 = ChoiceFactory()
        q3 = QuestionFactory()
        q3.choices.set([q3_ch1, q3_ch2])
        self.stdout.write(self.style.SUCCESS("Q3 and its choices"))

        q4_ch1 = ChoiceFactory()
        q4_ch2 = ChoiceFactory()
        q4 = QuestionFactory()
        q4.choices.set([q4_ch1, q4_ch2])
        self.stdout.write(self.style.SUCCESS("Q4 and its choices"))

        reviews = ReviewFactory.create_batch(4000)
        self.stdout.write(self.style.SUCCESS("Created 4000 Reviews"))

        for review in reviews:
            self.stdout.write(
                self.style.SUCCESS(f"Creating Answers for review {review.id}")
            )
            for _ in range(4):
                random_q = random.choice([q1, q2, q3, q4])
                random_ch = random.choice(random_q.choices.all())
                AnswerFactory(review=review, question=random_q, choice=random_ch)
        self.stdout.write(self.style.SUCCESS("Created 10 Answers for each Review"))

        self.stdout.write(
            self.style.SUCCESS(
                f"Now, db contains: {Review.objects.count()} Reviews, "
                f"{Choice.objects.count()} Choices, "
                f"{Question.objects.count()} Questions, and "
                f"{Answer.objects.count()} Answers"
            )
        )
