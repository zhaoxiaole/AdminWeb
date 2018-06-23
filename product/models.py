# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
            
class product_center(models.Model):
    id = models.AutoField('产品编号',primary_key=True)
    img = models.ImageField(upload_to='img')
    name = models.CharField('产品名称',max_length=20)
    TYPE_CHOICES=(
        (1,'鲜活产品'),
        (2,'冷冻产品'),
        (3,'加工产品'),
        (4,'精品礼盒'),
        )
    type=models.IntegerField(choices=TYPE_CHOICES)
    insert_time=models.DateTimeField(u'创建时间', auto_now_add=True)
    change_time=models.DateTimeField(u'修改时间', auto_now=True)
    class Meta:
        verbose_name = '产品中心'
        verbose_name_plural = '产品中心'