# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-05 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0002_auto_20181005_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsessionresult',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='session',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='questionsessionresult',
            unique_together=set([('session', 'question')]),
        ),
    ]
