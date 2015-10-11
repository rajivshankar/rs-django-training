# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='creation date and time', editable=False)),
                ('modified', models.DateTimeField(verbose_name='modification date and time', null=True, editable=False)),
                ('meta_keywords', models.CharField(help_text='Separate Keywords by comma.', max_length=255, verbose_name='Keywords', blank=True)),
                ('meta_description', models.CharField(max_length=255, verbose_name='Description', blank=True)),
                ('meta_author', models.CharField(max_length=255, verbose_name='Author', blank=True)),
                ('meta_copyright', models.CharField(max_length=255, verbose_name='Charfield', blank=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Idea',
                'verbose_name_plural': 'Ideas',
            },
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='status',
            field=models.CharField(max_length=20, verbose_name='Status', choices=[(b'draft', 'Draft'), (b'published', 'Published'), (b'not listed', 'Not Listed')]),
        ),
    ]
