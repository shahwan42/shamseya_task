from shamseya_task.core.models import Answer, Review
from rest_framework import serializers


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id",)


class ReviewSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Review
        fields = ("id", "submitted_at", "answers")
