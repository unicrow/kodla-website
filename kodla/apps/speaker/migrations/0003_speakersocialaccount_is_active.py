# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-02 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speaker', '0002_auto_20170301_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='speakersocialaccount',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]