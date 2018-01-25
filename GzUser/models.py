# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class gz_user(models.Model):
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
    name = models.CharField(max_length=20, blank=True, verbose_name='用户名')
    img = models.ImageField(upload_to='img', blank=True, verbose_name='用户头像')
    age = models.IntegerField(default=0, blank=True, verbose_name='年龄')
    phone = models.CharField(max_length=20,  verbose_name='电话')
    sex = models.CharField(max_length=20, blank=True, verbose_name='性别')

    def __str__(self):
        return "%s" % self.name

    def toJson(self):
        return {'user_name': self.name, 'user_img': self.img.url, 'user_age': self.age,
                 'user_phone': self.phone, 'user_sex': self.sex}



