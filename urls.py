from django.conf.urls import url, include
from squad_builder import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'action', views.ActionViewSet)
router.register(r'ship', views.ShipViewSet)
router.register(r'pilot', views.PilotViewSet)
router.register(r'upgrade/type', views.UpgradeTypeViewSet)
router.register(r'upgrade', views.UpgradeViewSet, base_name='Upgrade')
router.register(r'expansion', views.ExpansionViewSet)
router.register(r'squad/pilot/upgrade', views.SquadPilotUpgradeViewSet, base_name='SquadPilotUpgrade')
router.register(r'squad/pilot', views.SquadPilotViewSet, base_name='SquadPilot')
router.register(r'squad', views.SquadViewSet, base_name='Squad')

urlpatterns = [
    url(r'^', include(router.urls)),
]
