from rest_framework import serializers

from .models import Service, Environment

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = [
            'id',
            'name',
            'description',
            'owner_team',
            'created_at',
            'is_active'
        ]
        read_only_fields = ['id', 'created_at']

class EnvironmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Environment
        fields = [
            'id',
            'name',
            'region',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']