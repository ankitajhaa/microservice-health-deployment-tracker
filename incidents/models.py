from django.db import models
from django.conf import settings
# Create your models here.

class Incident(models.Model):

    service = models.ForeignKey(
        "services.Service",
        on_delete=models.CASCADE,
        related_name="incidents"
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Severity(models.TextChoices):
        LOW = "LOW"
        MEDIUM = "MEDIUM"
        HIGH = "HIGH"
        CRITICAL = "CRITICAL"

    severity = models.CharField(max_length=10, choices=Severity.choices)

    class Status(models.TextChoices):
        OPEN = "OPEN"
        RESOLVED = "RESOLVED"

    status = models.CharField(max_length=10, choices=Status.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

class StatusHistory(models.Model):
    
    incident = models.ForeignKey(
        Incident,
        on_delete=models.CASCADE,
        related_name="history"
    )

    old_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)

    changed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )

    changed_at = models.DateTimeField(auto_now_add=True)