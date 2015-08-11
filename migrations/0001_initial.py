# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Expansion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('released', models.BooleanField(default=True)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ExpansionPilot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('expansion', models.ForeignKey(related_name='pilots', to='squad_builder.Expansion')),
            ],
        ),
        migrations.CreateModel(
            name='ExpansionShip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('expansion', models.ForeignKey(related_name='ships', to='squad_builder.Expansion')),
            ],
        ),
        migrations.CreateModel(
            name='ExpansionUpgrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('expansion', models.ForeignKey(related_name='upgrades', to='squad_builder.Expansion')),
            ],
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Maneuver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('speed', models.IntegerField()),
                ('direction', models.CharField(blank=True, max_length=3, null=True, choices=[(b'LFT', b'Left'), (b'RHT', b'Right')])),
                ('angle', models.CharField(max_length=3, choices=[(b'TRN', b'Turn'), (b'BNK', b'Bank'), (b'STR', b'Straight'), (b'KTN', b'K-Turn'), (b'SLP', b'S-Loop')])),
            ],
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('text', models.TextField(blank=True)),
                ('skill', models.IntegerField()),
                ('points', models.IntegerField()),
                ('unique', models.BooleanField()),
                ('attack', models.IntegerField(null=True, blank=True)),
                ('agility', models.IntegerField(null=True, blank=True)),
                ('shield', models.IntegerField(null=True, blank=True)),
                ('hull', models.IntegerField(null=True, blank=True)),
                ('expansions', models.ManyToManyField(to='squad_builder.Expansion', through='squad_builder.ExpansionPilot')),
                ('faction', models.ForeignKey(related_name='pilots', to='squad_builder.Faction')),
            ],
        ),
        migrations.CreateModel(
            name='PilotSlot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pilot', models.ForeignKey(to='squad_builder.Pilot')),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('attack', models.IntegerField()),
                ('agility', models.IntegerField()),
                ('shield', models.IntegerField()),
                ('hull', models.IntegerField()),
                ('base', models.IntegerField()),
                ('actions', models.ManyToManyField(to='squad_builder.Action')),
                ('expansions', models.ManyToManyField(to='squad_builder.Expansion', through='squad_builder.ExpansionShip')),
            ],
        ),
        migrations.CreateModel(
            name='ShipManeuver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=1, choices=[(b'R', b'Red'), (b'W', b'White'), (b'G', b'Green')])),
                ('maneuver', models.ForeignKey(to='squad_builder.Maneuver')),
                ('ship', models.ForeignKey(to='squad_builder.Ship')),
            ],
        ),
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('faction', models.ForeignKey(related_name='squads', to='squad_builder.Faction')),
            ],
        ),
        migrations.CreateModel(
            name='SquadPilot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pilot', models.ForeignKey(to='squad_builder.Pilot')),
                ('squad', models.ForeignKey(to='squad_builder.Squad')),
            ],
        ),
        migrations.CreateModel(
            name='SquadPilotUpgrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.IntegerField()),
                ('pilot', models.ForeignKey(to='squad_builder.SquadPilot')),
            ],
        ),
        migrations.CreateModel(
            name='Upgrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('text', models.TextField(default=b'')),
                ('points', models.IntegerField(default=0)),
                ('unique', models.BooleanField(default=False)),
                ('limited', models.BooleanField(default=False)),
                ('required_slots', models.IntegerField(default=1)),
                ('attack', models.IntegerField(null=True, blank=True)),
                ('range', models.CharField(max_length=3, null=True, blank=True)),
                ('expansions', models.ManyToManyField(to='squad_builder.Expansion', through='squad_builder.ExpansionUpgrade')),
                ('faction', models.ForeignKey(related_name='upgrades', blank=True, to='squad_builder.Faction', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UpgradeBonus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prop', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
                ('limited', models.BooleanField(default=False)),
                ('upgrade', models.ForeignKey(related_name='bonuses', to='squad_builder.Upgrade')),
            ],
        ),
        migrations.CreateModel(
            name='UpgradeBonusRequirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prop', models.CharField(max_length=255)),
                ('operator', models.CharField(max_length=3, choices=[(b'==', b'=='), (b'!=', b'!='), (b'>', b'>'), (b'<', b'<'), (b'>=', b'>='), (b'<=', b'<='), (b'[]', b'[]'), (b'![]', b'![]')])),
                ('value', models.IntegerField()),
                ('required', models.BooleanField(default=True)),
                ('bonus', models.ForeignKey(related_name='requirements', to='squad_builder.UpgradeBonus')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UpgradeManeuver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('speed', models.IntegerField(null=True, blank=True)),
                ('direction', models.CharField(blank=True, max_length=3, null=True, choices=[(b'LFT', b'Left'), (b'RHT', b'Right')])),
                ('angle', models.CharField(blank=True, max_length=3, null=True, choices=[(b'TRN', b'Turn'), (b'BNK', b'Bank'), (b'STR', b'Straight'), (b'KTN', b'K-Turn'), (b'SLP', b'S-Loop')])),
                ('color', models.CharField(blank=True, max_length=1, null=True, choices=[(b'R', b'Red'), (b'W', b'White'), (b'G', b'Green')])),
                ('upgrade', models.ForeignKey(related_name='maneuvers', to='squad_builder.Upgrade')),
            ],
        ),
        migrations.CreateModel(
            name='UpgradeRequirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prop', models.CharField(max_length=255)),
                ('operator', models.CharField(max_length=3, choices=[(b'==', b'=='), (b'!=', b'!='), (b'>', b'>'), (b'<', b'<'), (b'>=', b'>='), (b'<=', b'<='), (b'[]', b'[]'), (b'![]', b'![]')])),
                ('value', models.IntegerField()),
                ('required', models.BooleanField(default=True)),
                ('upgrade', models.ForeignKey(related_name='requirements', to='squad_builder.Upgrade')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UpgradeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='upgrade',
            name='type',
            field=models.ForeignKey(related_name='upgrades', to='squad_builder.UpgradeType'),
        ),
        migrations.AddField(
            model_name='squadpilotupgrade',
            name='upgrade',
            field=models.ForeignKey(to='squad_builder.Upgrade'),
        ),
        migrations.AddField(
            model_name='squadpilot',
            name='upgrades',
            field=models.ManyToManyField(to='squad_builder.Upgrade', through='squad_builder.SquadPilotUpgrade'),
        ),
        migrations.AddField(
            model_name='squad',
            name='pilots',
            field=models.ManyToManyField(to='squad_builder.Pilot', through='squad_builder.SquadPilot'),
        ),
        migrations.AddField(
            model_name='ship',
            name='maneuvers',
            field=models.ManyToManyField(to='squad_builder.Maneuver', through='squad_builder.ShipManeuver'),
        ),
        migrations.AddField(
            model_name='pilotslot',
            name='slot',
            field=models.ForeignKey(to='squad_builder.UpgradeType'),
        ),
        migrations.AddField(
            model_name='pilot',
            name='ship',
            field=models.ForeignKey(related_name='pilots', to='squad_builder.Ship'),
        ),
        migrations.AddField(
            model_name='pilot',
            name='slots',
            field=models.ManyToManyField(to='squad_builder.UpgradeType', through='squad_builder.PilotSlot'),
        ),
        migrations.AddField(
            model_name='expansionupgrade',
            name='upgrade',
            field=models.ForeignKey(to='squad_builder.Upgrade'),
        ),
        migrations.AddField(
            model_name='expansionship',
            name='ship',
            field=models.ForeignKey(to='squad_builder.Ship'),
        ),
        migrations.AddField(
            model_name='expansionpilot',
            name='pilot',
            field=models.ForeignKey(to='squad_builder.Pilot'),
        ),
    ]
