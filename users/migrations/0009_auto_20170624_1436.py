# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20170325_0818'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.DeleteModel(
            name='StaffType',
        ),
    ]
