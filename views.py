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
	
class PilotSlotViewSet(viewsets.ModelViewSet):
	queryset = PilotSlot.objects.all()
	serializer_class = PilotSlotSerializer

class UpgradeTypeViewSet(viewsets.ModelViewSet):
	queryset = UpgradeType.objects.all()
	serializer_class = UpgradeTypeSerializer
	
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

class ExpansionViewSet(viewsets.ModelViewSet):
	queryset = Expansion.objects.all()
	serializer_class = ExpansionSerializer

class ExpansionShipViewSet(viewsets.ModelViewSet):
	queryset = ExpansionShip.objects.all()
	serializer_class = ExpansionShipSerializer

class ExpansionPilotViewSet(viewsets.ModelViewSet):
	queryset = ExpansionPilot.objects.all()
	serializer_class = ExpansionPilotSerializer

class ExpansionUpgradeViewSet(viewsets.ModelViewSet):
	queryset = ExpansionUpgrade.objects.all()
	serializer_class = ExpansionUpgradeSerializer
	
class ActionViewSet(viewsets.ModelViewSet):
	queryset = Action.objects.all()
	serializer_class = ActionSerializer
	
class SquadPilotViewSet(viewsets.ModelViewSet):
	queryset = SquadPilot.objects.all()
	serializer_class = CreateSquadPilotSerializer
	
class SquadViewSet(viewsets.ModelViewSet):
	queryset = Squad.objects.all()
	serializer_class = SquadSerializer
