# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.templatetags.static import static
from IOTStudio.settings import STATIC_ROOT
from django.utils.html import format_html

def get_all_meta_tags_html(meta_tags):
    html = ''
    for meta_tag in meta_tags.all():
        html += meta_tag.get_html()
    
    return html
    
def get_all_style_tags_html(style_tags):
    html = ''
    for style_tag in style_tags.all():
        html += style_tag.get_html()
        
    return html
    
def get_all_script_tags_html(script_tags):
    html = ''
    for script_tag in script_tags.all():
        html += script_tag.get_html()
        
    return html