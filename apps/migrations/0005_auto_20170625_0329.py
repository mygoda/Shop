# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_auto_20170625_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.CharField(max_length=255, null=True, verbose_name='\u54c1\u724clogo', blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='logo',
            field=models.CharField(max_length=255, null=True, verbose_name='\u54c1\u724clogo', blank=True),
        ),
    ]
