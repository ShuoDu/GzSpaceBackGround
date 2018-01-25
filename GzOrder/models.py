# -*- coding: utf-8 -*-
from django.db import models


def decode(info):
      return info.decode('utf-8')


class gz_order(models.Model):
    class Meta:
        verbose_name = '订单列表'
        verbose_name_plural = '订单列表'

    order_no = models.CharField(max_length=20)  # 订单号
    order_type = models.IntegerField(default=0)  # 订单类型
    order_statue = models.CharField(max_length=100)  # 订单状态
    store_no = models.CharField(max_length=20)  # 商户号
    store_name = models.CharField(max_length=20, blank=True)  # 商铺名称
    gzj_no = models.IntegerField(default=0)  # 格子架号
    gzj_img = models.CharField(max_length=200, blank=True)  # 格子架图片集合
    gz_no = models.CharField(max_length=100)  # 格子号集合
    gz_price = models.IntegerField(default=0, blank=True)  # 格子租用总价格
    gz_goods_no = models.CharField(max_length=300, blank=True)  # 格子商品号列表
    gz_goods_img = models.CharField(max_length=300, blank=True)  # 格子商品列表

    def __str__(self):
        return "%s" % self.order_no

    def toDict(self):
        return {'order_no': self.order_no, 'order_type': self.order_type, 'order_statue': self.order_statue,
                'store_no': self.store_no,'store_name': self.store_name, 'gzj_no': self.gzj_no, 'gzj_img': self.gzj_img,
                'gz_no': self.gz_no, 'gz_price': self.gz_price,
                 'gz_goods_no': self.gz_goods_no, 'gz_goods_img': self.gz_goods_img
                }


class gz_order_detail(models.Model):
    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = '订单详情'
    order_no = models.CharField(max_length=20)  # 订单号
    order_type = models.IntegerField(default=0)  # 订单类型 1商品订单，2格子订单
    order_statue = models.CharField(max_length=100)  # 订单状态 1 已下单 2 待发货 3 待收货 4 待评价

    store_no = models.CharField(max_length=20)  # 商户号
    store_name = models.CharField(max_length=20, blank=True)  # 商铺名称
    store_phone = models.CharField(max_length=20, blank=True)  # 商铺电话
    store_img_url = models.CharField(max_length=100, blank=True)  # 商户图片集合
    store_address = models.CharField(max_length=200, blank=True)  # 商铺地址

    gzj_no = models.IntegerField(default=0)  # 格子架号
    gzj_img = models.CharField(max_length=200, blank=True)  # 格子架图片集合
    gzj_price = models.IntegerField(default=0, blank=True)  # 格子架租用总价格

    gz_no = models.CharField(max_length=100)  # 格子号集合
    gz_price = models.IntegerField(default=0, blank=True)  # 格子租用总价格
    gz_content = models.CharField(max_length=200, blank=True)  # 格子说明

    use_no = models.IntegerField(default=0)  # 格子用户id
    use_phone = models.CharField(max_length=20)  # 格子用户电话

    gz_goods_no = models.CharField(max_length=300, blank=True)  # 格子商品号列表
    gz_goods_img = models.CharField(max_length=300, blank=True)  # 格子商品列表
    gz_goods_content = models.CharField(max_length=300, blank=True)  # 格子商品详情
    gz_goods_price = models.CharField(max_length=300, blank=True)  # 格子商品价格
    order = models.ForeignKey('gz_order')

    def __str__(self):
        return "%s" % self.order_no

    def toDict(self):
        return {'order_no': self.order_no, 'order_type': self.order_type, 'order_statue': self.order_statue,
                'store_name': self.store_name, 'store_phone': self.store_phone, 'store_img_url': self.store_img_url,
                'store_address': self.store_address, 'gzj_no': self.gzj_no, 'gzj_img': self.gzj_img,
                'gzj_price': self.gzj_price, 'gz_no': self.gzj_no, 'gz_price': self.gzj_price,
                'gz_content': self.gz_content, 'use_no': self.use_no, 'use_phone': self.use_phone,
                'gz_goods_no': self.gz_goods_no, 'gz_goods_img': self.gz_goods_img,
                'gz_goods_content': self.gz_goods_content,
                'gz_goods_price': self.gz_goods_price}


# 评价表