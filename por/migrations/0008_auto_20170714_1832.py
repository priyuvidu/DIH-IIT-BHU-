# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 13:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('por', '0007_auto_20170714_1829'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
    ]