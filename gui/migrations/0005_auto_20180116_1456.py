# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-16 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0004_auto_20180116_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='scripttag',
            name='script_file',
            field=models.FilePathField(blank=True, null=True, path='/data/data/com.termux/files/home/projects/python/django/IOTStudio/IOTStudio/staticfiles/js', recursive=True),
        ),
        migrations.AddField(
            model_name='scripttag',
            name='script_type',
            field=models.CharField(choices=[('-1', 'None'), ('00', 'File'), ('01', 'Inline')], default='00', max_length=2),
        ),
        migrations.AddField(
            model_name='styletag',
            name='style_file',
            field=models.FilePathField(blank=True, null=True, path='/data/data/com.termux/files/home/projects/python/django/IOTStudio/IOTStudio/staticfiles/css', recursive=True),
        ),
        migrations.AddField(
            model_name='styletag',
            name='style_type',
            field=models.CharField(choices=[('-1', 'None'), ('00', 'File'), ('01', 'Inline')], default='00', max_length=2),
        ),
        migrations.AlterField(
            model_name='stylemodel',
            name='style_path',
            field=models.FilePathField(blank=True, null=True, path='/data/data/com.termux/files/home/projects/python/django/IOTStudio/IOTStudio/staticfiles/css', recursive=True),
        ),
        migrations.AlterField(
            model_name='templatemodel',
            name='template_path',
            field=models.FilePathField(blank=True, null=True, path='/data/data/com.termux/files/home/projects/python/django/IOTStudio/IOTStudio/gui/templates', recursive=True),
        ),
    ]
