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

class PanelModel(UIElementModel):
    PANEL_TYPES=(
            ('-1', 'Panel'),
            ('00', 'StackPanel'),
            ('01', 'FlowLayoutPanel'),
            ('02', 'WrapPanel'),
            ('03', 'DockPanel'),
            ('04', 'GridPanel'),
            ('05', 'AbsolutePanel'),
            ('06', 'FlyoutPanel'),
            )
    panel_type = models.CharField(max_length=2, blank = True, choices = PANEL_TYPES, default = '-1')
    parent_id = models.ForeignKey('self', models.SET_NULL, blank = True)
    children = models.ManyToManyField(UIElementModel, blank = True, related_name = '+', default = None) 
    author = models.ForeignKey(User, models.SET_NULL, blank = True)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.panel_type)

    class Meta:
        verbose_name = 'Panel'
        verbose_name_plural = 'Panels'

class ControlModel(UIElementModel):
    control_type = models.CharField(max_length=255)
    parent_id = models.ForeignKey('self', models.SET_NULL, blank=True, null=True)

class PlaceHolderModel(iot.BaseModel):
    PLACE_HOLDER_TYPES=(
            ('-1', 'None'),
            ('00', 'HTML'),
            ('01', 'Panel'),
            )
    place_holder_type = models.CharField(max_length=2, choices = PLACE_HOLDER_TYPES, default='00')
    author = models.ForeignKey(User, models.SET_NULL, blank = True)

    def __str__(self):
        return '{0} ({1})'.format(self.name, place_holder_type)

    class Meta:
        verbose_name = 'Placeholder'
        verbose_name_plural = 'Placeholders'

class HtmlPlaceHolderModel(PlaceHolderModel):
    html_tags = models.ManyToManyField(tags.HtmlTag, blank = True, related_name = '+', default = None)

    def __str__(self):
        return '{0} (HtmlPlaceholder)'.format(self.name)

    class Meta:
        verbose_name = 'HtmlPlaceholder'
        verbose_name_plural = 'HtmlPlaceholders'

class PanelPlaceHolderModel(PlaceHolderModel):
        panels = models.ManyToManyField(PanelModel, blank = True, related_name = '+', default = 'None')

    def __str__(self):
        return '{0} (PanelPlaceholder)'.format(self.name)

    class Meta:
        verbose_name = 'PanelPlaceholder'
        verbose_name_plural = 'PanelPlaceholders'

class SectionModel(iot.BaseModel):
    place_holders = models.ManyToManyField(PlaceHolderModel, blank = True, related_name = '+', default = None, help_text = 'Each section consist of 0 or more place holders of type HTML or panel')
    author = models.ForeignKey(User, models.SET_NULL, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

class TemplateBlockModel(iot.BaseModel):
    allow_change_in_child = models.BooleanField(default=False, help_text='If checked, block can be overwritten by child templates')
    sections = models.ManyToManyField(SectionModel, blank = True, related_name='+', default=None, help_text='Each block consist of 0 or more sections')
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Block'
        verbose_name_plural = 'Blocks'

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
   block_tags = models.ManyToManyField(TemplateBlockModel, blank = True, related_name='+', default=None)
   template_applied_on = models.ForeignKey(ControlModel, models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)
    
    def __str__(self):
        return '{0} ({1})'.format(self.name, self.template_type)
        
    class Meta:
        verbose_name = "Template"
        verbose_name_plural = "Templates"

class ControlStyleModel(iot.BaseModel):
    STYLES=(
            ('-1', 'None'),
            ('00', 'File'),
            ('01', 'Inline'),
            )
    style_type = models.CharField(max_length=2, choices=STYLES, default='01')
    style_path = models.FilePathField(path=os.path.join(BASE_DIR, 'staticfiles/css'), recursive=True, allow_folders=False, blank=True, null=True)
    style_applied_on = models.ForeignKey(ControlModel, models.SET_NULL, blank = True, null = True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)
    
    def __str__(self):
        return '{0} ({1})'.format(self.name, style_type)
        
    class Meta:
        verbose_name = 'ControlStyle'
        verbose_name_plural = 'ControlStyles'

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
