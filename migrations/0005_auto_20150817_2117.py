# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squad_builder', '0004_ship_energy'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='range',
            field=models.CharField(default=b'1-3', max_length=3),
        ),
        migrations.AddField(
            model_name='ship',
            name='turret',
            field=models.BooleanField(default=False),
        ),
    ]
