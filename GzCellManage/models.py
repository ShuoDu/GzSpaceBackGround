# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# 格子架表
class gz_cell(models.Model):
    class Meta:
        verbose_name = '格子架'
        verbose_name_plural = '格子架'

    name = models.CharField(max_length=20, verbose_name='格子架名称')  #  格子名称
    width = models.IntegerField(default=0, verbose_name='宽度')  # 格子架宽度
    height = models.IntegerField(default=0, verbose_name="高度")  # 格子架高度
    cell_num = models.IntegerField(default=0, verbose_name="格子数")  # 格子数
    cell_img = models.ImageField(upload_to='img', verbose_name='格子图片')  # 格子图片

    def __str__(self):
        return "%s" % self.name

    def toDict(self):
        return {'name': self.name, 'width': self.width, 'height': self.height, 'cell_num': self.cell_num, 'cell_img': self.cell_img.url}


# 格子架使用表
class gz_cell_manange(models.Model):
    class Meta:
        verbose_name = '格子架使用'
        verbose_name_plural = '格子架使用'

    cell_name = models.CharField(max_length=20, verbose_name='格子架名称')  # 格子架名称
    cell_no = models.CharField(max_length=20, verbose_name='格子架编号')  # 格子架编号
    store_name = models.CharField(max_length=20, verbose_name="店铺名称")  # 店铺名称
    store_address = models.CharField(max_length=200, verbose_name="店铺地址")  # 店铺地址
    store_phone = models.CharField(max_length=20, verbose_name="店铺电话")  # 店铺电话
    use_cell_width = models.IntegerField(default=0,verbose_name="使用格子宽度")  #使用格子宽度
    use_cell_height = models.IntegerField(default=0, verbose_name="使用格子高度")  # 使用格子高度
    use_cell_num = models.IntegerField(default=0, verbose_name="使用格子个数")  # 使用格子个数

    def __str__(self):
        return "%s" % self.cell_name

    # 变更成json类型
    def toDict(self):
        return {'cell_name': self.cell_name, 'cell_no': self.cell_no, 'store_name': self.store_name,
                'store_address': self.store_address, 'store_phone': self.store_phone, 'use_cell_width': self.use_cell_width, 'use_cell_height': self.use_cell_height,
                'use_cell_num': self.use_cell_num}


# 格子使用表
class gz_manange(models.Model):
    class Meta:
        verbose_name = '格子使用'
        verbose_name_plural = '格子使用'

    cell_name = models.CharField(max_length=20, verbose_name='格子架名称', blank=True)  # 格子架名称
    cell_no = models.CharField(max_length=20, verbose_name='格子架编号', blank=True)  # 格子架编号
    store_name = models.CharField(max_length=20, verbose_name="店铺名称", blank=True)  # 店铺名称
    store_address = models.CharField(max_length=200, verbose_name="店铺地址", blank=True)  # 店铺地址
    store_phone = models.CharField(max_length=20, verbose_name="店铺电话")  # 店铺电话
    user_name = models.CharField(max_length=20, verbose_name="用户名称", blank=True)  # 用户名称
    user_phone = models.CharField(max_length=20, verbose_name="用户电话", blank=True)  # 用户电话
    use_cell_num = models.IntegerField(default=0, verbose_name="使用格子个数", blank=True)  # 使用格子个数
    use_cellNo_list = models.CharField(max_length=200, verbose_name="使用格子个数", blank=True)  # 使用格子编号集合
    pay_money = models.IntegerField(default=0, verbose_name="总金额", blank=True)  # 使用格子个数
    start_time = models.CharField(max_length=100, verbose_name="开始时间", blank=True)  # 开始时间
    end_time = models.CharField(max_length=100, verbose_name="结束时间", blank=True)  # 结束时间

    def __str__(self):
        return "%s" % self.cell_name

    # 变更成json类型
    def toDict(self):
        return {'cell_name': self.cell_name, 'cell_no': self.cell_no, 'store_name': self.store_name,
                'store_address': self.store_address, 'user_name': self.user_name, 'store_phone':self.store_phone,
                'use_cell_width': self.use_cell_width, 'use_cell_height': self.use_cell_height, 'pay_money': self.pay_money,
                'use_cell_num': self.use_cell_num, 'start_tim': self.start_time, 'end_tim': self.end_time, 'user_phone':self.user_phone}
