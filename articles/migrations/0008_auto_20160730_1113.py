# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-30 09:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20160728_2139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='cities',
            new_name='city',
        ),
    ]
