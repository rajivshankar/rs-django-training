# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.FloatField(null=True, verbose_name='Latitude', blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.FloatField(null=True, verbose_name='Longtude', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='large_image',
            field=models.ImageField(upload_to=b'', verbose_name='Large Image'),
        ),
        migrations.AlterField(
            model_name='location',
            name='medium_image',
            field=models.ImageField(upload_to=b'', verbose_name='Medium Image'),
        ),
    ]
