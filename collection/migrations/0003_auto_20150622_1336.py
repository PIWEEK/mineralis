# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_mineral_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineral',
            name='chemical_composition',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mineral',
            name='location',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='mineral',
            name='strength',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='collection/media'),
        ),
    ]
