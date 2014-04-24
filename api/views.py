#!python
#encoding:utf-8
from __future__ import division

# Create your views here.
from django.http.response import HttpResponse
from django.http.response import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, Page
from api.models import *
import json
import logging

logger = logging.getLogger("django.%s" % (__name__))

import traceback
import sys


def trace_back():
    try:
        return traceback.print_exc()
    except:
        return ''

'''
APP初始化
return
'''
def init(request, mcode):
    jsonstr = '{}'

    try:
        mall = Mall.objects.get(mall_code=mcode)
        logger.debug("search mall with code(%s): %s", mcode, mall)
        json_mall = {};
        json_mall["name"] = mall.name
        json_mall["logo"] = mall.logo
        json_mall["mall_code"] = mall.mall_code
        json_mall["app_name"] = mall.app_name
        jsonstr = json.dumps(json_mall)
    except:
        print trace_back()
        pass

    return HttpResponse(jsonstr, content_type="application/json")


'''
首页
return
'''
def index(request, mcode):
    jsonstr = '{}'

    try:
        mall = Mall.objects.get(mall_code=mcode)
        logger.debug("search mall with code(%s): %s", mcode, mall)
        json_mall = {};
        json_mall["name"] = mall.name
        json_mall["logo"] = mall.logo
        json_mall["mall_code"] = mall.mall_code
        json_mall["app_name"] = mall.app_name
        jsonstr = json.dumps(json_mall)
    except:
        print trace_back()
        pass

    return HttpResponse(jsonstr, content_type="application/json")


def list_store(request):
    jsonstr = '[]'
    try:
        store_list = Store.objects.all()
        logger.debug("store_list:%s", store_list)
        jsonstr = json.dumps(list(store_list), default=Store.serialize)
        logger.debug('jsonstr: %s', jsonstr)
    except:
        print trace_back()
        pass

    return HttpResponse(jsonstr, content_type="application/json")

