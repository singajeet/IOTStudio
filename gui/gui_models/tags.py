# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class HtmlTag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255)
    tag_text = models.CharField(max_length=5000)
    created_on_date = models.DateTimeField('Created on date', default=datetime.now)
    #author = models.CharField(max_length=255, default = request.user)
    author = models.ForeignKey(User)
    security_id = models.IntegerField(default=0)    

class StyleTag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255)
    style_text = models.CharField(max_length=5000)
    created_on_date = models.DateTimeField('Created on date', default=datetime.now)
    author = models.ForeignKey(User)
    security_id = models.IntegerField(default=0)

class ScriptTag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255)
    script_text = models.CharField(max_length=5000)
    created_on_date = models.DateTimeField('Created on date', default=datetime.now)
    author = models.ForeignKey(User)
    security_id = models.IntegerField(default=0)

