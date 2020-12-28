from rest_framework import serializers
from shamseya_task.core.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    answer_ids = serializers.ListField()
    answer_count = serializers.IntegerField(min_value=0)

    class Meta:
        model = Review
        fields = ("submitted_at", "answer_ids", "answer_count")
