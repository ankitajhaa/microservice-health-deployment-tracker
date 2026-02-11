from rest_framework.routers import DefaultRouter

from .views import DeploymentViewSet

router = DefaultRouter()
router.register('deployments', DeploymentViewSet)

urlpatterns = router.urls