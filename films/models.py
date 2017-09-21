# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Film(models.Model):
    title = models.CharField(max_length=250)
    genre = models.ForeignKey(Genre, default=1)
    file_name = models.CharField(max_length=250, unique=True)
    file_extension = models.CharField(max_length=10)
    file_size = models.CharField(null=True, max_length=10)
    poster = models.CharField(null=True, max_length=250)
    background = models.CharField(null=True, max_length=250)
    first_air_date = models.DateField(null=True, auto_now=False)
    movie_db_id = models.IntegerField(null=True, default=0)
    is_viewed = models.BooleanField(default=False)
    is_updated = models.BooleanField(default=False)
    overview = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
