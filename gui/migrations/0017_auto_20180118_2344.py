# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-18 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0016_auto_20180118_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationmodel',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Template under active app will be rendered for current app'),
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