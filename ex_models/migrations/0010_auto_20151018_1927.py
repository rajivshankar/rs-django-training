# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex_models', '0009_myperson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(serialize=False, primary_key=True)),
                ('headline', models.CharField(max_length=50)),
                ('body', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='myperson',
            options={'ordering': ['-last_name']},
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('article_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='ex_models.Article')),
                ('book_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='ex_models.Book')),
            ],
            bases=('ex_models.book', 'ex_models.article'),
        ),
    ]
