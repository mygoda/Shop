# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0013_companyactivity_stafftag'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicestaff',
            name='position',
            field=models.CharField(max_length=32, null=True, verbose_name='\u804c\u79f0', blank=True),
        ),
    ]
