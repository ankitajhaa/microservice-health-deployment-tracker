from django.utils import timezone

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Incident, StatusHistory
from .serializers import IncidentSerializer

class IncidentViewSet(viewsets.ModelViewSet):

    serializer_class = IncidentSerializer
    queryset = Incident.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["post"])
    def resolve(self, request, pk=None):
        incident = self.get_object()

        old_status = incident.status

        incident.status = Incident.Status.RESOLVED
        incident.resolved_at = timezone.now()
        incident.save()

        StatusHistory.objects.create(
            incident=incident,
            old_status=old_status,
            new_status=Incident.Status.RESOLVED,
            changed_by=request.user,
        )

        return Response({"status": "incident resolved"})