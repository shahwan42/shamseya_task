from rest_framework import serializers

from shamseya_task.core.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ("submitted_at", "answers")

    def get_answers(self, obj):
        return obj.answers.values_list("id", flat=True)
