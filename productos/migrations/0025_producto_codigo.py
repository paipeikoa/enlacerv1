# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-23 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0024_auto_20181112_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
