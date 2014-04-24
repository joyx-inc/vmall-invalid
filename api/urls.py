#!python
#encoding:utf-8

from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('api.views',
                       # Examples:
                       # url(r'^$', 'vmall.views.home', name='home'),
                       # 关于url()的name用法：https://docs.djangoproject.com/en/1.6/topics/http/urls/#naming-url-patterns
                       url(r'^list_store$', views.list_store, name='list_store'),

                       # APP初始化&首页
                      # url(r'^(?P<mcode>(\w+))/init$', views.init),

                       url(r'^(?P<mcode>(\w+))/index$', views.index),

)
