# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170317_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='user',
        ),
        migrations.AddField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=16, null=True, verbose_name='\u540d\u79f0', blank=True),
        ),
    ]
