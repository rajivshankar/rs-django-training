# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex_models', '0008_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='myPerson',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('ex_models.person',),
        ),
    ]
