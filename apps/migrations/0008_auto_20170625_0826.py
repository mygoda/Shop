# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_serviceitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceitem',
            name='shop',
        ),
        migrations.AddField(
            model_name='serviceitem',
            name='service',
            field=models.ForeignKey(verbose_name='\u5546\u5e97', blank=True, to='apps.Service', null=True),
        ),
    ]
