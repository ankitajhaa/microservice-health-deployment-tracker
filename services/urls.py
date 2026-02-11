from rest_framework.routers import DefaultRouter

from .views import ServiceViewSet, EnvironmentViewSet

router = DefaultRouter()
router.register("services", ServiceViewSet)
router.register("environments", EnvironmentViewSet)

urlpatterns = router.urls