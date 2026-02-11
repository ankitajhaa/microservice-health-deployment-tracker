from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    owner_team = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Environment(models.Model):

    class environ_name(models.TextChoices):
        DEV = "DEV"
        STAGING = "STAGING"
        PROD = "PROD"
    
    name = models.CharField(max_length=10, choices=environ_name.choices)
    region = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.region}"