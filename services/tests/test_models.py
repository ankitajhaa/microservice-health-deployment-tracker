from django.test import TestCase
from services.models import Service, Environment


class ModelTests(TestCase):

    def test_create_service(self):
        svc = Service.objects.create(
            name="payment",
            owner_team="fintech"
        )
        self.assertEqual(str(svc), "payment")

    def test_create_environment(self):
        env = Environment.objects.create(
            name="DEV",
            region="IN"
        )
        self.assertIn("DEV", str(env))
