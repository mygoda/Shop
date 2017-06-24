# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import libs.datetimes
from django.conf import settings
import libs.uuids
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(unique=True, serialize=False, verbose_name='\u7528\u6237\u8ba4\u8bc1', primary_key=True)),
                ('email', models.EmailField(default='', max_length=255, null=True, verbose_name='\u90ae\u7bb1', blank=True)),
                ('username', models.CharField(default='', max_length=255, null=True, verbose_name='\u7528\u6237\u540d', blank=True)),
                ('avatar', models.CharField(max_length=255, null=True, verbose_name='\u5934\u50cf', blank=True)),
                ('phone', models.CharField(default='', max_length=24, null=True, verbose_name='\u624b\u673a\u53f7', blank=True)),
                ('gender', models.SmallIntegerField(default=1, verbose_name='\u6027\u522b', choices=[(0, '\u7537'), (1, '\u5973')])),
                ('admin', models.BooleanField(default=False, verbose_name='\u7ba1\u7406\u5458')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('is_admin', models.BooleanField(default=False, verbose_name='\u662f\u5426\u7ba1\u7406\u5458')),
                ('is_staff', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5de5\u4f5c\u4eba\u5458')),
                ('wechat', models.CharField(max_length=36, null=True, verbose_name='wechat', blank=True)),
                ('type', models.CharField(default='customer', max_length=16, verbose_name='\u7c7b\u578b', choices=[('customer', '\u7528\u6237'), ('staff', '\u5de5\u4f5c\u4eba\u5458')])),
                ('created_at', models.DateTimeField(default=libs.datetimes.datetime_now, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4', blank=True)),
                ('age', models.IntegerField(default=10, verbose_name='\u5e74\u7eaa')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_token', models.CharField(default=libs.uuids.create_uuid, max_length=36)),
                ('create_timestamp', models.IntegerField(default=0, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('expired_timestamp', models.IntegerField(default=0)),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=36, null=True, verbose_name='\u5fae\u4fe1\u6635\u79f0', blank=True)),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SmsCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(default=libs.uuids.create_sms_code, max_length=8, verbose_name='\u9a8c\u8bc1\u7801')),
                ('type', models.CharField(default='register', max_length=16, verbose_name='\u7c7b\u578b', choices=[('register', '\u6ce8\u518c'), ('delete', '\u5220\u9664')])),
                ('mobile', models.CharField(max_length=24, verbose_name='\u624b\u673a\u53f7\u7801')),
                ('create_timestamp', models.IntegerField(default=0, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('expired_time', models.IntegerField(default=1800, verbose_name='\u8fc7\u671f\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default='open', max_length=16, verbose_name='\u72b6\u6001', choices=[('time', '\u7a7a\u95f2'), ('busy', '\u5fd9\u788c'), ('rest', '\u4f11\u606f')])),
                ('position', models.CharField(max_length=32, null=True, verbose_name='\u804c\u4f4d', blank=True)),
                ('point', models.FloatField(default=0.0, verbose_name='\u8bc4\u5206')),
                ('level', models.CharField(max_length=32, null=True, verbose_name='\u7ea7\u522b', blank=True)),
                ('notes', django_extensions.db.fields.json.JSONField(verbose_name='\u8be6\u7ec6\u4fe1\u606f')),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StaffType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=16, verbose_name='\u7236\u7c7b\u578b')),
                ('sub_type', models.CharField(max_length=24, verbose_name='\u5b50\u7c7b\u578b')),
            ],
        ),
    ]
