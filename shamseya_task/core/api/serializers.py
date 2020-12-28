from rest_framework import serializers

from shamseya_task.core.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ("submitted_at", "count", "answers")

    def get_answers(self, obj):
        return {
            "count": obj.answers.count(),
            "ids": obj.answers.values_list("id", flat=True),
        }

    def get_count(self, obj):
        return Review.objects.filter(submitted_at=obj.submitted_at).count()
