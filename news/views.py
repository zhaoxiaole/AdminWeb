# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import traceback

from django.core import serializers
from models import company_news
from django.http import HttpResponse
# Create your views here.

def selectNews(request):
    request.encoding = 'utf-8'
    dic = {}
    try:
        queryData = company_news.objects.filter()
        if queryData:
            jsondata = serializers.serialize("json", queryData.order_by('id'))
            print jsondata
            return HttpResponse(jsondata)
        else:
            dic['info'] = 'datanotexist'
            dic['resp'] = '0'
        data = json.dumps(dic)
        print data
        return HttpResponse(data)
    except:
        print traceback.format_exc()
        dic['info'] = 'exception'
        dic['resp'] = '-1'
        data = json.dumps(dic)
        return HttpResponse(data)