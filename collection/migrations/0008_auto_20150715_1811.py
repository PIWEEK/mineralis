# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0007_auto_20150715_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineral',
            name='crystalization_system',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mineral',
            name='mineral_deposit',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='kind',
            field=models.CharField(blank=True, choices=[('ELEMENTS', 'Elementos nativos'), ('SULFIDES', 'Sulfuros y sulfosales'), ('HALIDES', 'Halogenuros'), ('OXIDES', 'Óxidos e hidroxidos'), ('CARBONATES', 'Carbonatos y nitratos'), ('BORATES', 'Boratos'), ('SULFATES', 'Sulfatos, cromatos, molibdatos y wolframatos'), ('PHOSPHATES', 'Fosfatos, arseniatos y vanadatos'), ('SILICATES', 'Silicatos'), ('ORGANIC', 'Sustancias orgánicas')], max_length=255, null=True),
        ),
    ]
