from django.urls import path

from shamseya_task.core.api import views

app_name = "core_api"

urlpatterns = [
    path("reviews/", views.ReviewApi.as_view(), name="review_list"),
]
