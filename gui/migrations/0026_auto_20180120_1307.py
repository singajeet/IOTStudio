# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-20 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0025_auto_20180120_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='htmltagmodel',
            name='css_classes',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='htmltagmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='htmltagmodel',
            name='tag_type',
            field=models.CharField(choices=[('-1', 'None'), ('00', 'Div'), ('00', 'Span')], default='-1', max_length=2),
        ),
        migrations.AddField(
            model_name='styletagmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='controlstylemodel',
            name='style_path',
            field=models.FilePathField(blank=True, null=True, path='C:\\Users\\Admin\\Documents\\Projects\\Python\\Django\\IOTStudio\\staticfiles/css', recursive=True),
        ),
        migrations.AlterField(
            model_name='icontagmodel',
            name='icon_file',
            field=models.FilePathField(blank=True, null=True, path='C:\\Users\\Admin\\Documents\\Projects\\Python\\Django\\IOTStudio\\staticfiles/img', recursive=True),
        ),
        migrations.AlterField(
            model_name='scripttagmodel',
            name='script_file',
            field=models.FilePathField(blank=True, null=True, path='C:\\Users\\Admin\\Documents\\Projects\\Python\\Django\\IOTStudio\\staticfiles/js', recursive=True),
        ),
        migrations.AlterField(
            model_name='styletagmodel',
            name='style_file',
            field=models.FilePathField(blank=True, null=True, path='C:\\Users\\Admin\\Documents\\Projects\\Python\\Django\\IOTStudio\\staticfiles/css', recursive=True),
        ),
        migrations.AlterField(
            model_name='templatemodel',
            name='template_path',
            field=models.FilePathField(blank=True, null=True, path='C:\\Users\\Admin\\Documents\\Projects\\Python\\Django\\IOTStudio\\gui/templates', recursive=True),
        ),
    ]