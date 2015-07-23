from django.forms import widgets
from rest_framework import serializers
from squad_builder.models import *

class FactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Faction
		fields = ('id', 'name')

class ManeuverSerializer(serializers.ModelSerializer):
	class Meta:
		model = Maneuver
		fields = ('id', 'speed', 'angle', 'direction')

class ShipManeuverSerializer(serializers.ModelSerializer):
	maneuver = ManeuverSerializer()
	class Meta:
		model = ShipManeuver
		fields = ('id', 'maneuver', 'color')
				
class ShipSerializer(serializers.ModelSerializer):
	maneuvers = ShipManeuverSerializer(source='shipmaneuver_set', many=True)
	class Meta:
		model = Ship
		fields = ('id', 'name', 'attack', 'agility', 'hull', 'shield', 'base', 'actions', 'maneuvers')

class CreateShipManeuverSerializer(serializers.ModelSerializer):
        class Meta:
                model = ShipManeuver
                fields = ('id', 'ship', 'maneuver', 'color')

class PilotSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pilot
		fields = ('id', 'name', 'text', 'skill', 'attack', 'agility', 'hull', 'shield', 'points', 'unique', 'faction', 'ship', 'slots')

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
		fields = ('id', 'name', 'text', 'points', 'unique', 'limited', 'required_slots', 'attack', 'range', 'type', 'faction', 'expansion', 'bonuses', 'requirements')
