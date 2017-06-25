# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_auto_20170625_0636'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('desc', models.CharField(max_length=64, verbose_name='\u9879\u76ee\u63cf\u8ff0')),
                ('shop', models.ForeignKey(verbose_name='\u5546\u5e97', blank=True, to='apps.Shop', null=True)),
            ],
        ),
    ]
