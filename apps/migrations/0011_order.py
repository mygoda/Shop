# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import libs.uuids


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20170624_1436'),
        ('apps', '0010_servicestaff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(default=libs.uuids.create_uuid, max_length=36, serialize=False, verbose_name='UID', primary_key=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order_date', models.DateTimeField(null=True, verbose_name='\u9884\u7ea6\u65f6\u95f4', blank=True)),
                ('customer', models.ForeignKey(verbose_name='\u9884\u8ba2\u5ba2\u6237', to='users.Customer')),
                ('service', models.ForeignKey(verbose_name='\u670d\u52a1', to='apps.Service')),
                ('shop', models.ForeignKey(verbose_name='\u5e97\u9762', to='apps.Shop')),
                ('staff', models.ForeignKey(verbose_name='\u670d\u52a1\u4eba\u5458', blank=True, to='apps.ServiceStaff', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
