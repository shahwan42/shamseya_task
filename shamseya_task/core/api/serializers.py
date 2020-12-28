from rest_framework import serializers

from shamseya_task.core.models import Answer, Review


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id",)


class ReviewSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Review
        fields = ("submitted_at", "answers")
