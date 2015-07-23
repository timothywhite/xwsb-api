from squad_builder.models import *
from squad_builder.serializers import *

from rest_framework import viewsets


class ShipViewSet(viewsets.ModelViewSet):
	queryset = Ship.objects.all()
	serializer_class = ShipSerializer

class ShipManeuverViewSet(viewsets.ModelViewSet):
	queryset = ShipManeuver.objects.all()
	serializer_class = CreateShipManeuverSerializer

class ManeuverViewSet(viewsets.ModelViewSet):
	queryset = Maneuver.objects.all()
	serializer_class = ManeuverSerializer

class PilotViewSet(viewsets.ModelViewSet):
	queryset = Pilot.objects.all()
	serializer_class = PilotSerializer

class UpgradeViewSet(viewsets.ModelViewSet):
	queryset = Upgrade.objects.all()
	serializer_class = UpgradeSerializer

class UpgradeBonusViewSet(viewsets.ModelViewSet):
	queryset = UpgradeBonus.objects.all()
	serializer_class = UpgradeBonusSerializer

class UpgradeRequirementViewSet(viewsets.ModelViewSet):
	queryset = UpgradeRequirement.objects.all()
	serializer_class = UpgradeRequirementSerializer

class UpgradeManeuverViewSet(viewsets.ModelViewSet):
	queryset = UpgradeManeuver.objects.all()
	serializer_class = UpgradeManeuverSerializer

class UpgradeBonusRequirementViewSet(viewsets.ModelViewSet):
	queryset = UpgradeBonusRequirement.objects.all()
	serializer_class = UpgradeBonusRequirementSerializer
