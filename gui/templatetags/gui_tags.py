
from __future__ import unicode_literals
from ..gui_models import tags
from django import template
from django.shortcuts import get_object_or_404
from .. import models

register = template.Library()

@register.simple_tag
def title(title_name):
    title_tag = get_object_or_404(tags.HtmlTagModel, tag_name=title_name)    
    return title_tag.get_html()

@register.simple_tag
def style(style_name):
    style_tag = get_object_or_404(tags.StyleTagModel, tag_name=style_name)    
    return style_tag.get_html()
    
@register.simple_tag
def script(script_name):
    script_tag = get_object_or_404(tags.ScriptTagModel, tag_name=script_name)        
    return script_tag.get_html()

@register.simple_tag
def meta(meta_name):
    meta_tag = get_object_or_404(tags.HtmlTagModel, tag_name=meta_name)    
    return meta_tag.get_html()

@register.simple_tag
def page_icon(icon_name):
    icon_tag = get_object_or_404(tags.IconTagModel, tag_name=icon_name)    
    return icon_tag.get_html('page_icon')
    
@register.simple_tag
def panel(panel_name, panel_type):
    panel_tag = get_object_or_404(models.PanelModel, name=panel_name)