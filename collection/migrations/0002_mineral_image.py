# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineral',
            name='image',
            field=models.ImageField(null=True, upload_to='media', blank=True),
        ),
    ]
