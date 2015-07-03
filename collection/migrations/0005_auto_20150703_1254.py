# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_mineral_kind'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('image', models.ImageField(upload_to='collection/media', null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'images',
                'verbose_name': 'image',
            },
        ),
        migrations.RemoveField(
            model_name='mineral',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='mineral',
            field=models.ForeignKey(to='collection.Mineral'),
        ),
    ]
