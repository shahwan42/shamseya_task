from datetime import datetime

from dateutil import parser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from shamseya_task.core.api.serializers import ReviewSerializer
from shamseya_task.core.models import Review


class ReviewApi(APIView):
    """List of reviews and their answers, reviews are grouped by submitted_at date"""

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get(self, request):
        from_date = self.request.query_params.get("from_date")
        to_date = self.request.query_params.get("to_date")

        qs = self.queryset

        if from_date:
            try:
                from_date = parser.parse(from_date)
            except parser.ParserError:
                return Response({"detail": "Invlaid from_date"}, status=400)

            qs = qs.filter(submitted_at__gte=datetime.date(from_date))

        if to_date:
            try:
                to_date = parser.parse(to_date)
            except parser.ParserError:
                return Response({"detail": "Invlaid to_date"}, status=400)

            qs = qs.filter(submitted_at__lte=datetime.date(to_date))

        # reviews with answers
        qs = qs.prefetch_related("answers")

        # response data shape should be like the follwing
        # resp = {
        #     "reviews": [
        #         {
        #             "submitted_at": "",
        #             "count": qs.count(),
        #             "answers": [answer.id for answer in qs],
        #         },
        #         ...,
        #     ]
        # }

        return Response(ReviewSerializer(qs, many=True).data)
