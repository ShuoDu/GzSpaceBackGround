# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import xadmin
from django.contrib import admin
from models import gz_user
from models import IMG

xadmin.site.register(gz_user)
xadmin.site.register(IMG)
