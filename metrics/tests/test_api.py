class MetricsApiTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@test.com", password="pass", name="Test"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_metrics_endpoint(self):
        res = self.client.get("/api/metrics/")
        self.assertEqual(res.status_code, 200)
