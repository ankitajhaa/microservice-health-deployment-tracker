class IncidentApiTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@test.com", password="pass", name="Test"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.svc = Service.objects.create(name="svc", owner_team="team")

    def test_resolve_incident(self):
        incident = Incident.objects.create(
            service=self.svc,
            title="down",
            severity="HIGH",
            status="OPEN",
        )

        res = self.client.post(f"/api/incidents/{incident.id}/resolve/")
        incident.refresh_from_db()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(incident.status, "RESOLVED")
