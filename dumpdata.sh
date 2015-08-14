#!/bin/bash
../manage.py dumpdata squad_builder.action > fixtures/Action.json
../manage.py dumpdata squad_builder.expansion > fixtures/Expansion.json
../manage.py dumpdata squad_builder.expansionpilot > fixtures/ExpansionPilot.json
../manage.py dumpdata squad_builder.expansionship > fixtures/ExpansionShip.json
../manage.py dumpdata squad_builder.expansionupgrade > fixtures/ExpansionUpgrade.json
../manage.py dumpdata squad_builder.faction > fixtures/Faction.json
../manage.py dumpdata squad_builder.maneuver > fixtures/Maneuver.json
../manage.py dumpdata squad_builder.pilot > fixtures/Pilot.json
../manage.py dumpdata squad_builder.pilotslot > fixtures/PilotSlot.json
../manage.py dumpdata squad_builder.ship > fixtures/Ship.json
../manage.py dumpdata squad_builder.shipmaneuver > fixtures/ShipManeuver.json
../manage.py dumpdata squad_builder.upgradebonus > fixtures/UpgradeBonus.json
../manage.py dumpdata squad_builder.upgradebonusrequirement > fixtures/UpgradeBonusRequirement.json
../manage.py dumpdata squad_builder.upgrade > fixtures/Upgrade.json
../manage.py dumpdata squad_builder.upgrademaneuver > fixtures/UpgradeManeuver.json
../manage.py dumpdata squad_builder.upgraderequirement > fixtures/UpgradeRequirement.json
../manage.py dumpdata squad_builder.upgradetype > fixtures/UpgradeType.json
