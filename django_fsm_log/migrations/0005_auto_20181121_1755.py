# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-21 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_fsm_log', '0004_add_source_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statelog',
            name='object_id',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
