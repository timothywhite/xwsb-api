from squad_builder.models import *
from squad_builder.serializers import *

from django.db.models import Q

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    If the request is a PUT, PATCH, or DELETE, ensure that the user field equals request.user
    """
    
    def has_permission(self, request, view):
        if 'pk' in request.resolver_match.kwargs:
            pk = request.resolver_match.kwargs['pk']
            return view.get_queryset().filter(pk=pk).exists()
        else:
            return True

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
    serializer_class = UpgradeSerializer
    
    def get_queryset(self):
        queryset = Upgrade.objects.all()
        filters = []
        if 'type' in self.request.query_params:
            filters.append(Q(type__exact=self.request.query_params['type']))
            
        if 'faction' in self.request.query_params:
            filters.append(Q(faction__isnull=True) | Q(faction__exact=self.request.query_params['faction']))
        
        if (len(filters)):
            filter = reduce(lambda p, c: p & c, filters)
            queryset = queryset.filter(filter)
        
        for prop, value in self.request.query_params.iteritems():
            if prop != 'type' and prop != 'faction':
                queryset = queryset.exclude(Q(requirements__prop__exact=prop) & ~Q(requirements__value__exact=value))
                
        return queryset

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
	
class SquadPilotUpgradeViewSet(viewsets.ModelViewSet):
    queryset = SquadPilotUpgrade.objects.all()
    serializer_class = SquadPilotUpgradeSerializer
    
class SquadViewSet(viewsets.ModelViewSet):
    serializer_class = SquadSerializer
    #permission_classes = (IsAuthenticated, IsOwner)
    
    def get_queryset(self):
        return Squad.objects.all()#filter(user=self.request.user)
