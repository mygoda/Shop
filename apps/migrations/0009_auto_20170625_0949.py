# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0008_auto_20170625_0826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopindexpic',
            old_name='img',
            new_name='url',
        ),
    ]
