# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-26 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0029_auto_20181126_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]