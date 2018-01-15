# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models
from .gui_models import tags
# Register your models here.

admin.site.register(models.ApplicationModel)
admin.site.register(models.ContentControlModel)
admin.site.register(models.ItemsControlModel)
admin.site.register(models.TemplateModel)
admin.site.register(models.StyleModel)
admin.site.register(tags.HtmlTag)
admin.site.register(tags.StyleTag)
admin.site.register(tags.ScriptTag)

