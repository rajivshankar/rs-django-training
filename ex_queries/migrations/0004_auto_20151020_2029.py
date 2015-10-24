# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex_queries', '0003_auto_20151019_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='n_pingpacks',
            new_name='n_pingbacks',
        ),
    ]
