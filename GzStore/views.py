# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core import serializers
import models
import json
from models import store_detail
from django.shortcuts import render


# 转换成json形式
def toDicts(objs):
    obj_arr = []
    for o in objs:
        obj_arr.append(o.toDict())
    return obj_arr


# 查询所有商铺类型
def type_list(request):
    all_objs = models.gz_storeType.objects.all()
    all_dicts = toDicts(all_objs)
    all_json = json.dumps(all_dicts, ensure_ascii=False)
    return HttpResponse(all_json)


# 查询所有商铺
def list(request):
    all_objs = models.gz_store.objects.all()
    all_dicts = toDicts(all_objs)
    all_json = json.dumps(all_dicts, ensure_ascii=False)
    return HttpResponse(all_json)


# 商铺详情
def space_detail(request):
    gz_no = request.GET.get('gz_no')
    space_details = models.store_detail.objects.get(gz_no=gz_no)
    dict = space_details.toJson()
    all_json = json.dumps(dict, ensure_ascii=False)
    return HttpResponse(all_json)


# 商铺图片
def space_imgs(request):
    all_imgs = models.stoere_imgs.objects.all()
    obj_arr = []
    for i in all_imgs:
        obj_arr.append(i.store_img.url)

    return HttpResponse(obj_arr)





