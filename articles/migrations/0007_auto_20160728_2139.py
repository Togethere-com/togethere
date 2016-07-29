# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20160726_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('AMS', 'Amsterdam'), ('ROT', 'Rotterdam'), ('THE', 'The Hague'), ('UTR', 'Utrecht')], default='AMS', max_length=3)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='cities',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='articles.City'),
            preserve_default=False,
        ),
    ]