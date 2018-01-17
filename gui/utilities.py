# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.templatetags.static import static
from IOTStudio.settings import STATIC_ROOT
from django.utils.html import format_html

def get_page_icon_html(icon_tag):
    if icon_tag is not None and icon_tag.icon_type == '00':
        file_name = icon_tag.icon_file.replace(STATIC_ROOT, '')
        return format_html('\n\t<!-- PageIconTag -->\n\t<link rel="shortcut icon" href="{0}" />'.format(static(file_name)))
    
    if icon_tag is not None and icon_tag.icon_type == '01':
        return format_html('\n\t<!-- PageIconTag -->\n\t{0}'.format(icon_tag.icon_text))
        
    return None
    
def get_meta_tag_html(meta_tag):
    if meta_tag is not None:
        return format_html('\n\t<!-- MetaTag -->\n\t{0}'.format(meta_tag.tag_text))
    
    return ''
        
def get_all_meta_tags_html(meta_tags):
    html = ''
    for meta_tag in meta_tags.all():
        html += get_meta_tag_html(meta_tag)
    
    return html
    
def get_title_tag_html(title_tag):
    if title_tag is None:
        return '\n\t<!-- EmptyTitle -->'
        
    return format_html('\n\t<!-- TitleTag -->\n\t<title>{0}</title>'.format(title_tag.tag_text))
    
def get_style_tag_html(style_tag):
    if style_tag is not None and style_tag.style_type == '00':
        file_name = style_tag.style_file.replace(STATIC_ROOT, '')            
        return format_html('\n\t<!-- StyleTag -->\n\t<link href="{0}" rel="stylesheet" />'.format(static(file_name)))
        
    if style_tag is not None and style_tag.style_type == '01':
        return format_html('\n\t<!-- StyleTag -->\n\t<style>\n\t{0}\n\t</style>'.format(style_tag.style_text))
            
    return None
    
def get_all_style_tags_html(style_tags):
    html = ''
    for style_tag in style_tags.all():
        html += get_style_tag_html(style_tag)
        
    return html
    
def get_script_tag_html(script_tag):
    if script_tag is not None and script_tag.script_type == '00':
        file_name = script_tag.script_file.replace(STATIC_ROOT, '')
        return format_html('\n\t<!-- ScriptTag -->\n\t<script src="{0}" type="application/javascript"></script>' . format(static(file_name)))

    if script_tag is not None and script_tag.script_type == '01':
        return format_html('\n\t<!-- ScriptTag -->\n\t<script>\n\t{0}\n\t</script>'.format(script_tag.script_text))
            
    if script_tag is not None and script_tag.script_type == '02':
        return format_html('\n\t<!-- ScriptTag -->\n\t<script src="{0}" type="application/javascript"></script>' . format(script_tag.script_url))

    return None
    
def get_all_script_tags_html(script_tags):
    html = ''
    for script_tag in script_tags.all():
        html += get_script_tag_html(script_tag)
        
    return html