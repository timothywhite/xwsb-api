from squad_builder.models import *
from squad_builder.serializers import *

from django.db.models import Q

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class ActionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class ShipViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer

class PilotViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer

class UpgradeTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UpgradeType.objects.all()
    serializer_class = UpgradeTypeSerializer
	
class UpgradeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UpgradeSerializer
    queryset = Upgrade.objects.all()

class ExpansionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Expansion.objects.all()
    serializer_class = ExpansionSerializer
    
class SquadViewSet(viewsets.ModelViewSet):
    serializer_class = SquadSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return Squad.objects.filter(user=self.request.user)

class SquadPilotViewSet(viewsets.ModelViewSet):
    serializer_class = CreateSquadPilotSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return SquadPilot.objects.filter(squad__user=self.request.user)
	
class SquadPilotUpgradeViewSet(viewsets.ModelViewSet):
    serializer_class = SquadPilotUpgradeSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return SquadPilotUpgrade.objects.filter(pilot__squad__user=self.request.user)