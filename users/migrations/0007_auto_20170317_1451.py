# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20170317_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=10, verbose_name='\u5e74\u9f84'),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(default='\u5973', max_length=4, null=True, verbose_name='\u6027\u522b', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=13, null=True, verbose_name='\u7535\u8bdd\u53f7', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='uuid',
            field=models.CharField(max_length=36, null=True, verbose_name='\u5fae\u4fe1\u53f7', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='wechat',
            field=models.CharField(max_length=32, null=True, verbose_name='\u5fae\u4fe1\u53f7', blank=True),
        ),
        migrations.AlterField(
            model_name='accesstoken',
            name='user',
            field=models.ForeignKey(verbose_name='\u5ba2\u6237', to='users.Customer'),
        ),
    ]
