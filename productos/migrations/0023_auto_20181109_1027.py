# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-09 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0022_auto_20181109_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
