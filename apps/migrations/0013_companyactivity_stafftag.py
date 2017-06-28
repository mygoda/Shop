# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import libs.uuids


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0012_servicestaff_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyActivity',
            fields=[
                ('id', models.CharField(default=libs.uuids.create_uuid, max_length=36, serialize=False, verbose_name='UID', primary_key=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=32, verbose_name='\u6807\u9898')),
                ('desc', models.CharField(max_length=128, null=True, verbose_name='\u7b80\u4ecb', blank=True)),
                ('href', models.CharField(max_length=255, null=True, verbose_name='\u56fe\u6587\u6d88\u606f\u8fde\u63a5', blank=True)),
                ('company', models.ForeignKey(verbose_name='\u516c\u53f8', to='apps.Company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaffTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=32, null=True, verbose_name='\u6807\u7b7e\u540d\u79f0')),
                ('staff', models.ForeignKey(verbose_name='\u670d\u52a1\u4eba\u5458', to='apps.ServiceStaff')),
            ],
        ),
    ]
