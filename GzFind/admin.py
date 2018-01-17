# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import unicode_literals
from django.contrib import admin
from models import gz_find
from models import goods_detail
import xadmin
# Register your models here.
xadmin.site.register(gz_find)
xadmin.site.register(goods_detail)

