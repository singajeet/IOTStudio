# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-16 13:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0007_pageicontag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PageIconTag',
            new_name='IconTag',
        ),
    ]