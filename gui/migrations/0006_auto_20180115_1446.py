# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-15 09:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0005_htmltags_scripttags_styletags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HtmlTags',
            new_name='HtmlTag',
        ),
        migrations.RenameModel(
            old_name='ScriptTags',
            new_name='ScriptTag',
        ),
        migrations.RenameModel(
            old_name='StyleTags',
            new_name='StyleTag',
        ),
    ]
