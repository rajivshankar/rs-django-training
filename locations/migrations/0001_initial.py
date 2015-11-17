# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('small_image', models.ImageField(upload_to=b'', verbose_name='Small Image')),
                ('medium_image', models.ImageField(upload_to=b'', verbose_name='Small Image')),
                ('large_image', models.ImageField(upload_to=b'', verbose_name='Small Image')),
            ],
        ),
    ]
