# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class gz_user(models.Model):
    class Meta:
        verbose_name = '用户中心'
        verbose_name_plural = '用户中心'
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return "%s" % self.name


class IMG(models.Model):
    class Meta:
        verbose_name = '用户图片'
        verbose_name_plural = '用户图片'
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)
    user = models.ForeignKey('gz_user')
