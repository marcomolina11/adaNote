# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 18:55
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('notes_ajax', '0003_auto_20160903_0051'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='note',
            managers=[
                ('noteManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
