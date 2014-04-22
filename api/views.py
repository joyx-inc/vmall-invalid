#!python
#encoding:utf-8

# Create your views here.
from django.http.response import HttpResponse
from api.models import *
import top.api
import top
import json


def list_store(request):
    jsonstr = '[]'

    try:
        store_list = list(Store.objects.order_by('order'))
        jsonstr = json.dumps(store_list)
    except:
        pass

    return HttpResponse(jsonstr, content_type="application/json")