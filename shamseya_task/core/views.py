import datetime
from shamseya_task.core.models import Review
from django.shortcuts import render


def home(request):
    all_count = Review.objects.count()
    second_count = Review.objects.filter(
        submitted_at__gte=datetime.date(2020, 12, 31)
    ).count()
    third_count = Review.objects.filter(
        submitted_at__lte=datetime.date(2018, 1, 1)
    ).count()
    fourth_count = (
        Review.objects.filter(submitted_at__gte=datetime.date(2018, 1, 1))
        .filter(submitted_at__lte=datetime.date(2018, 2, 1))
        .count()
    )
    fifth_count = (
        Review.objects.filter(submitted_at__gte=datetime.date(2018, 3, 1))
        .filter(submitted_at__lte=datetime.date(2019, 2, 1))
        .count()
    )

    return render(
        request,
        "core/home.html",
        {
            "all_count": all_count,
            "second_count": second_count,
            "third_count": third_count,
            "fourth_count": fourth_count,
            "fifth_count": fifth_count,
        },
    )
