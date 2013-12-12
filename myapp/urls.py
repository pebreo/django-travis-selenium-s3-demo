from django.conf.urls import patterns, url
#from .views import ThingList, ThingCreate, ThingDetail, ThingUpdate, ThingDelete
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^formview1', views.formview1, name='formview1'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.user_login, name='login'),
    #url(r'^$', ThingList.as_view(), name='thing_list'),
    #url(r'^new/$', ThingCreate.as_view(), name='thing_create'),
    #url(r'^(?P<pk>\d+)/$', ThingDetail.as_view(), name='thing_detail'),
    #url(r'^(?P<pk>\d+)/update/$', ThingUpdate.as_view(), name='thing_update'),
    #url(r'^(?P<pk>\d+)/delete/$', ThingDelete.as_view(), name='thing_delete'),
)