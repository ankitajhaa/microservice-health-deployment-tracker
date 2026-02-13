class DeploymentApiTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@test.com", password="pass", name="Test"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

        self.svc = Service.objects.create(name="svc", owner_team="team")
        self.env = Environment.objects.create(name="DEV", region="IN")

    def test_create_deployment(self):
        payload = {
            "service": self.svc.id,
            "environment": self.env.id,
            "version": "v1",
            "status": "SUCCESS",
        }
        res = self.client.post("/api/deployments/", payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
