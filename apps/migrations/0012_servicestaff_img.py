# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0011_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicestaff',
            name='img',
            field=models.CharField(max_length=255, null=True, verbose_name='\u5934\u50cf', blank=True),
        ),
    ]
