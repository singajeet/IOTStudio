# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-15 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0003_auto_20180116_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stylemodel',
            name='style_path',
            field=models.FilePathField(blank=True, null=True, path='C:\\Users\\Admin\\Documents\\Projects\\Python\\Django\\IOTStudio\\staticfiles/css', recursive=True),
        ),
        migrations.AlterField(
            model_name='templatemodel',
            name='template_path',
            field=models.FilePathField(blank=True, null=True, path='C:\\Users\\Admin\\Documents\\Projects\\Python\\Django\\IOTStudio\\gui/templates', recursive=True),
        ),
    ]
