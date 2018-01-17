
from __future__ import unicode_literals
from ..gui_models import tags
from django import template
from django.shortcuts import get_object_or_404
from .. import utilities

register = template.Library()

@register.simple_tag
def title(title_name):
    title_tag = get_object_or_404(tags.HtmlTag, tag_name=title_name)
    
    return utilities.get_title_tag_html(title_tag)

@register.simple_tag
def style(style_name):
    style_tag = get_object_or_404(tags.StyleTag, tag_name=style_name)
    
    return utilities.get_style_tag_html(style_tag)
    
@register.simple_tag
def script(script_name):
    script_tag = get_object_or_404(tags.ScriptTag, tag_name=script_name)
        
    return utilities.get_script_tag_html(script_tag)

@register.simple_tag
def meta(meta_name):
    meta_tag = get_object_or_404(tags.HtmlTag, tag_name=meta_name)
    
    return utilities.get_meta_tag_html(meta_tag)

@register.simple_tag
def page_icon(icon_name):
    icon_tag = get_object_or_404(tags.IconTag, tag_name=icon_name)
    
    return utilities.get_page_icon_html(icon_tag)