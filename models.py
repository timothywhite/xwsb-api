from django.db import models

class Faction(models.Model):
	name = models.CharField(max_length=255)

class Action(models.Model):
	name = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.name

class Maneuver(models.Model):
	LEFT = 'LFT'
	RIGHT = 'RHT'
	STRAIGHT = 'STR'
	TURN = 'TRN'
	BANK = 'BNK'
	KTURN = 'KTN'
	SLOOP = 'SLP'
	DIRECTIONS = (
		(LEFT, 'Left'),
		(RIGHT, 'Right')
	)
	ANGLES = (
		(TURN, 'Turn'),
		(BANK, 'Bank'),
		(STRAIGHT, 'Straight'),
		(KTURN, 'K-Turn'),
		(SLOOP, 'S-Loop')
	)
	speed = models.IntegerField()
	direction = models.CharField(max_length=3, choices=DIRECTIONS, null=True, blank=True)
	angle = models.CharField(max_length=3, choices=ANGLES)
	
	def __unicode__(self):
		return str(self.speed) + ' ' + str(self.direction) + ' ' + self.angle + ' '
	
class UpgradeType(models.Model):
	name = models.CharField(max_length=255)
	order = models.IntegerField()

class Expansion(models.Model):
	name = models.CharField(max_length=255)
	order = models.IntegerField()


class ExpansionShip(models.Model):
	expansion = models.ForeignKey('Expansion')
	ship = models.ForeignKey('Ship')
	count = models.IntegerField()

class ExpansionPilot(models.Model):
	expansion = models.ForeignKey('Expansion')
	pilot = models.ForeignKey('Pilot')
	count = models.IntegerField()

class ExpansionUpgrade(models.Model):
	expansion = models.ForeignKey('Expansion')
	upgrade = models.ForeignKey('Upgrade')
	count = models.IntegerField()

class Base:
	SMALL = 0
	LARGE = 1
	HUGE = 2

class Ship(models.Model):
	name = models.CharField(max_length=255)
	attack = models.IntegerField()
	agility = models.IntegerField()
	shield = models.IntegerField()
	hull = models.IntegerField()
	base = models.IntegerField()

	maneuvers = models.ManyToManyField('Maneuver', through='ShipManeuver')	
	actions = models.ManyToManyField('Action')
	expansions = models.ManyToManyField('Expansion', through='ExpansionShip')

	def __unicode__(self):
		return self.name

class ShipManeuver(models.Model):
	RED = 'R'
	WHITE = 'W'
	GREEN = 'G'
	COLORS = (
		(RED, 'Red'),
		(WHITE, 'White'),
		(GREEN, 'Green')
	)
	ship = models.ForeignKey('Ship')
	maneuver = models.ForeignKey('Maneuver')
	color = models.CharField(max_length=1, choices=COLORS)
	
	def __unicode__(self):
		return str(self.color) + ' ' + str(self.maneuver)

class Pilot(models.Model):
	name = models.CharField(max_length=255)
	text = models.TextField(blank=True)
	skill = models.IntegerField()
	points = models.IntegerField()
	unique = models.BooleanField()
	
	attack = models.IntegerField(null=True, blank=True)
	agility = models.IntegerField(null=True, blank=True)
	shield = models.IntegerField(null=True, blank=True)
	hull = models.IntegerField(null=True, blank=True)
	
	ship = models.ForeignKey('Ship', related_name='pilots')
	faction = models.ForeignKey('Faction', related_name='pilots')
	slots = models.ManyToManyField('UpgradeType')
	expansion = models.ManyToManyField('Expansion', through='ExpansionPilot')
	
class Upgrade(models.Model):
	name = models.CharField(max_length=255)
	text = models.TextField(default='')
	points = models.IntegerField(default=0)	
	unique = models.BooleanField(default=False)
	limited = models.BooleanField(default=False)
	required_slots = models.IntegerField(default=1)
	
	attack = models.IntegerField(null=True, blank=True)
	range = models.CharField(max_length=3, null=True, blank=True)
	
	type = models.ForeignKey('UpgradeType', related_name='upgrades')
	faction = models.ForeignKey('Faction', null=True, related_name='upgrades')
	expansion = models.ManyToManyField('Expansion', through='ExpansionUpgrade')

class UpgradeBonus(models.Model):
	prop = models.CharField(max_length=255)
	value = models.IntegerField()
	limited = models.BooleanField(default=False)
	
	upgrade = models.ForeignKey('Upgrade', related_name='bonuses')

class Requirement(models.Model):
	EQUALS = '=='
	NOT_EQUALS = '!='
	GREATER_THAN = '>'
	LESS_THAN = '<'
	GREATER_THAN_OR_EQUAL = '>='
	LESS_THAN_OR_EQUAL = '<='
	CONTAINS = '[]'
	NOT_CONTAINS = '![]'
	OPERATORS = (
		(EQUALS, '=='),
	 (NOT_EQUALS, '!='),
	 (GREATER_THAN, '>'),
	 (LESS_THAN, '<'),
	 (GREATER_THAN_OR_EQUAL, '>='),
	 (LESS_THAN_OR_EQUAL, '<='),
	 (CONTAINS, '[]'),
		(NOT_CONTAINS, '![]')
	)
	prop = models.CharField(max_length=255)
	operator = models.CharField(max_length=3, choices=OPERATORS)
	value = models.IntegerField()
	required = models.BooleanField(default=True)

	class Meta:
		abstract = True

class UpgradeRequirement(Requirement):
	upgrade = models.ForeignKey('Upgrade', related_name='requirements')
	
class UpgradeBonusRequirement(Requirement):
	bonus = models.ForeignKey('UpgradeBonus', related_name='requirements')

class UpgradeManeuver(models.Model):
	speed = models.IntegerField(null=True, blank=True)
	direction = models.CharField(max_length=3, choices=Maneuver.DIRECTIONS, null=True, blank=True)
	angle = models.CharField(max_length=3, choices=Maneuver.ANGLES, null=True, blank=True)
	color = models.CharField(max_length=1, choices=ShipManeuver.COLORS, null=True, blank=True)
	
	upgrade = models.ForeignKey('Upgrade', related_name='maneuvers')

class Squad(models.Model):
	name = models.CharField(max_length=255)
	
	faction = models.ForeignKey('Faction', related_name='squads')
	pilots = models.ManyToManyField('Pilot', through='SquadPilot')
	
class SquadPilot(models.Model):
	squad = models.ForeignKey('Squad')
	pilot = models.ForeignKey('Pilot')
	upgrades = models.ManyToManyField('Upgrade')

