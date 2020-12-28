from collections import defaultdict
from datetime import datetime
from shamseya_task.core.api.permissions import IsSuperUser

from dateutil import parser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from shamseya_task.core.models import Review


class ReviewApi(APIView):
    """List of reviews and their answers, reviews are grouped by submitted_at date"""

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

        # reviews with answers
        qs = qs.prefetch_related("answers")

        it = qs.iterator()

        def shaped_dict():
            return {"count": 0, "answers": []}

        revs = defaultdict(shaped_dict)
        for review in it:
            review_date = str(review.submitted_at)
            revs[review_date].update(
                {
                    "answers": revs[review_date]["answers"]
                    + list(review.answers.values_list("id", flat=True)),
                    "count": revs[review_date]["count"] + 1,
                }
            )
        resp_data = revs
        return Response(resp_data)
