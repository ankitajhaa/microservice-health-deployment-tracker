from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Deployment
from .serializers import DeploymentSerializer

class DeploymentViewSet(viewsets.ModelViewSet):

    serializer_class = DeploymentSerializer
    queryset = Deployment.objects.all()
    permission_classes = [IsAuthenticated]