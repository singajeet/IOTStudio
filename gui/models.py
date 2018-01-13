# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .gui_models import iot

# Create your models here.
class ApplicationModel(iot.BaseModel):
    author = models.CharField(max_length=255)
    version = models.CharField(max_length=20)
    url = models.CharField(max_length=255)
    company = models.CharField(max_length=255)

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

class StyleModel(iot.BaseModel):
    style_type = models.CharField(max_length=255)
    style_path = models.CharField(max_length=255)
    style_applied_on = models.ForeignKey(ControlModel, models.SET_NULL, blank = True, null = True)

class ContentControlModel(ControlModel):
    template = models.ForeignKey(TemplateModel, models.SET_NULL, blank = True, null = True)
    style = models.ForeignKey(StyleModel, models.SET_NULL, blank = True, null = True)
    content = models.ForeignKey('self', models.SET_NULL, blank = True, null = True)

class ItemsControlModel(ContentControlModel):
	items = models.ManyToManyField(ContentControlModel, related_name = '+')
	