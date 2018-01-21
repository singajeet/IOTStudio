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

NONE = 'None'
DIV = 'Div'
SPAN = 'Span'
NAV = 'nav'
HEADER = 'header'
MAIN = 'main'
HTML = 'Html'
ASIDE = 'aside'
FOOTER = 'footer'
PANEL = 'Panel'
STACK_PANEL = 'StackPanel'
FLOW_LAYOUT_PANEL = 'FlowLayoutPanel'
WRAP_PANEL = 'WrapPanel'
DOCK_PANEL = 'DockPanel'
GRID_PANEL = 'GridPanel'
ABSOLUTE_PANEL = 'AbsolutePanel'
FLYOUT_PANEL = 'FlyoutPanel'

SORT_LEVEL = 'sort_level'

FILE = 'File'
RUNTIME = 'Runtime'
PAGE_ICON = 'page_icon'
INLINE = 'Inline'

_MINUS_1 = '-1'
_00 = '00'
_01 = '01'
_02 = '02'
_03 = '03'
_04 = '04'
_05 = '05'
_06 = '06'

START_TAG_TEMPLATE = '<{0} id="{1}" class="{2}" >'
END_TAG_TEMPLATE = '</{0}>'

TEMPLATE_NAME = '<!-- Template Name: {0} -->'
NEW_LINE = '\n'
HTML_START = NEW_LINE + '<!DOCTYPE html>' + NEW_LINE + '<html lang="en">' + NEW_LINE
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
            (_MINUS_1, PANEL),
            (_00, STACK_PANEL),
            (_01, FLOW_LAYOUT_PANEL),
            (_02, WRAP_PANEL),
            (_03, DOCK_PANEL),
            (_04, GRID_PANEL),
            (_05, ABSOLUTE_PANEL),
            (_06, FLYOUT_PANEL),
            )
    panel_type = models.CharField(max_length=2, blank = True, choices = PANEL_TYPES, default = _MINUS_1)
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
            (_MINUS_1, NONE),
            (_00, HTML),
            (_01, PANEL),
            )
    TAG_TYPES=(
            (_MINUS_1, NONE),
            (_00, DIV),
            (_01, SPAN),
            )
    place_holder_type = models.CharField(max_length=2, choices = PLACE_HOLDER_TYPES, default=_00)
    tag_type = models.CharField(max_length=2, choices=TAG_TYPES, default=_00)
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
        pre_tag = START_TAG_TEMPLATE
        post_tag = END_TAG_TEMPLATE
        if self.tag_type == _00:
            pre_tag = pre_tag.format(DIV, self.slug, self.css_classes)
            post_tag = post_tag.format(DIV)
        if self.tag_type == _01:
            pre_tag = pre_tag.format(SPAN, self.slug, self.css_classes)
            post_tag = post_tag.format(SPAN)
        if self.tag_type != _MINUS_1:
            html += pre_tag
        for html_tag in self.html_tags.all().order_by(SORT_LEVEL):
            html += html_tag.get_html()
            
        if self.tag_type != _MINUS_1:
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
        for panel in self.panels.all().order_by(SORT_LEVEL):
            html += panel.get_html()
            
        return html
        
    class Meta:
        verbose_name = 'PanelPlaceholder'
        verbose_name_plural = 'PanelPlaceholders'

