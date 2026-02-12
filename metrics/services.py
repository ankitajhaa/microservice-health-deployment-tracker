from django.db.models import Count, Q, Avg, F, ExpressionWrapper, DurationField, FloatField, Case, When
from incidents.models import Incident
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

def calculate_mttr():
    resolved_incidents = Incident.objects.filter(
        status=Incident.Status.RESOLVED,
        resolved_at__isnull=False,
    )
    return resolved_incidents.annotate(
        duration=ExpressionWrapper(
            F("resolved_at") - F("created_at"),
            output_field=DurationField(),
        )
    ).aggregate(avg_mttr=Avg("duration"))

def deployment_reliability():
    return (
        Service.objects
        .annotate(
            total=Count("deployments"),
            failed=Count(
                "deployments",
                filter=Q(deployments__status="FAILED")
            ),
        )
        .annotate(
            failure_rate=Case(
                When(total=0, then=0),
                default=(F("failed") * 100.0) / F("total"),
                output_field=FloatField(),
            )
        )
    )