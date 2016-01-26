from django.conf.urls import include, url
from . import views

urlpatterns = [
  	url(r'^$', views.craft_list, name='craft_list'),
   	url(r'^craft/(?P<pk>[0-9]+)/$', views.craft_detail, name='craft_detail'),
   	url(r'^craft/new/$', views.craft_new, name='craft_new'),
   	url(r'^craft/(?P<pk>[0-9]+)/edit/$', views.craft_edit, name='craft_edit'),
   	url(r'^drafts/$', views.craft_draft_list, name='craft_draft_list'),
   	url(r'^craft/(?P<pk>[0-9]+)/publish/$', views.craft_publish, name='craft_publish'),
   	url(r'^craft/(?P<pk>[0-9]+)/remove/$', views.craft_remove, name='craft_remove'),

]	