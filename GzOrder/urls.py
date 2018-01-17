from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^list/$', views.list),
    url(r'^detail/$', views.order_detail),
    url(r'^createGzOrder/$', views.gz_order),
]