# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0014_servicestaff_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyactivity',
            name='img',
            field=models.CharField(max_length=255, null=True, verbose_name='\u6807\u9898\u56fe\u7247', blank=True),
        ),
    ]
