# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-12 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20180412_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precios',
            name='precio_unitario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]