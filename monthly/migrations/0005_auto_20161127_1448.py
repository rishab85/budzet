# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-27 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthly', '0004_auto_20161127_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budzetmax',
            name='expenditure_month',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='budzetmax',
            name='expenduture_date',
            field=models.IntegerField(default=1),
        ),
    ]