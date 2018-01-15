# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from . import iot


class HtmlTag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255, unique = True)
    tag_text = models.TextField()
    created_on_date = models.DateTimeField(auto_now_add = True, editable = False)    
    modified_on_date = models.DateTimeField(auto_now = True, editable = False)
    author = models.ForeignKey(User, blank=True, null=True)
    security_id = models.ForeignKey(iot.SecurityIdModel, models.SET_NULL, blank = True, null = True)

class StyleTag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255, unique = True)
    style_text = models.TextField()
    created_on_date = models.DateTimeField(auto_now_add = True, editable = False)
    modified_on_date = models.DateTimeField(auto_now = True, editable = False)
    author = models.ForeignKey(User, blank=True, null=True)
    security_id = models.ForeignKey(iot.SecurityIdModel, models.SET_NULL, blank = True, null = True)

class ScriptTag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255, unique = True)
    script_text = models.TextField()
    created_on_date = models.DateTimeField(auto_now_add = True, editable = False)
    modified_on_date = models.DateTimeField(auto_now = True, editable = False)
    author = models.ForeignKey(User, blank=True, null=True)
    security_id = models.ForeignKey(iot.SecurityIdModel, models.SET_NULL, blank = True, null = True)

