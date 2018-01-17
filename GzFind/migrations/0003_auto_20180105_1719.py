# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GzFind', '0002_goods_detail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods_detail',
            options={'verbose_name': '\u5546\u54c1\u8be6\u60c5', 'verbose_name_plural': '\u5546\u54c1\u8be6\u60c5'},
        ),
        migrations.AlterModelOptions(
            name='gz_find',
            options={'verbose_name': '\u5546\u54c1', 'verbose_name_plural': '\u5546\u54c1'},
        ),
    ]
