# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0013_auto_20170916_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='is_updated',
            field=models.BooleanField(default=False),
        ),
    ]
