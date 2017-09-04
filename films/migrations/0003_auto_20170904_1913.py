# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_auto_20170904_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genre',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
