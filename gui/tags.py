
from __future__ import unicode_literals
from .gui_models import tags
from django import template

register = template.Library()

@register.simple_tag
def title(title_text):
    html_tag = tags.HtmlTags.objects.get(tag_name='Title')

