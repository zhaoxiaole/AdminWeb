# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
    
class company_news(models.Model):
    id = models.AutoField('新闻编号',primary_key=True)
    title = models.CharField('新闻标题',max_length=9999)
    abstract = models.CharField('摘要',max_length=9999)
    abstract_image=models.ImageField('摘要图片',upload_to='img')
    content=UEditorField('新闻正文    ',height=300,width=850,default='',blank=True,
                         imagePath="uploads/blog/images",
                         toolbars='besttome',
                         filePath='uploads/blog/files')
    insert_time=models.DateTimeField(u'创建时间', auto_now_add=True)
    change_time=models.DateTimeField(u'修改时间', auto_now=True)
    class Meta:
        verbose_name = '公司新闻'
        verbose_name_plural = '公司新闻'
    
class industry_news(models.Model):
    id = models.AutoField('新闻编号',primary_key=True)
    title = models.CharField('新闻标题',max_length=9999)
    abstract = models.CharField('摘要',max_length=9999)
    abstract_image=models.ImageField('摘要图片',upload_to='img')
    content=UEditorField('新闻正文    ',height=300,width=850,default='',blank=True,
                         imagePath="uploads/blog/images",
                         toolbars='besttome',
                         filePath='uploads/blog/files')
    insert_time=models.DateTimeField(u'创建时间', auto_now_add=True)
    change_time=models.DateTimeField(u'修改时间', auto_now=True)
    class Meta:
        verbose_name = '行业新闻'
        verbose_name_plural = '行业新闻'