class SectionModel(iot.BaseModel):
    TAG_TYPES=(
            (_MINUS_1, NONE),
            (_00, DIV),
            (_01, SPAN),
            (_02, HEADER),
            (_03, MAIN),
            (_04, NAV),
            (_05, ASIDE),
            (_06, FOOTER),
            )
    tag_type = models.CharField(max_length=2, choices=TAG_TYPES, default=_00)
    css_classes = models.CharField(max_length=100, blank=True, null=True)
    header_html = models.TextField(null = True, blank = True)
    place_holders = models.ManyToManyField(PlaceHolderModel, blank = True, related_name = '+', default = None, help_text = 'Each section consist of 0 or more place holders of type HTML or panel')
    footer_html = models.TextField(null = True, blank = True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)

    def __str__(self):
        return self.name
        
    def get_html(self):
        html = ''
        html += '<!-- Start [{0}] Section -->'.format(self.name) + NEW_LINE
        pre_tag = START_TAG_TEMPLATE + NEW_LINE
        post_tag = END_TAG_TEMPLATE
        if self.tag_type == _00:
            pre_tag = pre_tag.format(DIV, self.slug, self.css_classes)
            post_tag = post_tag.format(DIV)
        if self.tag_type == _01:
            pre_tag = pre_tag.format(SPAN, self.slug, self.css_classes)
            post_tag = post_tag.format(SPAN)
        if self.tag_type == _02:
            pre_tag = pre_tag.format(HEADER, self.slug, self.css_classes)
            post_tag = post_tag.format(HEADER)
        if self.tag_type == _03:
            pre_tag = pre_tag.format(MAIN, self.slug, self.css_classes)
            post_tag = post_tag.format(MAIN)
        if self.tag_type == _04:
            pre_tag = pre_tag.format(NAV, self.slug, self.css_classes)
            post_tag = post_tag.format(NAV)
        if self.tag_type == _05:
            pre_tag = pre_tag.format(ASIDE, self.slug, self.css_classes)
            post_tag = post_tag.format(ASIDE)
        if self.tag_type == _06:
            pre_tag = pre_tag.format(FOOTER, self.slug, self.css_classes)
            post_tag = post_tag.format(FOOTER)
        if self.tag_type != _MINUS_1:
            html += pre_tag
        #render header html if provided
        html += '' if (self.header_html is None or self.header_html == '') else (self.header_html + NEW_LINE)
        #render all place holders
        for place_holder in self.place_holders.all().order_by(SORT_LEVEL):
            html += place_holder.get_html()
        #Render new line if place holders were rendered
        if self.place_holders.count() > 0:
            html += NEW_LINE
        #render footer html if provided
        html += '' if (self.footer_html is None or self.footer_html == '') else (self.footer_html + NEW_LINE)
        if self.tag_type != _MINUS_1:
            html += post_tag + NEW_LINE
            
        html += '<!-- End [{0}] Section -->'.format(self.name)
        return html

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

