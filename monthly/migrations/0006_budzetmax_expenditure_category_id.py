# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-07 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthly', '0005_auto_20161127_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='budzetmax',
            name='expenditure_category_id',
            field=models.IntegerField(default=1),
        ),
    ]