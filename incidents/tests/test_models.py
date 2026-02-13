from django.test import TestCase
from services.models import Service
from incidents.models import Incident


class IncidentModelTests(TestCase):

    def test_create_incident(self):
        svc = Service.objects.create(name="svc", owner_team="team")
        incident = Incident.objects.create(
            service=svc,
            title="down",
            severity="HIGH",
            status="OPEN",
        )
        self.assertEqual(incident.status, "OPEN")
