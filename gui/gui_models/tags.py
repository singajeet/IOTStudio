# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import os
from IOTStudio.settings import BASE_DIR
from IOTStudio.settings import STATIC_ROOT
from django.utils.html import format_html
from django.templatetags.static import static
from . import iot


class HtmlTagModel(models.Model):
    TAG_TYPES=(
            ('-1', 'None'),
            ('00', 'Div'),
            ('00', 'Span'),
            )
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255, unique = True)
    tag_text = models.TextField()
    sort_level = models.IntegerField(default=0)
    slug = models.SlugField(max_length=300, unique = True, blank = True, null = True)
    tag_type = models.CharField(max_length=2, choices=TAG_TYPES, default='-1')
    css_classes = models.CharField(max_length=100, blank=True, null=True) 
    created_on_date = models.DateTimeField(auto_now_add = True, editable = False)    
    modified_on_date = models.DateTimeField(auto_now = True, editable = False)
    author = models.ForeignKey(User, blank=True, null=True)
    security_id = models.ForeignKey(iot.SecurityIdModel, models.SET_NULL, blank = True, null = True)
    
    def __str__(self):
        return self.tag_name
        
    def get_html(self):
        return format_html('\n\t<!-- {0} -->\n\t{1}'.format(self.tag_name, self.tag_text))

    class Meta:
        verbose_name ='HtmlTag'
        verbose_name_plural = 'HtmlTags'
        

class StyleTagModel(models.Model):
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
    sort_level = models.IntegerField(default=0)
    slug = models.SlugField(max_length=300, unique = True, blank = True, null = True)
    created_on_date = models.DateTimeField(auto_now_add = True, editable = False)
    modified_on_date = models.DateTimeField(auto_now = True, editable = False)
    author = models.ForeignKey(User, blank=True, null=True)
    security_id = models.ForeignKey(iot.SecurityIdModel, models.SET_NULL, blank = True, null = True)
    
    def __str__(self):
        return '{0} ({1})'.format(self.tag_name, dict(self.STYLE_TYPES)[self.style_type])
        
    def get_html(self):
        if self.style_type == '00':
            file_name = self.style_file.replace(STATIC_ROOT, '')            
            return format_html('\n\t<!-- {0} -->\n\t<link href="{1}" rel="stylesheet" />'.format(self.tag_name, static(file_name)))
        
        if self.style_type == '01':
            return format_html('\n\t<!-- {0} -->\n\t<style>\n\t{1}\n\t</style>'.format(self.tag_name, self.style_text))
            
        return None

    class Meta:
        verbose_name = 'StyleTag'
        verbose_name_plural = 'StyleTags'
        

class ScriptTagModel(models.Model):
    SCRIPT_TYPES=(
            ('-1', 'None'),
            ('00', 'File'),
            ('01', 'Inline'),
            ('02', 'Url'),
            )
    POSITIONS=(
            ('-1', 'None'),
            ('00', 'Header'),
            ('01', 'Body'),
            )
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255, unique = True)
    position = models.CharField(max_length=2, default = '00', choices=POSITIONS)
    script_type = models.CharField(max_length = 2, choices=SCRIPT_TYPES, default='02')
    script_url = models.URLField(max_length=255, blank=True, null=True, help_text='Url to CDN location')
    script_file = models.FilePathField(path=os.path.join(BASE_DIR, 'staticfiles/js'), recursive=True, allow_folders=False, blank=True, null=True)
    script_text = models.TextField(blank=True, null=True)
    sort_level = models.IntegerField(default=0)
    created_on_date = models.DateTimeField(auto_now_add = True, editable = False)
    modified_on_date = models.DateTimeField(auto_now = True, editable = False)
    author = models.ForeignKey(User, blank=True, null=True)
    security_id = models.ForeignKey(iot.SecurityIdModel, models.SET_NULL, blank = True, null = True)
    
    def __str__(self):
        return '{0} ({1})'.format(self.tag_name, dict(self.SCRIPT_TYPES)[self.script_type])
        
    def get_html(self):
        if self.script_type == '00':
            file_name = self.script_file.replace(STATIC_ROOT, '')
            return format_html('\n\t<!-- {0} -->\n\t<script src="{1}" type="application/javascript"></script>' . format(self.tag_name, static(file_name)))

        if self.script_type == '01':
            return format_html('\n\t<!-- {0} -->\n\t<script>\n\t{1}\n\t</script>'.format(self.tag_name, self.script_text))
            
        if self.script_type == '02':
            return format_html('\n\t<!-- {0} -->\n\t<script src="{1}" type="application/javascript"></script>' . format(self.tag_name, self.script_url))

        return None

    class Meta:
        verbose_name = 'ScriptTag'
        verbose_name_plural = 'ScriptTags'

        
class IconTagModel(models.Model):
    ICON_TYPES = (
        ('-1', 'None'),
        ('00', 'File'),
        ('01', 'Inline'),
    )
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255, unique = True)
    icon_type = models.CharField(max_length = 2, choices=ICON_TYPES, default='00')
    icon_file = models.FilePathField(path=os.path.join(BASE_DIR, 'staticfiles/img'), recursive=True, allow_folders=False, blank=True, null=True)
    icon_text = models.TextField(blank=True, null=True)
    sort_level = models.IntegerField(default=0)
    slug = models.SlugField(max_length=300, unique = True, blank = True, null = True)
    created_on_date = models.DateTimeField(auto_now_add = True, editable = False)
    modified_on_date = models.DateTimeField(auto_now = True, editable = False)
    author = models.ForeignKey(User, blank=True, null=True)
    security_id = models.ForeignKey(iot.SecurityIdModel, models.SET_NULL, blank = True, null = True)
    
    def __str__(self):
        return '{0} ({1})'.format(self.tag_name, dict(self.ICON_TYPES)[self.icon_type])
        
    def get_html(self, for_element):
        if for_element == 'page_icon':
            if self.icon_type == '00':
                file_name = self.icon_file.replace(STATIC_ROOT, '')
                return format_html('\n\t<!-- {0} -->\n\t<link rel="shortcut icon" href="{1}" />'.format(self.tag_name, static(file_name)))
    
            if self.icon_type == '01':
                return format_html('\n\t<!-- {0} -->\n\t{1}'.format(self.tag_name, self.icon_text))
                
        return None

    class Meta:
        verbose_name = 'IconTag'
        verbose_name_plural = 'IconTags'
        
