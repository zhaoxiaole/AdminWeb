# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-03 00:02
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image',
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='\u5185\u5bb9    '),
        ),
    ]
