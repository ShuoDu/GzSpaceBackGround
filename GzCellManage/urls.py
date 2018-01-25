# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^gz_type_list/$', views.cell_type_list),
    url(r'^cell_manage_list/$', views.cell_manage_list),
    url(r'^gz_manage_list/$', views.gz_manage_list),
]

