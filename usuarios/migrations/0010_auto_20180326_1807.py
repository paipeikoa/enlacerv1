# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-26 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_userprofile_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
