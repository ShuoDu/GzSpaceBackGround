# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GzFind', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='goods_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=30)),
                ('goods_img', models.CharField(max_length=200)),
                ('store_phone', models.CharField(max_length=20)),
                ('store_name', models.CharField(max_length=300)),
                ('user_img_url', models.CharField(max_length=500)),
                ('user_name', models.CharField(max_length=20)),
                ('use_phone', models.CharField(max_length=20)),
                ('user_goods_list', models.CharField(max_length=500)),
                ('price', models.IntegerField(default=0)),
                ('order_no', models.CharField(max_length=20)),
                ('order_type', models.IntegerField(default=0)),
                ('discuss_list', models.CharField(max_length=500)),
                ('gfind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GzFind.gz_find')),
            ],
        ),
    ]