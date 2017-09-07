# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 22:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0008_auto_20170906_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='films.Genre'),
        ),
    ]
