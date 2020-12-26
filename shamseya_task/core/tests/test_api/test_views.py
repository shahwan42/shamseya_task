from django.test import tag
from django.urls import reverse
from rest_framework.test import APITestCase

from shamseya_task.core.tests.factories import ReviewFactory


@tag("reviewapi")
class ReviewApiTests(APITestCase):
    url = reverse("core_api:review_list")

    def setUpTestData():
        ReviewFactory.create_batch(20)

    def test_list_without_any_query_params(self):
        resp = self.client_class().get(self.url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get("count"), 20)

    def test_list_with_from_date_only(self):
        resp = self.client_class().get(f"{self.url}?from_date=2018-01-01")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get("count"), 20)

    def test_list_with_to_date_only(self):
        resp = self.client_class().get(f"{self.url}?to_date=2020-12-31")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get("count"), 20)

    def test_list_with_both_from_and_to_dates(self):
        resp = self.client_class().get(
            f"{self.url}?from_date=2018-01-01&to_date=2020-12-31"
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get("count"), 20)
