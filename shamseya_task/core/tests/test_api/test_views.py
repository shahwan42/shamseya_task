from django.test import tag
from django.urls import reverse
from rest_framework.test import APITestCase

from shamseya_task.core.tests.factories import ReviewFactory
from shamseya_task.users.models import User


@tag("reviewapi")
class ReviewApiTests(APITestCase):
    url = reverse("core_api:review_list")

    def setUpTestData():
        ReviewFactory.create_batch(20)

    def setUp(self) -> None:
        self.client = self.client_class()
        self.user = User.objects.create_superuser(
            name="Ahmed Shahwan", username="ahmed"
        )

    def test_not_authenticated(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 403)

    def test_authenticated_not_admin(self):
        user = User.objects.create_user(username="ahmed2")
        self.client.force_login(user)
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 403)

    def test_authenticated_staff(self):
        user = User.objects.create_user(is_staff=True, username="ahmed2")
        self.client.force_login(user)
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_list_without_any_query_params(self):
        self.client.force_login(self.user)
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 20)

    def test_list_with_from_date_only(self):
        self.client.force_login(self.user)
        resp = self.client.get(f"{self.url}?from_date=2018-01-01")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 20)

    def test_list_with_to_date_only(self):
        self.client.force_login(self.user)
        resp = self.client.get(f"{self.url}?to_date=2020-12-31")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 20)

    def test_list_with_both_from_and_to_dates(self):
        self.client.force_login(self.user)
        resp = self.client.get(f"{self.url}?from_date=2018-01-01&to_date=2020-12-31")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 20)
