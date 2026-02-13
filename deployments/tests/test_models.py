from django.test import TestCase
from django.contrib.auth import get_user_model
from services.models import Service, Environment
from deployments.models import Deployment


class DeploymentModelTests(TestCase):

    def test_create_deployment(self):
        user = get_user_model().objects.create_user(
            email="t@test.com", password="pass", name="T"
        )
        svc = Service.objects.create(name="svc", owner_team="team")
        env = Environment.objects.create(name="DEV", region="IN")

        dep = Deployment.objects.create(
            service=svc,
            environment=env,
            version="v1",
            status="SUCCESS",
            deployed_by=user
        )

        self.assertIn("v1", str(dep))
