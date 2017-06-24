# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_stafftype_show_in_index'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accesstoken',
            options={'verbose_name': '\u767b\u5f55\u4ee4\u724c', 'verbose_name_plural': '\u767b\u5f55\u4ee4\u724c'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237'},
        ),
        migrations.AlterModelOptions(
            name='smscode',
            options={'verbose_name': '\u624b\u673a\u9a8c\u8bc1\u7801', 'verbose_name_plural': '\u624b\u673a\u9a8c\u8bc1\u7801'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': '\u5de5\u4f5c\u4eba\u5458', 'verbose_name_plural': '\u5de5\u4f5c\u4eba\u5458'},
        ),
        migrations.AlterModelOptions(
            name='stafftype',
            options={'verbose_name': '\u5de5\u4f5c\u4eba\u5458\u7c7b\u578b', 'verbose_name_plural': '\u5de5\u4f5c\u4eba\u5458\u7c7b\u578b'},
        ),
    ]
