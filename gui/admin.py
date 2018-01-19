# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models
from .gui_models import tags
from django.contrib import admin
# Register your models here.


@admin.register(models.ApplicationModel)
class ApplicationModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_on_date', 'modified_on_date', 'is_active')
    list_filter = ['name']
    search_fields = ['name']
    empty_value_display = '-empty-'
    list_display_links = ('id', 'name')
    save_as = True

@admin.register(models.ContentControlModel)
class ContentControlModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_on_date', 'modified_on_date')
    list_filter = ['name', 'control_type', 'template', 'style']
    search_fields = ['name', 'content']
    empty_value_display = '-empty-'
    list_display_links = ('id', 'name')
    save_as = True
    
@admin.register(models.ItemsControlModel)
class ItemsControlModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_on_date', 'modified_on_date')
    list_filter = ['name', 'control_type', 'template', 'style']
    search_fields = ['name', 'content']
    empty_value_display = '-empty-'
    list_display_links = ('id', 'name')
    save_as = True

@admin.register(models.TemplateModel)
class TemplateModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_on_date', 'modified_on_date')
    list_filter = ['name', 'template_type']
    search_fields = ['name', 'template_path']
    empty_value_display = '-empty-'
    list_display_links = ('id', 'name')
    save_as = True
    
@admin.register(models.ControlStyleModel)
class ControlStyleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_on_date', 'modified_on_date')
    list_filter = ['name', 'style_type']
    search_fields = ['name', 'style_path']
    empty_value_display = '-empty-'
    list_display_links = ('id', 'name')
    save_as = True
    
@admin.register(tags.HtmlTagModel)
class HtmlTagModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name', 'author', 'created_on_date', 'modified_on_date')
    list_filter = ['tag_name', 'author']
    search_fields = ['tag_name', 'author', 'tag_text']
    empty_value_display = '-empty-'
    list_display_links = ('id', 'tag_name')
    save_as = True
    
@admin.register(tags.StyleTagModel)
class StyleTagModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name', 'author', 'created_on_date', 'modified_on_date')
    list_filter = ['tag_name', 'author']
    search_fields = ['tag_name', 'author', 'style_text']
    empty_value_display = '-empty-'
    list_display_links = ('id', 'tag_name')
    save_as = True
    
@admin.register(tags.ScriptTagModel)
class ScriptTagModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name', 'author', 'created_on_date', 'modified_on_date', 'position')
    list_filter = ['tag_name', 'author']
    search_fields = ['tag_name', 'author', 'script_text']
    empty_value_display = '-empty-'
    list_display_links = ('id', 'tag_name')
    save_as = True

@admin.register(tags.IconTagModel)
class IconTagModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name', 'author', 'created_on_date', 'modified_on_date')
    list_filter = ['tag_name', 'author']
    search_fields = ['tag_name', 'author', 'icon_text']
    empty_value_display = '-empty-'
    list_display_links = ('id', 'tag_name')
    save_as = True
    
@admin.register(models.SectionModel)
class SectionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'created_on_date', 'modified_on_date')
    list_filter = ['name', 'author']
    search_fields = ['name', 'author']
    empty_value_display = '-empty-'
    list_display_links = ('id', 'name')
    save_as = True
    
@admin.register(models.PanelPlaceHolderModel)
class PanelPlaceHolderModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'created_on_date', 'modified_on_date')
    list_filter = ['name', 'author']
    search_fields = ['name', 'author']
    empty_value_display = '-empty-'
    list_display_links = ('id', 'name')
    save_as = True
    
@admin.register(models.HtmlPlaceHolderModel)
class HtmlPlaceHolderModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'created_on_date', 'modified_on_date')
    list_filter = ['name', 'author']
    search_fields = ['name', 'author']
    empty_value_display = '-empty-'
    list_display_links = ('id', 'name')
    save_as = True
    
@admin.register(models.PanelModel)
class PanelModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'created_on_date', 'modified_on_date')
    list_filter = ['name', 'author']
    search_fields = ['name', 'author']
    empty_value_display = '-empty-'
    list_display_links = ('id', 'name')
    save_as = True
    
@admin.register(models.TemplateBlockModel)
class TemplateBlockModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'created_on_date', 'modified_on_date')
    list_filter = ['name', 'author']
    search_fields = ['name', 'author']
    empty_value_display = '-empty-'
    list_display_links = ('id', 'name')
    save_as = True
