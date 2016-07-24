# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quadraticsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtopicmodel',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quadraticsApp.TopicModel'),
            preserve_default=False,
        ),
    ]
