# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import models
import json


# 转换成json形式
def toDicts(objs):
    obj_arr = []
    for o in objs:
        obj_arr.append(o.toDict())
    return obj_arr


# 格子架类型列表
def cell_type_list(request):
    all_objs = models.gz_cell.objects.all()
    all_dict = toDicts(all_objs)
    all_json = json.dumps(all_dict, ensure_ascii=False)
    return HttpResponse(all_json)


# 格子架使用详情列表
def cell_manage_list(request):
    all_objs = models.gz_cell_manange.objects.all()
    all_dict = toDicts(all_objs)
    all_json = json.dumps(all_dict, ensure_ascii=False)
    return HttpResponse(all_json)


# 格子使用详情列表
def gz_manage_list(request):
    all_objs = models.gz_manange.objects.all()
    all_dict = toDicts(all_objs)
    all_json = json.dumps(all_dict, ensure_ascii=False)
    return HttpResponse(all_json)

