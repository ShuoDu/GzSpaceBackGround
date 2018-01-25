from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^list/$', views.list),
    url(r'^type_list/$', views.type_list),
    url(r'^space_detail/$', views.space_detail),

]
