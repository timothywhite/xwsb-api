from django.conf.urls import url, include
from squad_builder import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'maneuver', views.ManeuverViewSet)
router.register(r'ship/maneuver', views.ShipManeuverViewSet)
router.register(r'ship', views.ShipViewSet)
router.register(r'pilot', views.PilotViewSet)
router.register(r'upgrade/bonus/requirement', views.UpgradeBonusRequirementViewSet)
router.register(r'upgrade/bonus', views.UpgradeBonusViewSet)
router.register(r'upgrade/requirement', views.UpgradeRequirementViewSet)
router.register(r'upgrade/maneuver', views.UpgradeManeuverViewSet)
router.register(r'upgrade', views.UpgradeViewSet)
# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
