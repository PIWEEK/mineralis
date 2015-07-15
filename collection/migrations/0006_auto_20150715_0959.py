# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_auto_20150703_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineral',
            name='thumbnail',
            field=models.ImageField(upload_to='collection/media', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='mineral',
            field=models.ForeignKey(related_name='images', to='collection.Mineral'),
        ),
    ]
