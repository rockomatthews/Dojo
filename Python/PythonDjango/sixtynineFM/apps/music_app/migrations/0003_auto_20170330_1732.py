# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0002_fan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=64, unique='true'),
        ),
    ]
