# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squad_builder', '0002_squad_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipmaneuver',
            name='energy',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='upgrade',
            name='energy',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
