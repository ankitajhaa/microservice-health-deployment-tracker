from rest_framework import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .services import (
    most_unstable_service,
    calculate_mttr,
    deployment_reliability,
)

class MetricsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        unstable = most_unstable_service()
        mttr = calculate_mttr()
        reliability = deployment_reliability().values(
            "name", "failure_rate"
        )

        return Response({
            "most_unstable_service": unstable.name if unstable else None,
            "average_mttr": mttr["avg_mttr"],
            "deployment_reliability": list(reliability),
        })