# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
import xadmin
from models import gz_store
from models import store_detail
from models import stoere_imgs
from models import gz_storeType

xadmin.site.register(gz_store)
xadmin.site.register(store_detail)
xadmin.site.register(stoere_imgs)
xadmin.site.register(gz_storeType)



