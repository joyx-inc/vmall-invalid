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
import time

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
    json_mall = {};
    try:
        mallList = Mall.objects.filter(mall_code=mcode)
        logger.debug("search mall with code(%s): %s", mcode, mallList)
        if mallList.count() > 0:
            current_mall = mallList[0]
            sign = request.GET.get('sign', '')
            timestamp = request.GET.get('timestamp', '')
            userid = request.GET.get('userid', '')
            v = request.GET.get('v', '')

            isNewUser = 0;
            secretKey = "";
            userlist = User.objects.filter(deviceId=userid)
            if userlist.count() == 0:
                user = User()
                user.deviceId = userid
                user.app_secret = "123456"
                user.gender = 1
                user.name = '网友123456'
                user.mall = current_mall
                user.save()
                #User.objects.create(user)
                isNewUser = 1;
                secretKey = "123456";

            json_mall["mallId"] = current_mall.id
            json_mall["mallName"] = current_mall.name
            json_mall["mallMapId"] = current_mall.mall_map_id
            json_mall["mallLogo"] = current_mall.logo
            json_mall["mallCode"] = current_mall.mall_code
            json_mall["appName"] = current_mall.app_name
            json_mall["date"] = time.time()
            json_mall["isNewUser"] = isNewUser
            json_mall["secretKey"] = secretKey
        else:
            json_mall["error"] = 1
            json_mall["errorCode"] = "1001"
            json_mall["errorMsg"] = "接口不存在"

    except:
        print trace_back()
        pass

    return HttpResponse(json.dumps(json_mall), content_type="application/json")


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


def search(request, mcode):
    jsonObj = {}
    keyword = request.GET.get('keyword', '')
    type = request.GET.get('type', '')
    order = request.GET.get('order', '')
    amount = request.GET.get('amount', '')
    page = request.GET.get('page', '')
    try:
        jsonObj["totalCount"] = 3
        jsonObj['currentPage'] = 1
        '''
        jsonObj['coupons'][0]['store'] = {
            "title": '商户名称',
            "logo": '商户LOGO',
            "id": '商户ID',
            "category": '商户类型'
        }'''
        jsonObj['coupons'][0]['id'] = 1
        jsonObj['coupons'][0]['title'] = "优惠标题"
        jsonObj['coupons'][0]['type'] = 1
        jsonObj['coupons'][0]['tag'] = "HOT"
        jsonObj['coupons'][0]['image'] = "http://img10.360buyimg.com/da/g14/M0A/1F/11/rBEhVVNXWkEIAAAAAAEZiA2IHjIAAMfMQFTwKkAARmg289.jpg"
        jsonObj['coupons'][0]['collectCount'] = 10
        jsonObj['coupons'][0]['commentCount'] = 20
        jsonObj['coupons'][0]['startTime'] = time.time()
        jsonObj['coupons'][0]['endTime'] = time.time()





        logger.debug('jsonstr: %s', jsonObj)
    except:
        print trace_back()
        pass

    return HttpResponse(json.dumps(jsonObj), content_type="application/json")

