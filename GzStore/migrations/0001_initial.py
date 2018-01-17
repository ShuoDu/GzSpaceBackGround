# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gz_store',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe9\x93\xba\xe5\x90\x8d\xe7\xa7\xb0')),
                ('gz_no', models.IntegerField(default=0, verbose_name=b'\xe6\xa0\xbc\xe5\xad\x90\xe6\x80\xbb\xe6\x95\xb0')),
                ('use_no', models.IntegerField(default=0, verbose_name=b'\xe6\xa0\xbc\xe5\xad\x90\xe4\xbd\xbf\xe7\x94\xa8\xe6\x95\xb0')),
                ('phone', models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe9\x93\xba\xe7\x94\xb5\xe8\xaf\x9d')),
                ('gz_price', models.IntegerField(default=0, verbose_name=b'\xe6\xa0\xbc\xe5\xad\x90\xe5\xb9\xb3\xe5\x9d\x87\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('address', models.CharField(max_length=200, verbose_name=b'\xe5\x95\x86\xe9\x93\xba\xe5\x9c\xb0\xe5\x9d\x80')),
                ('gz_goods', models.CharField(max_length=300, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x88\x97\xe8\xa1\xa8')),
            ],
            options={
                'verbose_name': '\u5e97\u94fa',
                'verbose_name_plural': '\u5e97\u94fa',
            },
        ),
        migrations.CreateModel(
            name='gz_storeType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe9\x93\xba\xe7\xb1\xbb\xe5\x9e\x8b')),
            ],
            options={
                'verbose_name': '\u5e97\u94fa\u7c7b\u578b',
                'verbose_name_plural': '\u5e97\u94fa\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='stoere_imgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_name', models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe9\x93\xba\xe5\x90\x8d\xe7\xa7\xb0')),
                ('store_img', models.ImageField(upload_to=b'img', verbose_name=b'\xe5\x95\x86\xe9\x93\xba\xe5\x9b\xbe\xe7\x89\x87')),
                ('gzj_img', models.ImageField(upload_to=b'img', verbose_name=b'\xe6\xa0\xbc\xe5\xad\x90\xe6\x9e\xb6\xe5\x9b\xbe\xe7\x89\x87')),
                ('gz_img', models.ImageField(upload_to=b'img', verbose_name=b'\xe6\xa0\xbc\xe5\xad\x90\xe5\x9b\xbe\xe7\x89\x87')),
                ('store', models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe9\x93\xba', to='GzStore.gz_store')),
            ],
            options={
                'verbose_name': '\u5e97\u94fa\u56fe\u7247',
                'verbose_name_plural': '\u5e97\u94fa\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='store_detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_name', models.CharField(max_length=30)),
                ('store_address', models.CharField(max_length=300)),
                ('store_phone', models.CharField(max_length=20)),
                ('gz_no', models.IntegerField(default=0)),
                ('gz_content', models.CharField(max_length=300)),
                ('select_gz_no', models.CharField(max_length=20)),
                ('price', models.IntegerField(default=0)),
                ('order_no', models.CharField(max_length=20)),
                ('use_phone', models.CharField(max_length=20)),
                ('discuss_list', models.CharField(max_length=500)),
                ('store_goods_list', models.CharField(max_length=500)),
                ('store', models.ForeignKey(to='GzStore.gz_store')),
            ],
            options={
                'verbose_name': '\u5e97\u94fa\u8be6\u60c5',
                'verbose_name_plural': '\u5e97\u94fa\u8be6\u60c5',
            },
        ),
        migrations.AddField(
            model_name='gz_store',
            name='store_type',
            field=models.ForeignKey(to='GzStore.gz_storeType'),
        ),
    ]
