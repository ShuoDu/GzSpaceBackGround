# -*- coding: utf-8 -*-
from django.contrib import admin
import xadmin
# Register your models here.
from models import gz_cell
from models import gz_cell_manange
from models import gz_manange
xadmin.site.register(gz_cell)
xadmin.site.register(gz_cell_manange)
xadmin.site.register(gz_manange)

