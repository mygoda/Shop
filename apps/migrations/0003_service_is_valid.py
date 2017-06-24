# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20170624_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548'),
        ),
    ]
