# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex_queries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='rating',
            field=models.IntegerField(default=None, null=True, blank=True),
        ),
    ]
