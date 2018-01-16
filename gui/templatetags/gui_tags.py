
from __future__ import unicode_literals
from ..gui_models import tags
from django import template
from django.utils.html import format_html
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe
from django.templatetags.static import static
from IOTStudio.settings import STATIC_ROOT

register = template.Library()

@register.simple_tag
def title(title_text):
    if title_text is None:
        return '-EmptyTitle-'
        
    html_tag = get_object_or_404(tags.HtmlTag, tag_name='Title')
    if html_tag is None:
        return '-EmptyTitle-'
        
    return format_html(('<!-- TitleTag -->\n\t<title>{0}</title>'.format(html_tag.tag_text)), title_text)

@register.simple_tag
def style(style_name):
    if style_name is not None:
        style_tag = get_object_or_404(tags.StyleTag, tag_name=style_name)
        if style_tag is not None and style_tag.style_type == '00':
            file_name = style_tag.style_file.replace(STATIC_ROOT, '')            
            return format_html('<!-- StyleTag -->\n\t<link href="{0}" rel="stylesheet" />'.format(static(file_name)))
        
        if style_tag is not None and style_tag.style_type == '01':
            return format_html('<!-- StyleTag -->\n\t<style>\n\t{0}\n\t</style>'.format(style_tag.style_text))
            
    return None
    
@register.simple_tag
def script(script_name):
    if script_name is not None:
        script_tag = get_object_or_404(tags.ScriptTag, tag_name=script_name)
        
        if script_tag is not None and script_tag.script_type == '00':
            file_name = script_tag.script_file.replace(STATIC_ROOT, '')
            return format_html('<!-- ScriptTag -->\n\t<script src="{0}" type="application/javascript"></script>' . format(static(file_name)))

        if script_tag is not None and script_tag.script_type == '01':
            return format_html('<!-- ScriptTag -->\n\t<script>\n\t{0}\n\t</script>'.format(script_tag.script_text))
            
        if script_tag is not None and script_tag.script_type == '02':
            return format_html('<!-- ScriptTag -->\n\t<script src="{0}" type="application/javascript"></script>' . format(script_tag.script_url))

    return None

@register.simple_tag
def meta():
    meta_tag = get_object_or_404(tags.HtmlTag, tag_name='Meta')
    if meta_tag is not None:
        return format_html('<!-- MetaTag -->\n\t{0}'.format(meta_tag.tag_text))

@register.simple_tag
def page_icon(icon_name):
    icon_tag = get_object_or_404(tags.IconTag, tag_name=icon_name)
    
    if icon_tag is not None and icon_tag.icon_type == '00':
        file_name = icon_tag.icon_file.replace(STATIC_ROOT, '')
        return format_html('<!-- PageIconTag -->\n\t<link rel="shortcut icon" href="{0}" />'.format(static(file_name)))
    
    if icon_tag is not None and icon_tag.icon_type == '01':
        return format_html('<!-- PageIconTag -->\n\t{0}'.format(icon_tag.icon_text))
        
    return None