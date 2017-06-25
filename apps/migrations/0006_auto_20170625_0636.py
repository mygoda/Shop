# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_auto_20170625_0329'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, null=True, verbose_name='\u670d\u52a1\u540d\u79f0', blank=True)),
                ('url', models.CharField(max_length=255, null=True, verbose_name='\u56fe\u7247\u5730\u5740', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='desc',
            field=models.CharField(max_length=255, null=True, verbose_name='\u63cf\u8ff0', blank=True),
        ),
        migrations.AddField(
            model_name='serviceimage',
            name='service',
            field=models.ForeignKey(verbose_name='\u670d\u52a1', blank=True, to='apps.Service', null=True),
        ),
    ]
