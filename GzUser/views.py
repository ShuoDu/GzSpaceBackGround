# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import models
import json


def login(request):
    phones = request.GET.get('phone')
    msg = request.GET.get('msg')
    user_details = ""
    print phones
    print msg
    successContext = {'result': 'success', 'code': 0, 'message': '登录成功!','phone':phones }
    faildContext = {'result': 'faild', 'code': 1, 'message': '请输入正确验证码!'}
    # http://127.0.0.1:8080/login/?phone=18801114226&msg=8888
    try:
        user_details = models.gz_user.objects.get(phone=phones)
    except models.gz_user.DoesNotExist:
        user_details = None
    if (user_details == None) :
        models.gz_user.objects.create(name=phones, phone=phones, age=18)
        result_json = json.dumps(successContext, ensure_ascii=False)
        return HttpResponse(result_json)
    else:
        result_json = json.dumps(successContext, ensure_ascii=False)
        return HttpResponse(result_json)


def uploadImg(request):
    if request.method == 'POST':
        new_img = models.IMG(
            img=request.FILES.get('img'),
            # name=request.FILES.get('img').name
            name="杜硕",
            user_id=1
        )
        new_img.save()
    return render(request, 'uploading.html')


def showImg(request):
    imgs = models.IMG.objects.all()
    content = {
        'imgs':imgs,
    }
    for i in imgs:
        print i.img.url
    return render(request, 'showImg.html', content)


