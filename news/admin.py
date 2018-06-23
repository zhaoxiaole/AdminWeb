# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import company_news,industry_news
 
@admin.register(company_news)
class company_news_admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'abstract', 'abstract_image', 'content', 'insert_time')
    list_per_page = 50
    list_display_links = ('title',)
    fk_fields = ('id', 'title', 'abstract', 'abstract_image', 'content', 'insert_time')
    list_filter = ('title', 'insert_time')
    search_fields = ('id', 'title', 'abstract', 'abstract_image', 'content', 'insert_time')
    
@admin.register(industry_news)
class industry_news_admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'abstract', 'abstract_image', 'content', 'insert_time')
    list_per_page = 50
    list_display_links = ('title',)
    fk_fields = ('id', 'title', 'abstract', 'abstract_image', 'content', 'insert_time')
    list_filter = ('title', 'insert_time')
    search_fields = ('id', 'title', 'abstract', 'abstract_image', 'content', 'insert_time')