# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-08 10:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0018_auto_20170308_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcodestatus',
            name='last_read',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 8, 18, 49, 12, 607368)),
        ),
    ]