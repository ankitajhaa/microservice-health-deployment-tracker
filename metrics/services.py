from django.db.models import Count, Q
from services.models import Service
from deployments.models import Deployment

def most_unstable_service():
    return (
        Service.objects
        .annotate(total_incidents=Count("incidents"))
        .order_by("-total_incidents")
        .first()
    )

def failure_ratio():
    return (
        Service.objects
        .annotate(
            total=Count("deployments"),
            failed=Count("deployments", filter=Q(deployments_status="FAILED"))
        )
    )

def incident_counts():
    return (
        Service.objects
        .annotate(total_incidents=Count("incidents"))
    )

def deployments_freq():
    return (
        Deployment.objects
        .annotate(total_deployments=Count("deployments"))
    )