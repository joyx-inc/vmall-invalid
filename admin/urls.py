#!python
#encoding:utf-8

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vmall.views.home', name='home'),

    url(r'^index$', 'admin.views.app_index', name='admin_app_index'),
)
