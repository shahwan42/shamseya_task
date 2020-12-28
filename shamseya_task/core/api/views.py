from collections import defaultdict
from datetime import datetime
from shamseya_task.core.api.serializers import ReviewSerializer

from django.db.models.aggregates import Count
from shamseya_task.core.api.permissions import IsSuperUser
from django.contrib.postgres.aggregates import ArrayAgg
from dateutil import parser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from shamseya_task.core.models import Review


class ReviewApi(APIView):
    """List of reviews and their answers, reviews are grouped by submitted_at date"""

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsSuperUser)

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

        # reviews with answer_ids and answer_count
        qs = qs.prefetch_related("answers").annotate(
            answer_ids=ArrayAgg("answers"), answer_count=Count("answers")
        )
        it = qs.iterator()

        def shaped_dict():
            return {"count": 0, "answer_count": 0, "answer_ids": []}

        revs = defaultdict(shaped_dict)
        for review in it:
            review_date = str(review.submitted_at)
            revs[review_date].update(
                {
                    "count": revs[review_date]["count"] + 1,
                    "answer_count": revs[review_date]["answer_count"]
                    + review.answer_count,
                    "answer_ids": revs[review_date]["answer_ids"] + review.answer_ids,
                }
            )
        resp_data = revs
        # resp_data = self.serializer_class(qs, many=True).data
        return Response(resp_data)
