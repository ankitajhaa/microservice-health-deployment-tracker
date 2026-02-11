from rest_framework import serializers

from .models import Incident

class IncidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incident
        fields = [
            'service',
            'title',
            'description',
            'severity',
            'status',
            'created_at',
            'resolved_at',
        ]
        read_only_fields = ['created_at','resolved_at']