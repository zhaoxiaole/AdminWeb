# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import product_center
 
@admin.register(product_center)
class product_center_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'img', 'insert_time')
    list_per_page = 50
    list_display_links = ('name',)
    fk_fields = ('id', 'name', 'type', 'img', 'insert_time')
    list_filter = ('name', 'type', 'insert_time')
    search_fields = ('id', 'name', 'type', 'img', 'insert_time')