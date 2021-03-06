# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-16 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0005_auto_20180116_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scripttag',
            name='script_file',
            field=models.FilePathField(blank=True, null=True, path='C:\\Users\\Admin\\Documents\\Projects\\Python\\Django\\IOTStudio\\staticfiles/js', recursive=True),
        ),
        migrations.AlterField(
            model_name='scripttag',
            name='script_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stylemodel',
            name='style_path',
            field=models.FilePathField(blank=True, null=True, path='C:\\Users\\Admin\\Documents\\Projects\\Python\\Django\\IOTStudio\\staticfiles/css', recursive=True),
        ),
        migrations.AlterField(
            model_name='styletag',
            name='style_file',
            field=models.FilePathField(blank=True, null=True, path='C:\\Users\\Admin\\Documents\\Projects\\Python\\Django\\IOTStudio\\staticfiles/css', recursive=True),
        ),
        migrations.AlterField(
            model_name='styletag',
            name='style_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='templatemodel',
            name='template_path',
            field=models.FilePathField(blank=True, null=True, path='C:\\Users\\Admin\\Documents\\Projects\\Python\\Django\\IOTStudio\\gui/templates', recursive=True),
        ),
    ]
