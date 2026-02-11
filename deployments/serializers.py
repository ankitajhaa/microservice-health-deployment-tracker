from rest_framework import serializers

from .models import Deployment

class DeploymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deployment
        fields = [
            'service',
            'environment',
            'version',
            'deployed_by',
            'deployed_at',
            'status'
        ]
        read_only_fields = ['deployed_at', 'deployed_by']