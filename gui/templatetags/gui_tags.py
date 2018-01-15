
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
    html_tag = get_object_or_404(tags.HtmlTag, tag_name='Title')
    return format_html(html_tag.tag_text, title_text)

@register.simple_tag
def style(style_name):
    style_tag = get_object_or_404(tags.StyleTag, tag_name=style_name)
    return format_html('<link href="{0}" rel="stylesheet" />'.format(static(style_tag.style_text)))

@register.simple_tag
def script(script_name):
    script_tag = get_object_or_404(tags.ScriptTag, tag_name=script_name)
    return format_html('<script src="{0}" type="application/javascript" />' . format(static(script_tag.script_text)))

