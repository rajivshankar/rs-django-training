# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex_models', '0003_auto_20151018_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'group name')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_joined', models.DateField(verbose_name=b'date joined')),
                ('invite_reason', models.CharField(max_length=64)),
                ('group', models.ForeignKey(to='ex_models.Group')),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(default=None, choices=[(b'S', b'Small'), (b'M', b'MEdium'), (b'L', b'Large')], max_length=1, blank=True, null=True, verbose_name=b'shirt size'),
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(to='ex_models.Person'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(to='ex_models.Person', through='ex_models.Membership'),
        ),
    ]
