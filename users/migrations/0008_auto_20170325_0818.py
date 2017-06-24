# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import libs.datetimes


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20170317_1451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '\u540e\u53f0\u7ba1\u7406\u7528\u6237', 'verbose_name_plural': '\u540e\u53f0\u7ba1\u7406\u7528\u6237'},
        ),
        migrations.RenameField(
            model_name='accesstoken',
            old_name='user',
            new_name='customer',
        ),
        migrations.AddField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(default=libs.datetimes.datetime_now, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548'),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=16, null=True, verbose_name='\u540d\u5b57', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=32, null=True, verbose_name='\u7528\u6237\u540d', blank=True),
        ),
    ]
