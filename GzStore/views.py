# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.core import serializers
import models
import json
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
    print('请求路径%s' % request.path)
    print('请求方法%s' % request.method)
    print('提交的数据的编码方式%s' % request.encoding)  # 为null就是默认utf8
    all_objs = models.gz_store.objects.all()
    all_dicts = toDicts(all_objs)
    all_json = json.dumps(all_dicts, ensure_ascii=False)
    return HttpResponse(all_json)


# 商铺详情
def space_detail(request):
    #gz_no_list = request.GET.getlist('gz_no')  # 将键的值以列表返回，可以获取一个键的多个值
    gz_no = request.GET.get('gz_no')  # Get一个类似于字典的对象，包含get请求方式的所有参数
    gz_no = request.GET['gz_no']  # 也可以是这种写法
    files = request.FILES.get()  # 一个类似于字典的对象，包含所有的上传文件
    cookies = request.COOKIES  # 一个标准的Python字典，包含所有的cookie，键和值都为字符串

    space_details = models.store_detail.objects.get(gz_no=gz_no)
    dict = space_details.toJson()
    all_json = json.dumps(dict, ensure_ascii=False)
    #  HttpResponseRedirect('js/') 重定向位置
    # JsonResponse({'list': 'abc'}) 子类返回json数据
    # render 简写函数  from django.shortcuts import render
    # render(request, 'booktest/index.html', {'h1': 'hello'})
    # 结合一个给定的模板和一个给定的上下文字典，并返回一个渲染后的HttpResponse对象 request：该request用于生成response
    # from django.shortcuts import redirect  重定向 为传递进来的参数返回HttpResponseRedirect
    # return redirect(reverse('booktest:index2'))

    return HttpResponse(all_json)


def my_image(request):
   image_data=open("picture.png", "rb").read()
   return HttpResponse(image_data, mimetype="image/png")



# 商铺图片
def space_imgs(request):
    all_imgs = models.stoere_imgs.objects.all()
    obj_arr = []
    for i in all_imgs:
        obj_arr.append(i.store_img.url)

    return HttpResponse(obj_arr)





