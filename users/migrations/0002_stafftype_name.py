# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stafftype',
            name='name',
            field=models.CharField(default='name', max_length=24, verbose_name='\u663e\u793a\u540d\u79f0'),
        ),
    ]
