from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Service, Environment
from .serializers import ServiceSerializer, EnvironmentSerializer

# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):

    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticated]
    
class EnvironmentViewSet(viewsets.ModelViewSet):

    serializer_class = EnvironmentSerializer
    queryset = Environment.objects.all()
    permission_classes = [IsAuthenticated]