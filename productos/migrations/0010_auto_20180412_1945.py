# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-12 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_auto_20180412_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='precio_compra',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]