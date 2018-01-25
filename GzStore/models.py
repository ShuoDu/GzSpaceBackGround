# -*- coding: utf-8 -*-
from django.db import models


def decode(info):
      return info.decode('utf-8')


# 店铺类型表
class gz_storeType(models.Model):
    class Meta:
        verbose_name = '店铺类型'
        verbose_name_plural = '店铺类型'
    name = models.CharField(max_length=20, verbose_name='商铺类型')  # 商铺类型

    def __str__(self):
        return "%s" % self.name

    def toDict(self):
        return {'name': self.name}


# 店铺列表
class gz_store(models.Model):
    class Meta:
        verbose_name = '店铺'
        verbose_name_plural = '店铺'
    id = models.AutoField(primary_key=True)  # 自增主键
    name = models.CharField(max_length=20, verbose_name='商铺名称')  # 商铺名称
    gz_no = models.IntegerField(default=0, verbose_name='格子总数')
    use_no = models.IntegerField(default=0, verbose_name='格子使用数')
    phone = models.CharField(max_length=20, verbose_name='商铺电话')  # 商铺电话
    gz_price = models.IntegerField(default=0, verbose_name='格子平均价格')
    address = models.CharField(max_length=200, verbose_name='商铺地址')  # 商铺地址
    gz_goods = models.CharField(max_length=300, verbose_name='商品列表')  # 商品列表
    store_img = models.ImageField(upload_to='img', verbose_name='商铺图片') # 商铺图片
    store_type = models.ForeignKey('gz_storeType')
    list_filter = ['name']
    search_fields = ['name']

    def __str__(self):
        return "%s" % self.name

    # 变更成json类型
    def toDict(self):
        print self.store_img.url
        return {'name': self.name, 'gz_no': self.gz_no, 'use_no': self.use_no,
                'phone': self.phone, 'gz_price': self.gz_price, 'address': self.address, 'gz_goods': self.gz_goods, 'store_img':self.store_img.url}


# 店铺详情表
class store_detail(models.Model):
    class Meta:
        verbose_name = '店铺详情'
        verbose_name_plural = '店铺详情'
    store_name = models.CharField(max_length=30, verbose_name='商铺名称')  # 商铺名称
    store_img_one = models.ImageField(upload_to='img', verbose_name='商品图片1')  # 商品图片
    store_img_two = models.ImageField(upload_to='img', verbose_name='商品图片2', blank=True)  # 商品图片
    store_img_three = models.ImageField(upload_to='img', verbose_name='商品图片3', blank=True)  # 商品图片
    store_address = models.CharField(max_length=300, verbose_name='商铺地址')  # 商铺地址
    store_phone = models.CharField(max_length=20, verbose_name='商铺电话')  # 商铺电话
    gz_no = models.IntegerField(default=0, verbose_name='格子架号')  # 格子架号
    gz_content = models.CharField(max_length=300, verbose_name='格子架详细解释', blank=True)  # 格子架详解
    select_gz_no = models.CharField(max_length=20, blank=True, verbose_name='选中的格子号')  # 选中格子号
    price = models.IntegerField(default=0, blank=True, verbose_name='总价格')  # 总价格
    order_no = models.CharField(max_length=20, blank=True, verbose_name='订单号')  # 订单号
    use_phone = models.CharField(max_length=20, blank=True, verbose_name='用户手机号')  # 用户手机号
    discuss_list = models.CharField(max_length=500, blank=True, verbose_name='评论')  # 评论
    store_goods_list = models.CharField(max_length=500, blank=True, verbose_name='店内其他商品')  # 店内其他商品
    store = models.ForeignKey('gz_store')

    def __str__(self):
        return "%s" % self.store_name

    def toJson(self):
        return {'store_name': self.store_name, 'gz_no': self.gz_no, 'gz_content': self.gz_content,
                 'store_phone': self.store_phone,
                'store_address': self.store_address, 'gz_no': self.gz_no, 'select_gz_no': self.select_gz_no,
                'use_phone': self.use_phone, 'discuss_list': self.discuss_list, 'store_goods_list': self.store_goods_list,
                'order_no': self.order_no, 'store_img_one': self.store_img_one.url, 'store_img_two': self.store_img_two.url, 'store_img_three': self.store_img_three.url }







