# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 08:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20160724_1550'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='category',
            new_name='categories',
        ),
    ]
