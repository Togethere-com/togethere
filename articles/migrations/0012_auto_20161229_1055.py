# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-29 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20161227_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='number',
        ),
        migrations.AddField(
            model_name='article',
            name='score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]