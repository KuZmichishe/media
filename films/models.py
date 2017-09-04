# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Film(models.Model):
    title = models.CharField(max_length=250)
    genre = models.ForeignKey(Genre, default='1')
    file_name = models.CharField(max_length=250)
    file_extension = models.CharField(max_length=10)
    is_viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




