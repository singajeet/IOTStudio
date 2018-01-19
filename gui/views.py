# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import shortcuts
from django.http import HttpResponse
from django.template import Template, Context
from . import models
import sys
import textwrap
# Create your views here.


def no_app_active_msg(error_msg):
    message = str(
                    "<html>"
                        "<head>"
                            "<Title>"
                                "No Active App Found!"
                            "</Title>"
                        "</head>"
                        "<body>"
                                "<div>"
                                    "<center>"
                                        "<h2>Unable to locate active App!</h2>"
                                    "</center>"
                                "</div>"
                                "<div>"
                                    "<center>"
                                        "<div><h4>Please check your system <a href=\"/admin\">settings</a></h4></div>"
                                        "<div><h4>and below message for more information...</h4></div>"
                                        "<div>"
                                        "</div>"
                                    "</center>"
                                "</div>"
                            "</body>"
                    "</html>"
                    )
    return message
                    
def index(request):
    try:
        app_details = models.ApplicationModel.objects.get(is_active=True)
    except:
        return no_app_active_msg(sys.exc_info()[0])
        
    if app_details is not None:
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
    else:
        return no_app_active_msg(sys.exc_info()[0])
        
    return no_app_active_msg(sys.exc_info()[0])