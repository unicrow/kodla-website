# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-08 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_auto_20170306_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
    ]
