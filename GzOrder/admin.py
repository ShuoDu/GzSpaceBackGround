# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import gz_order
from models import gz_order_detail
import xadmin

xadmin.site.register(gz_order)
xadmin.site.register(gz_order_detail)
