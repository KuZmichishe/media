# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0012_auto_20170914_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='movie_db_id',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
