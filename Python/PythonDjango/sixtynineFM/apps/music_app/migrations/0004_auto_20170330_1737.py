# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0003_auto_20170330_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]