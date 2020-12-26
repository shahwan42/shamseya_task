import factory
from shamseya_task.core.models import Answer, Choice, Question, Review


class ReviewFactory(factory.Factory):
    class Meta:
        model = Review


class ChoiceFactory(factory.Factory):
    class Meta:
        model = Choice


class QuestionFactory(factory.Factory):
    class Meta:
        model = Question


class AnswerFactory(factory.Factory):
    class Meta:
        model = Answer
