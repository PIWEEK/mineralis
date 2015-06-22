# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20150622_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineral',
            name='kind',
            field=models.CharField(max_length=255, blank=True, null=True, choices=[('ELEMENTS', 'Elements'), ('SULFIDES', 'Sulfides and sulfosalts'), ('HALIDES', 'Halides'), ('OXIDES', 'Oxides, hydroxides and arsenites'), ('CARBONATES', 'Carbonates and nitrates'), ('BORATES', 'Borates'), ('SULFATES', 'Sulfates, chromates, molybdates and tungstates'), ('PHOSPHATES', 'Phosphates, arsenates and vanadates'), ('SILICATES', 'Silicates'), ('ORGANIC', 'Organic compounds')]),
        ),
    ]
