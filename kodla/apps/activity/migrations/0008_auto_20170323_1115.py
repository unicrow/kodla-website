# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-23 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0007_activity_has_speaker_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='has_activity_document',
            field=models.BooleanField(default=True, verbose_name='Activity Document'),
        ),
        migrations.AddField(
            model_name='activity',
            name='has_register_url',
            field=models.BooleanField(default=True, verbose_name='Register URL'),
        ),
    ]
