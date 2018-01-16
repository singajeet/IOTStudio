# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import os
from IOTStudio.settings import BASE_DIR
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
    STYLE_TYPES=(
            ('-1', 'None'),
            ('00', 'File'),
            ('01', 'Inline'),
            )
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255, unique = True)
    style_type = models.CharField(max_length=2, choices=STYLE_TYPES, default='00')
    style_text = models.TextField(blank=True, null=True)
    style_file = models.FilePathField(path=os.path.join(BASE_DIR, 'staticfiles/css'), recursive = True, allow_folders = False, blank = True, null = True)
    created_on_date = models.DateTimeField(auto_now_add = True, editable = False)
    modified_on_date = models.DateTimeField(auto_now = True, editable = False)
    author = models.ForeignKey(User, blank=True, null=True)
    security_id = models.ForeignKey(iot.SecurityIdModel, models.SET_NULL, blank = True, null = True)

class ScriptTag(models.Model):
    SCRIPT_TYPES=(
            ('-1', 'None'),
            ('00', 'File'),
            ('01', 'Inline'),
            )
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255, unique = True)
    script_type = models.CharField(max_length = 2, choices=SCRIPT_TYPES, default='00')
    script_file = models.FilePathField(path=os.path.join(BASE_DIR, 'staticfiles/js'), recursive=True, allow_folders=False, blank=True, null=True)
    script_text = models.TextField(blank=True, null=True)
    created_on_date = models.DateTimeField(auto_now_add = True, editable = False)
    modified_on_date = models.DateTimeField(auto_now = True, editable = False)
    author = models.ForeignKey(User, blank=True, null=True)
    security_id = models.ForeignKey(iot.SecurityIdModel, models.SET_NULL, blank = True, null = True)

