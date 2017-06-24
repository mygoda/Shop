# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_stafftype_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='stafftype',
            name='show_in_index',
            field=models.BooleanField(default=False, verbose_name='\u9996\u9875\u5c55\u793a'),
        ),
    ]
