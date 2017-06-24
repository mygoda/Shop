# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548'),
        ),
        migrations.AddField(
            model_name='shop',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548'),
        ),
    ]