class TemplateBlockModel(iot.BaseModel):
    TAG_TYPES=(
            (_MINUS_1, NONE),
            (_00, DIV),
            (_01, SPAN),
            (_02, HEADER),
            (_03, MAIN),
            (_04, NAV),
            (_05, ASIDE),
            (_06, FOOTER),
            )
    tag_type = models.CharField(max_length=2, choices=TAG_TYPES, default=_00)
    css_classes = models.CharField(max_length=100, blank=True, null=True)
    allow_change_in_child = models.BooleanField(default=False, help_text='If checked, block can be overwritten by child templates')
    header_html = models.TextField(null = True, blank = True)
    sections = models.ManyToManyField(SectionModel, blank = True, related_name='+', default=None, help_text='Each block consist of 0 or more sections')
    child_blocks = models.ManyToManyField('self', blank=True, related_name='+', symmetrical = False, default=None)
    footer_html = models.TextField(null = True, blank = True)
    author = models.ForeignKey(User, models.SET_NULL, blank = True, null = True)

    def __str__(self):
        return self.name

    def get_html(self):
        html = ''
        #Render comment with block name
        html += '<!-- Start [{0}] Block -->'.format(self.name) + NEW_LINE
        #Render Pre/Post tags as containers for this block 
        pre_tag = START_TAG_TEMPLATE + NEW_LINE          
        post_tag = END_TAG_TEMPLATE
        #Based on type of HTML tag selected, the pre part of block will be prepared to render
        if self.tag_type == _00:
            pre_tag = pre_tag.format(DIV, self.slug, self.css_classes)
            post_tag = post_tag.format(DIV)
        if self.tag_type == _01:
            pre_tag = pre_tag.format(SPAN, self.slug, self.css_classes)
            post_tag = post_tag.format(SPAN)
        if self.tag_type == _02:
            pre_tag = pre_tag.format(HEADER, self.slug, self.css_classes)
            post_tag = post_tag.format(HEADER)
        if self.tag_type == _03:
            pre_tag = pre_tag.format(MAIN, self.slug, self.css_classes)
            post_tag = post_tag.format(MAIN)
        if self.tag_type == _04:
            pre_tag = pre_tag.format(NAV, self.slug, self.css_classes)
            post_tag = post_tag.format(NAV)
        if self.tag_type == _05:
            pre_tag = pre_tag.format(ASIDE, self.slug, self.css_classes)
            post_tag = post_tag.format(ASIDE)
        if self.tag_type == _06:
            pre_tag = pre_tag.format(FOOTER, self.slug, self.css_classes)
            post_tag = post_tag.format(FOOTER)
        #if a valid html tag is selected, render it else nothing is rendered
        if self.tag_type != _MINUS_1:
            html += pre_tag
        #render the header  part of block if any html is provided in admin
        html += '' if (self.header_html is None or self.header_html == '') else (self.header_html + NEW_LINE)
        #render all the sections under this block if available
        for section in self.sections.all().order_by(SORT_LEVEL):
            html += section.get_html()
        #if sections were rendered, print a NewLine to have child blocks rendered in next line
        if self.sections.count() > 0:
            html += NEW_LINE
        #render all child blocks if available
        for child_block in self.child_blocks.all().order_by(SORT_LEVEL):
            html += child_block.get_html()
        #if child blocks were rendered, print a NewLine to have footer rendered in next line
        if self.child_blocks.count() > 0:
            html += NEW_LINE    
        html += '' if (self.footer_html is None or self.footer_html == '') else (self.footer_html + NEW_LINE)
        if self.tag_type != _MINUS_1:
            html += post_tag + NEW_LINE
        
        html += '<!-- End [{0}] Block -->'.format(self.name) + NEW_LINE
        return html
        
    class Meta:
        verbose_name = 'Block'
        verbose_name_plural = 'Blocks'

class TemplateModel(iot.BaseModel):    
    TEMPLATE_TYPES=(
            (_MINUS_1, NONE),
            (_00, FILE),
            (_01, RUNTIME),
            )
    template_type = models.CharField(max_length=2, choices=TEMPLATE_TYPES, default=_00)
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
        if self.template_type == _00:
            return shortcuts.render(request, self.template_path.lstrip('\\'), context)
        
        if self.template_type == _01:
            #start HTML tag
            html = TEMPLATE_NAME.format(self.name)
            html += HTML_START        
            #start Head tag
            html += HEAD_START        
            #Render all meta tags if available        
            for meta_tag in self.meta_tags.all().order_by(SORT_LEVEL):
                html += meta_tag.get_html()
                
            html += NEW_LINE
            
            #Render page-icon-tag
            html += self.page_icon_tag.get_html(PAGE_ICON) + NEW_LINE        
            #Render title-tag 
            html += self.title_tag.get_html() + NEW_LINE        
            #Render header-script-tags
            if self.script_tags.filter(position=_00).exists():
                for script_tag in self.script_tags.filter(position=_00).order_by(SORT_LEVEL):
                    html += script_tag.get_html()
                
                html += NEW_LINE
            
            #Render header-style-tags        
            for style_tag in self.style_tags.all().order_by(SORT_LEVEL):
                html += style_tag.get_html()
            
            html += NEW_LINE
            
            #End Head tag
            html += HEAD_END        
            #Body start tag
            html += BODY_START + NEW_LINE        
            #Render all blocks        
            for block_tag in self.block_tags.all().order_by(SORT_LEVEL):
                html += block_tag.get_html()
            
            html += NEW_LINE

            #Render body script tags
            if self.script_tags.filter(position=_01).exists():
                for body_script in self.script_tags.filter(position=_01).order_by(SORT_LEVEL):
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
            (_MINUS_1, NONE),
            (_00, FILE),
            (_01, INLINE),
            )
    style_type = models.CharField(max_length=2, choices=STYLES, default=_01)
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
