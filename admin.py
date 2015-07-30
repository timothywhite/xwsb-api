from django.contrib import admin
from squad_builder.models import *


admin.site.register(Ship)
admin.site.register(ShipManeuver)
admin.site.register(Pilot)
admin.site.register(Upgrade)
admin.site.register(UpgradeRequirement)
admin.site.register(UpgradeBonus)
admin.site.register(UpgradeBonusRequirement)
admin.site.register(UpgradeType)
