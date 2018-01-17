# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import shortcuts
from django.http import HttpResponse
from django.template import Template, Context
from . import models
from . import utilities
# Create your views here.

TEMPLATE_NAME = '<!-- Template Name: {0} -->'
NEW_LINE = '\n'
HTML_START = '<!DOCTYPE html>' + NEW_LINE + '<html lang="en">' + NEW_LINE
HTML_END = '</html>' + NEW_LINE
HEAD_START = '<head>' + NEW_LINE
HEAD_END = '</head>' + NEW_LINE
BODY_START = '<body>' + NEW_LINE
BODY_END = '</body>' + NEW_LINE

def index(request):
    app_details = models.ApplicationModel.objects.get(id=2)
    template = models.TemplateModel.objects.get(id=app_details.selected_template.id)
    context = { 'app_details' : app_details, }
    
    if template is not None and template.template_type == '00':
        return shortcuts.render(request, template.template_path.lstrip('\\'), context)
        
    if template is not None and template.template_type == '01':
        #start HTML tag
        html = TEMPLATE_NAME.format(template.name)
        html += HTML_START
        
        #start Head tag
        html += HEAD_START
        
        #Render all meta tags if available
        html += utilities.get_all_meta_tags_html(template.meta_tags) + NEW_LINE
        
        #Render page-icon-tag
        html += utilities.get_page_icon_html(template.page_icon_tag) + NEW_LINE
        
        #Render title-tag 
        html += utilities.get_title_tag_html(template.title_tag) + NEW_LINE
        
        #Render header-script-tags
        html += utilities.get_all_script_tags_html(template.header_script_tags) + NEW_LINE
        
        #Render header-style-tags
        html += utilities.get_all_style_tags_html(template.header_style_tags)
        
        
        html += HEAD_END
        html += BODY_START
        
        html += utilities.get_all_script_tags_html(template.header_script_tags) + NEW_LINE
        html += BODY_END
        html += HTML_END
        html_template = Template(html)
        html_context = Context(context)
        return HttpResponse(html_template.render(html_context))