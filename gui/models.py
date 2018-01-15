# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .gui_models import iot
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class ApplicationModel(iot.BaseModel):    
    version = models.CharField(max_length=20)
    url = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    selected_template = models.ForeignKey('TemplateModel', models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User)
    class Meta:
        verbose_name_plural = "Applications"
        verbose_name = "Application"

class Layout(iot.BaseModel):
    pass

class UIElementModel(iot.BaseModel):
    element_type = models.CharField(max_length=255)

class ControlModel(UIElementModel):
    control_type = models.CharField(max_length=255)
    parent_id = models.ForeignKey('self', models.SET_NULL, blank=True, null=True)

class TemplateModel(iot.BaseModel):    
    template_type = models.CharField(max_length=255)
    template_path = models.CharField(max_length=255)
    template_applied_on = models.ForeignKey(ControlModel, models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)
    class Meta:
        verbose_name = "Template"
        verbose_name_plural = "Templates"

class StyleModel(iot.BaseModel):    
    style_type = models.CharField(max_length=255)
    style_path = models.CharField(max_length=255)
    style_applied_on = models.ForeignKey(ControlModel, models.SET_NULL, blank = True, null = True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)
    class Meta:
        verbose_name = "Style"
        verbose_name_plural = "Styles"

class ContentControlModel(ControlModel):        
    template = models.ForeignKey(TemplateModel, models.SET_NULL, blank = True, null = True)
    style = models.ForeignKey(StyleModel, models.SET_NULL, blank = True, null = True)
    content = models.ForeignKey('self', models.SET_NULL, blank = True, null = True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)
    class Meta:
        verbose_name="ContentControl"
        verbose_name_plural = "ContentControls"

class ItemsControlModel(ContentControlModel):    
    items = models.ManyToManyField(ContentControlModel, related_name = '+')
    class Meta:
        verbose_name = "ItemsControl"
        verbose_name_plural = "ItemsControls"
