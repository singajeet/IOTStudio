
from __future__ import unicode_literals
from ..gui_models import tags
from django import template
from django.utils.html import format_html
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def title(title_text):
    if title_text is None:
        return '-EmptyTitle-'
        
    html_tag = get_object_or_404(tags.HtmlTag, tag_name='Title')
    if html_tag is None:
        return '-EmptyTitle-'
        
    return format_html(html_tag.tag_text, title_text)

@register.simple_tag
def style(style_name):
    if style_name is not None:
        style_tag = get_object_or_404(tags.StyleTag, tag_name=style_name)
        if style_tag is not None:
            return format_html('<link href="{0}" rel="stylesheet" />'.format(static(style_tag.style_text)))
            
    return None
    
@register.simple_tag
def script(script_name):
    if script_name is not None:
        script_tag = get_object_or_404(tags.ScriptTag, tag_name=script_name)
        if script_tag is not None:
            return format_html('<script src="{0}" type="application/javascript" />' . format(static(script_tag.script_text)))

    return None