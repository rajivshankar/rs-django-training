# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'author name')),
                ('email', models.EmailField(default=None, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'blog name')),
                ('tagline', models.TextField(default=None, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField(default=None, null=True, blank=True)),
                ('pub_date', models.DateField(default=None, null=True, blank=True)),
                ('mod_date', models.DateField(default=None, null=True, blank=True)),
                ('n_comments', models.IntegerField(default=0)),
                ('n_pingpacks', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=None)),
                ('authors', models.ManyToManyField(to='ex_queries.Author')),
                ('blog', models.ForeignKey(to='ex_queries.Blog')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
