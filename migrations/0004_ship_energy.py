# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squad_builder', '0003_auto_20150813_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='energy',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
