import datetime
import factory
import factory.fuzzy
from factory.django import DjangoModelFactory

from shamseya_task.core.models import Answer, Choice, Question, Review


class ReviewFactory(DjangoModelFactory):
    class Meta:
        model = Review

    submitted_at = factory.fuzzy.FuzzyDate(
        start_date=datetime.date(2018, 1, 1),
        end_date=datetime.date(2020, 12, 31),
    )


class ChoiceFactory(DjangoModelFactory):
    class Meta:
        model = Choice

    text = factory.fuzzy.FuzzyText(length=20)


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question

    text = factory.Faker("text")


class AnswerFactory(DjangoModelFactory):
    class Meta:
        model = Answer
