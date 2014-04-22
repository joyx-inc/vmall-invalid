from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('api.views',
                       # Examples:
                       # url(r'^$', 'vmall.views.home', name='home'),
                       url(r'^api/list_store$', views.list_store, name='list_store'),

)
