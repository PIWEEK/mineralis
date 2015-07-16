# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0006_auto_20150715_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineral',
            name='chemical_composition',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
