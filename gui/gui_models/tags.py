# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class HtmlTags(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=255)
    tag_text = models.CharField(max_length=5000)
    created_on_date = models.DateTimeField()
    author = models.CharField(max_length=255)
    security_id = models.IntegerField()

class StyleTags(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=255)
    style_text = models.CharField(max_length=5000)
    created_on_date = models.DateTimeField()
    author = models.CharField(max_length=255)
    security_id = models.IntegerField()

class ScriptTags(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=255)
    script_text = models.CharField(max_length=5000)
    created_on_date = models.DateTimeField()
    author = models.CharField(max_length=255)
    security_id = models.IntegerField()

