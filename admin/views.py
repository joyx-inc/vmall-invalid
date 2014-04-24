#!python
#encoding:utf-8
from __future__ import division

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.http.response import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, Page
from api.models import *
import json
import logging
from django.contrib.admin.views.decorators import staff_member_required

logger = logging.getLogger("django.%s" % (__name__))

import traceback
import sys


@staff_member_required
def app_index(request):
    jsonstr = '[]'

    response_data = {'data': 1, "q": 2}
    return render_to_response("admin/app/index.html", response_data,
        context_instance=RequestContext(request))


@staff_member_required
def promotion_list(request):
    jsonstr = '[]'

    response_data = {'data': 1, "q": 2}
    return render_to_response("admin/app/promotion.html", response_data,
        context_instance=RequestContext(request))


@staff_member_required
def promotion_list(request):
    jsonstr = '[]'

    response_data = {'data': 1, "q": 2}
    return render_to_response("admin/app/promotion.html", response_data,
        context_instance=RequestContext(request))