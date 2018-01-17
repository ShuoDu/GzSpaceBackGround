# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GzUser', '0002_auto_20171213_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMG',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to='img')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='gz_user',
            options={'verbose_name': '\u7528\u6237\u4e2d\u5fc3', 'verbose_name_plural': '\u7528\u6237\u4e2d\u5fc3'},
        ),
        migrations.AddField(
            model_name='img',
            name='user',
            field=models.ForeignKey(to='GzUser.gz_user'),
        ),
    ]
