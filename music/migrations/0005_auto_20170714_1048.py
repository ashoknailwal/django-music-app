# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20170714_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]