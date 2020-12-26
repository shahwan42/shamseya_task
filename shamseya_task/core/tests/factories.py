import datetime
import factory
import factory.fuzzy
from django.utils import timezone
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


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question


class AnswerFactory(DjangoModelFactory):
    class Meta:
        model = Answer
