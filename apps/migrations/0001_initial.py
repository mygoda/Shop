# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import libs.uuids


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.CharField(default=libs.uuids.create_uuid, max_length=36, serialize=False, verbose_name='UID', primary_key=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u516c\u53f8\u540d\u79f0')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.CharField(default=libs.uuids.create_uuid, max_length=36, serialize=False, verbose_name='UID', primary_key=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u670d\u52a1\u540d\u79f0')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.CharField(default=libs.uuids.create_uuid, max_length=36, serialize=False, verbose_name='UID', primary_key=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u5e97\u9762\u540d\u79f0')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='\u5730\u5740', blank=True)),
                ('company', models.ForeignKey(verbose_name='\u516c\u53f8', blank=True, to='apps.Company', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShopIndexPic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('href', models.CharField(max_length=255, null=True, verbose_name='\u94fe\u63a5', blank=True)),
                ('img', models.CharField(max_length=255, null=True, verbose_name='\u56fe\u7247\u94fe\u63a5', blank=True)),
                ('pri', models.IntegerField(default=0, help_text='\u4ece\u5c0f\u5230\u5927\u6392\u5217', verbose_name='\u4f18\u5148\u7ea7')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='shop',
            field=models.ForeignKey(verbose_name='\u5e97\u9762', blank=True, to='apps.Shop', null=True),
        ),
    ]
