from __future__ import unicode_literals
from django.db import models
from .gui_models import iot
from datetime import datetime
from django.contrib.auth.models import User
from IOTStudio.settings import BASE_DIR
from .gui_models import tags
import os
from polymorphic.models import PolymorphicModel
from django.db.models.query_utils import Q

TEMPLATE_NAME = '<!-- Template Name: {0} -->'
NEW_LINE = '\n'
HTML_START = '<!DOCTYPE html>' + NEW_LINE + '<html lang="en">' + NEW_LINE
HTML_END = '</html>' + NEW_LINE
HEAD_START = '<head>' + NEW_LINE
HEAD_END = '</head>' + NEW_LINE
BODY_START = '<body>' + NEW_LINE
BODY_END = '</body>' + NEW_LINE

# Create your models here.
class ApplicationModel(iot.BaseModel):    
    is_active = models.BooleanField(default=False, help_text='Template under active app will be rendered for current app')
    version = models.CharField(max_length=20, blank=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    selected_template = models.ForeignKey('TemplateModel', models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Applications"
        verbose_name = "Application"

class Layout(iot.BaseModel):
    pass

class UIElementModel(iot.BaseModel):
    element_type = models.CharField(max_length=255)

class PanelModel(UIElementModel):
    PANEL_TYPES=(
            ('-1', 'Panel'),
            ('00', 'StackPanel'),
            ('01', 'FlowLayoutPanel'),
            ('02', 'WrapPanel'),
            ('03', 'DockPanel'),
            ('04', 'GridPanel'),
            ('05', 'AbsolutePanel'),
            ('06', 'FlyoutPanel'),
            )
    panel_type = models.CharField(max_length=2, blank = True, choices = PANEL_TYPES, default = '-1')
    parent_id = models.ForeignKey('self', models.SET_NULL, blank = True, null = True)
    children = models.ManyToManyField(UIElementModel, blank = True, related_name = '+', default = None) 
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)

    def __str__(self):
        return '{0} ({1})'.format(self.name, dict(self.PANEL_TYPES)[self.panel_type])
        
    def get_html(self):
        return ''

    class Meta:
        verbose_name = 'Panel'
        verbose_name_plural = 'Panels'

class PlaceHolderModel(iot.BaseModel):
    PLACE_HOLDER_TYPES=(
            ('-1', 'None'),
            ('00', 'HTML'),
            ('01', 'Panel'),
            )
    TAG_TYPES=(
            ('-1', 'None'),
            ('00', 'Div'),
            ('01', 'Span'),
            )
    place_holder_type = models.CharField(max_length=2, choices = PLACE_HOLDER_TYPES, default='00')
    tag_type = models.CharField(max_length=2, choices=TAG_TYPES, default='00')
    css_classes = models.CharField(max_length=100, blank=True, null=True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)

    def __str__(self):
        return '{0} ({1})'.format(self.name, dict(self.PLACE_HOLDER_TYPES)[self.place_holder_type])

    def get_html(self):
        return self.build_html()

    def build_html(self):
        return ''
        
    class Meta:
        verbose_name = 'Placeholder'
        verbose_name_plural = 'Placeholders'

class HtmlPlaceHolderModel(PlaceHolderModel):
    html_tags = models.ManyToManyField(tags.HtmlTagModel, blank = True, related_name = '+', default = None)

    def __str__(self):
        return '{0} (HtmlPlaceholder)'.format(self.name)
        
    def build_html(self):
        html = ''
        pre_tag = '<{0} id="{1}" class="{2}" >'
        post_tag = '</{0}>'
        if self.tag_type == '00':
            pre_tag = pre_tag.format('div', self.slug, self.css_classes)
            post_tag = post_tag.format('div')
        if self.tag_type == '01':
            pre_tag = pre_tag.format('span', self.slug, self.css_classes)
            post_tag = post_tag.format('span')
        if self.tag_type != '-1':
            html += pre_tag
        for html_tag in self.html_tags.all().order_by('sort_level'):
            html += html_tag.get_html()
            
        if self.tag_type != '-1':
            html += post_tag

        return html

    class Meta:
        verbose_name = 'HtmlPlaceholder'
        verbose_name_plural = 'HtmlPlaceholders'

class PanelPlaceHolderModel(PlaceHolderModel):
    panels = models.ManyToManyField(PanelModel, blank = True, related_name = '+', default = None)

    def __str__(self):
        return '{0} (PanelPlaceholder)'.format(self.name)

    def build_html(self):
        html = ''
        for panel in self.panels.all().order_by('sort_level'):
            html += panel.get_html()
            
        return html
        
    class Meta:
        verbose_name = 'PanelPlaceholder'
        verbose_name_plural = 'PanelPlaceholders'

class SectionModel(iot.BaseModel):
    TAG_TYPES=(
            ('-1', 'None'),
            ('00', 'Div'),
            ('01', 'Span'),
            )
    tag_type = models.CharField(max_length=2, choices=TAG_TYPES, default='00')
    css_classes = models.CharField(max_length=100, blank=True, null=True)
    header_html = models.TextField(null = True, blank = True)
    place_holders = models.ManyToManyField(PlaceHolderModel, blank = True, related_name = '+', default = None, help_text = 'Each section consist of 0 or more place holders of type HTML or panel')
    footer_html = models.TextField(null = True, blank = True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)

    def __str__(self):
        return self.name
        
    def get_html(self):
        html = ''
        pre_tag = '<{0} id="{1}" class="{2}" >'
        post_tag = '</{0}>'
        if self.tag_type == '00':
            pre_tag = pre_tag.format('div', self.slug, self.css_classes)
            post_tag = post_tag.format('div')
        if self.tag_type == '01':
            pre_tag = pre_tag.format('span', self.slug, self.css_classes)
            post_tag = post_tag.format('span')
        if self.tag_type != '-1':
            html += pre_tag
        html += ('' if self.header_html is None else self.header_html) + NEW_LINE
        for place_holder in self.place_holders.all().order_by('sort_level'):
            html += place_holder.get_html()
            
        html += ('' if self.footer_html is None else self.footer_html) + NEW_LINE
        if self.tag_type != '-1':
            html += post_tag
        return html

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

class TemplateBlockModel(iot.BaseModel):
    TAG_TYPES=(
            ('-1', 'None'),
            ('00', 'Div'),
            ('01', 'Span'),
            ('02', 'Header'),
            ('03', 'Main'),
            )
    tag_type = models.CharField(max_length=2, choices=TAG_TYPES, default='00')
    css_classes = models.CharField(max_length=100, blank=True, null=True)
    allow_change_in_child = models.BooleanField(default=False, help_text='If checked, block can be overwritten by child templates')
    header_html = models.TextField(null = True, blank = True)
    sections = models.ManyToManyField(SectionModel, blank = True, related_name='+', default=None, help_text='Each block consist of 0 or more sections')
    child_blocks = models.ManyToManyField('self', blank=True, related_name='+', default=None)
    footer_html = models.TextField(null = True, blank = True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)

    def __str__(self):
        return self.name

    def get_html(self):
        html = ''
        pre_tag = '<{0} id="{1}" class="{2}" >' + NEW_LINE          
        post_tag = '</{0}>'
        if self.tag_type == '00':
            pre_tag = pre_tag.format('div', self.slug, self.css_classes)
            post_tag = post_tag.format('div')
        if self.tag_type == '01':
            pre_tag = pre_tag.format('span', self.slug, self.css_classes)
            post_tag = post_tag.format('span')
        if self.tag_type == '02':
            pre_tag = pre_tag.format('header', self.slug, self.css_classes)
            post_tag = post_tag.format('header')
        if self.tag_type == '03':
            pre_tag = pre_tag.format('main', self.slug, self.css_classes)
            post_tag = post_tag.format('main')
        if self.tag_type != '-1':
            html += pre_tag
        html += ('' if self.header_html is None else self.header_html) + NEW_LINE
        for section in self.sections.all().order_by('sort_level'):
            html += section.get_html()
        for child_block in self.child_blocks.all().order_by('sort_level'):
            html += child_block.get_html()
            
        html += ('' if self.footer_html is None else self.footer_html) + NEW_LINE
        if self.tag_type != '-1':
            html += post_tag + NEW_LINE
        return html
        
    class Meta:
        verbose_name = 'Block'
        verbose_name_plural = 'Blocks'

class TemplateModel(iot.BaseModel):    
    TEMPLATE_TYPES=(
            ('-1', 'None'),
            ('00', 'File'),
            ('01', 'Runtime'),
            )
    template_type = models.CharField(max_length=2, choices=TEMPLATE_TYPES, default='00')
    template_path = models.FilePathField(path=os.path.join(BASE_DIR, 'gui/templates'), recursive=True, allow_folders=False, blank=True, null=True)
    meta_tags = models.ManyToManyField(tags.HtmlTagModel, related_name='+', blank=True, default=None, limit_choices_to={'tag_name__contains':'Meta'})
    page_icon_tag = models.ForeignKey(tags.IconTagModel, models.SET_NULL, blank = True, null = True, default=None)
    title_tag = models.ForeignKey(tags.HtmlTagModel, models.SET_NULL, blank = True, null = True, default=None, limit_choices_to={'tag_name__contains':'Title'})
    script_tags = models.ManyToManyField(tags.ScriptTagModel, blank=True, default=None, related_name='+')
    style_tags = models.ManyToManyField(tags.StyleTagModel, blank=True, related_name='+', default=None)
    block_tags = models.ManyToManyField(TemplateBlockModel, blank = True, related_name='+', default=None)
    template_applied_on = models.ForeignKey('ControlModel', models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)
    
    def __str__(self):
        return '{0} ({1})'.format(self.name, dict(self.TEMPLATE_TYPES)[self.template_type])

    def get_html(self, request, context):
        if self.template_type == '00':
            return shortcuts.render(request, self.template_path.lstrip('\\'), context)
        
        if self.template_type == '01':
            #start HTML tag
            html = TEMPLATE_NAME.format(self.name)
            html += HTML_START        
            #start Head tag
            html += HEAD_START        
            #Render all meta tags if available        
            for meta_tag in self.meta_tags.all().order_by('sort_level'):
                html += meta_tag.get_html()
                
            html += NEW_LINE
            
            #Render page-icon-tag
            html += self.page_icon_tag.get_html('page_icon') + NEW_LINE        
            #Render title-tag 
            html += self.title_tag.get_html() + NEW_LINE        
            #Render header-script-tags
            if self.script_tags.filter(position='00').exists():
                for script_tag in self.script_tags.filter(position='00').order_by('sort_level'):
                    html += script_tag.get_html()
                
                html += NEW_LINE
            
            #Render header-style-tags        
            for style_tag in self.style_tags.all().order_by('sort_level'):
                html += style_tag.get_html()
            
            html += NEW_LINE
            
            #End Head tag
            html += HEAD_END        
            #Body start tag
            html += BODY_START + NEW_LINE        
            #Render all blocks        
            for block_tag in self.block_tags.all().order_by('sort_level'):
                html += block_tag.get_html()
            
            html += NEW_LINE

            #Render body script tags
            if self.script_tags.filter(position='01').exists():
                for body_script in self.script_tags.filter(position='01').order_by('sort_level'):
                    html += body_script.get_html()

                html += NEW_LINE

            #Body end tag
            html += BODY_END        
            #HTML end tag
            html += HTML_END
            
        return html
        
    class Meta:
        verbose_name = "Template"
        verbose_name_plural = "Templates"

class ControlModel(UIElementModel):    
    control_type = models.CharField(max_length=255)
    parent_id = models.ForeignKey('self', models.SET_NULL, blank=True, null=True)
    
class ControlStyleModel(iot.BaseModel):
    STYLES=(
            ('-1', 'None'),
            ('00', 'File'),
            ('01', 'Inline'),
            )
    style_type = models.CharField(max_length=2, choices=STYLES, default='01')
    style_path = models.FilePathField(path=os.path.join(BASE_DIR, 'staticfiles/css'), recursive=True, allow_folders=False, blank=True, null=True)
    style_applied_on = models.ForeignKey(ControlModel, models.SET_NULL, blank = True, null = True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)
    
    def __str__(self):
        return '{0} ({1})'.format(self.name, dict(self.STYLES)[self.style_type])
        
    class Meta:
        verbose_name = 'ControlStyle'
        verbose_name_plural = 'ControlStyles'

class ContentControlModel(ControlModel):    
    template = models.ForeignKey(TemplateModel, models.SET_NULL, blank = True, null = True)
    style = models.ForeignKey(ControlStyleModel, models.SET_NULL, blank = True, null = True)
    content = models.ManyToManyField(TemplateBlockModel, related_name='+', blank = True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name="ContentControl"
        verbose_name_plural = "ContentControls"

class ItemsControlModel(ContentControlModel):    
    items = models.ManyToManyField(ContentControlModel, related_name = '+')
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "ItemsControl"
        verbose_name_plural = "ItemsControls"
