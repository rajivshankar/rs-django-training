# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex_models', '0002_fruit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'car model name')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b"manufacturer's name")),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(verbose_name=b'artist name', to='ex_models.Musician'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'name'),
        ),
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(verbose_name=b'rating'),
        ),
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(verbose_name=b'release date'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='instrument',
            field=models.CharField(max_length=100, verbose_name=b'instrument'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name=b'first name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name=b'last name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(max_length=1, verbose_name=b'shirt size', choices=[(b'S', b'Small'), (b'M', b'MEdium'), (b'L', b'Large')]),
        ),
        migrations.AddField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(to='ex_models.Manufacturer'),
        ),
    ]
