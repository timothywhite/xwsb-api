from django.forms import widgets
from rest_framework import serializers
from squad_builder.models import *

class FactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Faction
		fields = ('id', 'name', 'canonical')

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('id', 'name', 'canonical')

class ManeuverSerializer(serializers.ModelSerializer):
	class Meta:
		model = Maneuver
		fields = ('id', 'speed', 'angle', 'direction')
		
class UpgradeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpgradeType
        fields = ('id', 'name', 'canonical', 'order')

class PilotSerializer(serializers.ModelSerializer):
    faction = FactionSerializer()
    slots = UpgradeTypeSerializer(many=True, read_only=True)
    class Meta:
        model = Pilot
        fields = ('id', 'name', 'canonical', 'text', 'skill', 'attack', 'agility', 'hull', 'shield', 'points', 'unique', 'faction', 'ship', 'slots', 'expansions')

class PilotSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = PilotSlot
        fields = ('id', 'pilot', 'slot')

###########################################################################
##############     UPGRADE      ###########################################
###########################################################################

class UpgradeBonusRequirementSerializer(serializers.ModelSerializer):
	class Meta:
		model = UpgradeBonusRequirement
		fields = ('id', 'prop', 'operator', 'value', 'required', 'bonus')

class UpgradeBonusSerializer(serializers.ModelSerializer):
	requirements = UpgradeBonusRequirementSerializer(many=True, required=False)
	class Meta:
		model = UpgradeBonus
		fields = ('id', 'prop', 'value', 'limited', 'requirements', 'upgrade')

class UpgradeRequirementSerializer(serializers.ModelSerializer):
	class Meta:
		model = UpgradeRequirement
		fields = ('id', 'prop', 'operator', 'value', 'required', 'upgrade')

class UpgradeManeuverSerializer(serializers.ModelSerializer):
	class Meta:
		model = UpgradeManeuver
		fields = ('id', 'speed', 'direction', 'angle', 'color', 'upgrade')

class UpgradeSerializer(serializers.ModelSerializer):
	bonuses = UpgradeBonusSerializer(many=True, required=False, read_only=True)
	requirements = UpgradeRequirementSerializer(many=True, required=False, read_only=True)
	class Meta:
		model = Upgrade
		fields = ('id', 'name', 'canonical', 'text', 'points', 'unique', 'limited', 'required_slots', 'attack', 'range', 'energy', 'type', 'faction', 'expansions', 'bonuses', 'requirements')

###########################################################################
##############       SHIP       ###########################################
###########################################################################

class ShipManeuverSerializer(serializers.ModelSerializer):
	maneuver = ManeuverSerializer()
	class Meta:
		model = ShipManeuver
		fields = ('id', 'maneuver', 'color', 'energy')
		
class CreateShipManeuverSerializer(serializers.ModelSerializer):
        class Meta:
                model = ShipManeuver
                fields = ('id', 'ship', 'maneuver', 'color')

class BaseShipSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ship
		fields = ('id', 'name', 'canonical', 'attack', 'agility', 'hull', 'shield', 'energy', 'base', 'actions', 'maneuvers', 'pilots', 'expansions')

class ShipSerializer(BaseShipSerializer):    
    maneuvers = ShipManeuverSerializer(source='shipmaneuver_set', many=True)
    pilots = PilotSerializer(many=True)
    actions = ActionSerializer(many=True)

###########################################################################
##############    EXPANSION     ###########################################
###########################################################################

class ExpansionShipSerializer(serializers.ModelSerializer):
	class Meta:
		model = ExpansionShip
		fields = ('id', 'expansion', 'ship', 'count')

class ExpansionPilotSerializer(serializers.ModelSerializer):
	class Meta:
		model = ExpansionPilot
		fields = ('id', 'expansion', 'pilot', 'count')

class ExpansionUpgradeSerializer(serializers.ModelSerializer):
	class Meta:
		model = ExpansionUpgrade
		fields = ('id', 'expansion', 'upgrade', 'count')

class ExpansionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Expansion
		fields = ('id', 'name', 'released', 'order', 'ships', 'pilots', 'upgrades') 

###########################################################################
################    SQUAD     #############################################
###########################################################################

class SquadPilotUpgradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SquadPilotUpgrade
        fields = ('id', 'upgrade', 'pilot', 'index')

class DetailSquadPilotUpgradeSerializer(SquadPilotUpgradeSerializer):
    upgrade = UpgradeSerializer()

class SquadPilotShipSerializer(BaseShipSerializer):
    maneuvers = ShipManeuverSerializer(source='shipmaneuver_set', many=True)
    actions = ActionSerializer(many=True)

class PilotAndShipSerializer(PilotSerializer):
    ship = SquadPilotShipSerializer()

class CreateSquadPilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = SquadPilot
        fields = ('id', 'pilot', 'upgrades', 'squad')
        
class SquadPilotSerializer(CreateSquadPilotSerializer):
    pilot = PilotAndShipSerializer()
    upgrades = DetailSquadPilotUpgradeSerializer(many=True, source='squadpilotupgrade_set')
        
class SquadSerializer(serializers.ModelSerializer):
    pilots = SquadPilotSerializer(source='squadpilot_set', many=True, read_only=True)
    class Meta:
        model = Squad
        fields = ('id', 'name', 'faction', 'pilots', 'user')
