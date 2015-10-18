# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ex_models', '0004_auto_20151018_1624'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['last_name'], 'verbose_name_plural': 'People'},
        ),
        migrations.AddField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 18, 15, 57, 42, 427000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
