# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_auto_20170625_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceStaff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u7406\u53d1\u5e08\u540d\u79f0')),
                ('service', models.ForeignKey(verbose_name='\u670d\u52a1', to='apps.Service')),
                ('shop', models.ForeignKey(verbose_name='\u5e97\u9762', blank=True, to='apps.Shop', null=True)),
            ],
        ),
    ]
