# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex_models', '0007_place_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('place_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='ex_models.Place')),
                ('customers', models.ManyToManyField(related_name='supplier_related', to='ex_models.Place')),
            ],
            bases=('ex_models.place',),
        ),
    ]
