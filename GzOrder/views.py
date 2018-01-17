# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core import serializers
import models
import json
from GzStore.views import toDicts


def list(request):
    all_objs = models.gz_order.objects.all()
    all_dicts = toDicts(all_objs)
    all_json = json.dumps(all_dicts, ensure_ascii=False)
    return HttpResponse(all_json)


def order_detail(request):
    order_no = request.GET.get('order_no')
    order_details = models.gz_order_detail.objects.get(order_no=order_no)
    dict = order_details.toDict()
    all_json = json.dumps(dict, ensure_ascii=False)
    return HttpResponse(all_json)


def gz_order(request):
    store_name = request.GET.get('store_name')
    gzj_no = request.GET.get('gzj_no')
    gz_no = request.GET.get('gz_no')
    goods_id = request.GET.get('goods_id')
    user_phone = request.GET.get('phone')

    successContext = {'result': 'success', 'code': 0, 'message': '添加成功!'}
    models.gz_order.objects.create(order_no='222', order_type='1', store_no='333', gzj_img='', gz_no='3', gz_price='20',
                                   gz_goods_no='222,22,33', gz_goods_img='',
                                   store_name='麦当劳', gzj_no='', phone='18801114226', age=18)
    result_json = json.dumps(successContext, ensure_ascii=False)
    return HttpResponse(result_json)