# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_service_is_valid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopindexpic',
            options={'ordering': ('pri',)},
        ),
        migrations.AddField(
            model_name='shopindexpic',
            name='shop',
            field=models.ForeignKey(verbose_name='\u5546\u5e97', blank=True, to='apps.Shop', null=True),
        ),
    ]
