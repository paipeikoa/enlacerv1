# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-26 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_remove_userprofile_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='imagen',
            field=models.ImageField(blank=True, default='static/imagenes/user-default.png', null=True, upload_to='imagenes'),
        ),
    ]