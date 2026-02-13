from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model


def test_create_environment():
    user = get_user_model().objects.create_user(
        email="test@test.com", password="pass123", name="Test"
    )
    client = APIClient()
    client.force_authenticate(user)

    payload = {
        "name": "DEV",
        "region": "IN"
    }

    res = client.post("/api/environments/", payload)

    assert res.status_code == status.HTTP_201_CREATED
