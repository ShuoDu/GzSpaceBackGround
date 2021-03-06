# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-24 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gz_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4e2d\u5fc3',
                'verbose_name_plural': '\u7528\u6237\u4e2d\u5fc3',
            },
        ),
        migrations.CreateModel(
            name='IMG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
                ('name', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GzUser.gz_user')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u56fe\u7247',
                'verbose_name_plural': '\u7528\u6237\u56fe\u7247',
            },
        ),
    ]
