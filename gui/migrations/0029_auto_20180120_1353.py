# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-20 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0028_auto_20180120_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentcontrolmodel',
            name='content',
            field=models.ManyToManyField(blank=True, related_name='_contentcontrolmodel_content_+', to='gui.TemplateBlockModel'),
        ),
    ]