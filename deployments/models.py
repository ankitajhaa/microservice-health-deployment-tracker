from django.conf import settings
from django.db import models

# Create your models here.

class Deployment(models.Model):

    class Status(models.TextChoices):
        SUCCESS = "SUCCESS"
        FAILED = "FAILED"

    service = models.ForeignKey(
        "services.Service",
        on_delete=models.CASCADE,
        related_name="deployments"
    )
    environment = models.ForeignKey(
        "services.Environment",
        on_delete=models.CASCADE,
        related_name="deployments"
    )
    version = models.CharField(max_length=100)
    deployed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    deployed_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices)

    def __str__(self):
        return f"{self.service.name} - {self.version}"