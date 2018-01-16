from __future__ import unicode_literals
from django.db import models
from .gui_models import iot
from datetime import datetime
from django.contrib.auth.models import User
from IOTStudio.settings import BASE_DIR
from .gui_models import tags
import os

# Create your models here.
class ApplicationModel(iot.BaseModel):    
    version = models.CharField(max_length=20, blank=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    selected_template = models.ForeignKey('TemplateModel', models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True)
    
    def __str__(self):
        return self.name
        
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
    TEMPLATE_TYPES=(
            ('-1', 'None'),
            ('00', 'File'),
            ('01', 'Runtime'),
            )
    template_type = models.CharField(max_length=2, choices=TEMPLATE_TYPES, default='00')
    template_path = models.FilePathField(path=os.path.join(BASE_DIR, 'gui/templates'), recursive=True, allow_folders=False, blank=True, null=True)
    meta_tags = models.ManyToManyField(tags.HtmlTag, related_name='+', blank=True, default=None, limit_choices_to={'tag_name__contains':'Meta'})
    page_icon_tag = models.ForeignKey(tags.IconTag, models.SET_NULL, blank = True, null = True, default=None)
    title_tag = models.ForeignKey(tags.HtmlTag, models.SET_NULL, blank = True, null = True, default=None, limit_choices_to={'tag_name__contains':'Title'})
    header_script_tags = models.ManyToManyField(tags.ScriptTag, blank=True, default=None, related_name='+')
    header_style_tags = models.ManyToManyField(tags.StyleTag, blank=True, related_name='+', default=None)
    template_applied_on = models.ForeignKey(ControlModel, models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Template"
        verbose_name_plural = "Templates"

class StyleModel(iot.BaseModel):    
    style_type = models.CharField(max_length=255)
    style_path = models.FilePathField(path=os.path.join(BASE_DIR, 'staticfiles/css'), recursive=True, allow_folders=False, blank=True, null=True)
    style_applied_on = models.ForeignKey(ControlModel, models.SET_NULL, blank = True, null = True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "Style"
        verbose_name_plural = "Styles"

class ContentControlModel(ControlModel):        
    template = models.ForeignKey(TemplateModel, models.SET_NULL, blank = True, null = True)
    style = models.ForeignKey(StyleModel, models.SET_NULL, blank = True, null = True)
    content = models.ForeignKey('self', models.SET_NULL, blank = True, null = True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name="ContentControl"
        verbose_name_plural = "ContentControls"

class ItemsControlModel(ContentControlModel):    
    items = models.ManyToManyField(ContentControlModel, related_name = '+')
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "ItemsControl"
        verbose_name_plural = "ItemsControls"
