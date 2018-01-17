# -*- coding: utf-8 -*-
from django.db import models


class gz_find(models.Model):
    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'
    goods_name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    gz_no = models.IntegerField(default=0)
    use_no = models.IntegerField(default=0)
    phone = models.CharField(max_length=20)
    goods_price = models.IntegerField(default=0)
    goods_content = models.CharField(max_length=300)
    goods_little_content = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % self.goods_name

    def toDict(self):
        return {'goods_name': self.goods_name, 'user_name': self.user_name, 'use_no': self.use_no,
                'gz_no': self.gz_no, 'phone': self.phone, 'goods_price': self.goods_price,
                'goods_content': self.goods_content, 'goods_little_content': self.goods_little_content}


class goods_detail (models.Model):
    class Meta:
        verbose_name = '商品详情'
        verbose_name_plural = '商品详情'
    goods_name = models.CharField(max_length=30)  # 商品名称
    goods_img = models.CharField(max_length=200)  # 商品图片
    store_phone = models.CharField(max_length=20)  # 商铺电话
    store_name = models.CharField(max_length=300)  # 商铺名称
    user_img_url = models.CharField(max_length=500)  # 用户图片
    user_name = models.CharField(max_length=20)  # 用户名称
    use_phone = models.CharField(max_length=20)  # 用户手机号
    user_goods_list = models.CharField(max_length=500)  # 用户其他商品
    price = models.IntegerField(default=0)  # 总价格
    order_no = models.CharField(max_length=20)  # 订单号
    order_type = models.IntegerField(default=0)  # 订单类型
    discuss_list = models.CharField(max_length=500)  # 评论
    gfind = models.ForeignKey('gz_find')

    def __str__(self):
        return "%s" % self.goods_name
