from collections import defaultdict
from datetime import datetime

from dateutil import parser
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from shamseya_task.core.api.serializers import ReviewSerializer
from shamseya_task.core.models import Review


class ReviewApi(generics.ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
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

        qs = qs.prefetch_related("answers")
        return qs

    def get_paginated_response(self, data):
        assert self.paginator is not None
        revs = defaultdict(list)

        # Merge reviews that have similar dates
        for entry in data:
            revs[entry["submitted_at"]].append({"answers": entry["answers"]})

        return self.paginator.get_paginated_response(revs)
