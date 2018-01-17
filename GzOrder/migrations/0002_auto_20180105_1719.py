# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GzOrder', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gz_order',
            options={'verbose_name': '\u8ba2\u5355\u5217\u8868', 'verbose_name_plural': '\u8ba2\u5355\u5217\u8868'},
        ),
        migrations.AlterModelOptions(
            name='gz_order_detail',
            options={'verbose_name': '\u8ba2\u5355\u8be6\u60c5', 'verbose_name_plural': '\u8ba2\u5355\u8be6\u60c5'},
        ),
    ]
