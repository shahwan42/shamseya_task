from shamseya_task.core.models import Answer, Choice, Question, Review
from rest_framework import serializers


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "text")


class QuestionSerializer(serializers.ModelSerializer):
    # choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ("id", "text")  # , "choices")


class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    choice = ChoiceSerializer()

    class Meta:
        model = Answer
        fields = ("id", "question", "choice")


class ReviewSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Review
        fields = ("id", "submitted_at", "answers")
