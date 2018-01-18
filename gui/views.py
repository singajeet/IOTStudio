# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import shortcuts
from django.http import HttpResponse
from django.template import Template, Context
from . import models
# Create your views here.



def index(request):
    app_details = models.ApplicationModel.objects.get(id=2)
    template = models.TemplateModel.objects.get(id=app_details.selected_template.id)
    context = { 'app_details' : app_details, }
    
    if template.template_type == '00':
        return template.get_html(request, context)
    
    #Compose template using context and return rendered HTML
    if template.template_type == '01':
        html = template.get_html(request, context)
        html_template = Template(html)
        html_context = Context(context)
        return HttpResponse(html_template.render(html_context))
        
    return None