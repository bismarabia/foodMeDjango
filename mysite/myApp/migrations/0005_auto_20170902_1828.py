# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 16:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_auto_20170902_1826'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Logs',
            new_name='Log',
        ),
    ]
