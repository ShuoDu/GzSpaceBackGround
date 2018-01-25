# -*- coding: utf-8 -*-
from django.db import models


# 商品列表
class gz_find(models.Model):
    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'
    goods_img = models.ImageField(upload_to='img', verbose_name='商品图片')
    goods_name = models.CharField(max_length=20, verbose_name='商品名称')
    user_name = models.CharField(max_length=20, verbose_name='用户名')
    gz_no = models.IntegerField(default=0, verbose_name='格子号')
    use_no = models.IntegerField(default=0, verbose_name='用户号')
    phone = models.CharField(max_length=20, verbose_name='用户手机号')
    goods_price = models.IntegerField(default=0, verbose_name='商品价格')
    goods_content = models.CharField(max_length=300, verbose_name='商品详情')
    goods_little_content = models.CharField(max_length=200, verbose_name='商品小标题')

    def __str__(self):
        return "%s" % self.goods_name

    def toDict(self):
        return {'goods_name': self.goods_name, 'user_name': self.user_name, 'use_no': self.use_no,
                'gz_no': self.gz_no, 'phone': self.phone, 'goods_price': self.goods_price,
                'goods_content': self.goods_content, 'goods_little_content': self.goods_little_content, 'goods_img': self.goods_img.url}


# 商品详情表
class goods_detail (models.Model):
    class Meta:
        verbose_name = '商品详情'
        verbose_name_plural = '商品详情'
    goods_name = models.CharField(max_length=30, verbose_name='商品图片')  # 商品名称
    goods_img_one = models.ImageField(upload_to='img', verbose_name='商品图片1')  # 商品图片
    goods_img_two = models.ImageField(upload_to='img', verbose_name='商品图片2', blank=True)  # 商品图片
    goods_img_three = models.ImageField(upload_to='img', verbose_name='商品图片3', blank=True)  # 商品图片
    store_phone = models.CharField(max_length=20, verbose_name='商铺电话')  # 商铺电话
    store_name = models.CharField(max_length=300, verbose_name='商铺名称')  # 商铺名称
    store_address = models.CharField(max_length=300, verbose_name='商铺地址')  # 商铺地址
    user_img_url = models.ImageField(upload_to='img', verbose_name='用户图片1')  # 用户图片
    user_name = models.CharField(max_length=20, verbose_name='用户名称')  # 用户名称
    use_phone = models.CharField(max_length=20, verbose_name='用户手机号')  # 用户手机号
    user_goods_list = models.CharField(max_length=500, verbose_name='用户其他商品')  # 用户其他商品
    price = models.IntegerField(default=0, verbose_name='总价格')  # 总价格
    order_no = models.CharField(max_length=20, blank=True, verbose_name='订单号')  # 订单号
    order_type = models.IntegerField(default=0, blank=True, verbose_name='订单类型')  # 订单类型 可为空
    discuss_list = models.CharField(max_length=500, blank=True, verbose_name='评论列表')  # 评论
    goods_content = models.CharField(max_length=300, verbose_name='商品详情')
    goods_little_content = models.CharField(max_length=200, verbose_name='商品小标题')
    gfind = models.ForeignKey('gz_find')

    def __str__(self):
        return "%s" % self.goods_name

    def toDict(self):
        return {'goods_name': self.goods_name, 'user_name': self.user_name,
                'price': self.goods_price,
                'goods_content': self.goods_content, 'goods_little_content': self.goods_little_content,  'goods_img_one': self.goods_img_one.url, 'store_goods_two': self.goods_img_two.url, 'goods_img_three': self.goods_img_three.url}

