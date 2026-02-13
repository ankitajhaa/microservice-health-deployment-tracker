from django.test import TestCase
from metrics.services import most_unstable_service


class MetricsLogicTests(TestCase):

    def test_unstable_service_runs(self):
        result = most_unstable_service()
        self.assertIsNotNone(result)  # or None acceptable
