from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from services.models import Service


class ServiceApiTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@test.com", password="pass", name="Test"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_list_services(self):
        Service.objects.create(name="svc", owner_team="team")
        res = self.client.get("/api/services/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
