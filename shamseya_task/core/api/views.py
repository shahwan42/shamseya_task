from rest_framework.views import APIView
from rest_framework.response import Response

from shamseya_task.core.models import Review
from shamseya_task.core.api.serializers import ReviewSerializer


class ReviewApi(APIView):
    def get(self, request):
        qs = Review.objects.all()
        return Response(ReviewSerializer(qs, many=True).data)
