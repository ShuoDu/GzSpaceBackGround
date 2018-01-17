# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
import models
import json
from GzStore.views import toDicts


def list(request):
    all_objs = models.gz_find.objects.all()
    all_dicts = toDicts(all_objs)
    all_json = json.dumps(all_dicts, ensure_ascii=False)
    return HttpResponse(all_json)


def good_detail(request):
    price = request.GET.get('price')
    order_details = models.goods_detail.objects.get(price=price)
    # all_json = json.dumps(order_details, ensure_ascii=False)
    return HttpResponse(order_details)


