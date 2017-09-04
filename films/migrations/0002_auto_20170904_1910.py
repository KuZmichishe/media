# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Genre'),
        ),
    ]
