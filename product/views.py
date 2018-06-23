# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import traceback

from django.core import serializers
from models import product_center
from django.http import HttpResponse
# Create your views here.

def selectProduct(request):
    request.encoding = 'utf-8'
    dic = {}
    try:
        if request.method == 'GET':
            ptype = request.GET.get('type', '')
        if request.method == 'POST':
            ptype = request.POST.get('type', '')
        if ptype:
            queryData = product_center.objects.filter(type=ptype)
        else:
            queryData = product_center.objects.filter()
        if queryData:
            jsondata = serializers.serialize("json", queryData.order_by('id'))
            return HttpResponse(jsondata)
        else:
            dic['info'] = 'datanotexist'
            dic['resp'] = '0'
        data = json.dumps(dic)
        return HttpResponse(data)
    except:
        print traceback.format_exc()
        dic['info'] = 'exception'
        dic['resp'] = '-1'
        data = json.dumps(dic)
        return HttpResponse(data)