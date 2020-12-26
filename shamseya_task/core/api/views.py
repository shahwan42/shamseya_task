from datetime import datetime
from dateutil import parser

from rest_framework.views import APIView
from rest_framework.response import Response

from shamseya_task.core.models import Review
from shamseya_task.core.api.serializers import ReviewSerializer


class ReviewApi(APIView):
    queryset = Review.objects.all()

    def get(self, request):
        from_date = request.query_params.get("from_date")
        to_date = request.query_params.get("to_date")

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

        count = qs.count()
        qs = qs.prefetch_related("answers")

        return Response(
            {
                "count": count,
                "reviews": ReviewSerializer(qs, many=True).data,
            }
        )
