# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-28 01:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_auto_20170228_0120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='uid',
            new_name='user',
        ),
    ]
