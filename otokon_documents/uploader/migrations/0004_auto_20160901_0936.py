# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 09:36
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0003_auto_20160805_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
