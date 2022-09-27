from django.urls import re_path
from . import views


urlpatterns = [
  	re_path(r'crafts', views.craft_list, name='craft_list'),
   re_path(r'^food/$', views.food_list, name='food_list'),
   re_path(r'^craft/(?P<pk>[0-9]+)/$', views.craft_detail, name='craft_detail'),
   re_path(r'^food/(?P<pk>[0-9]+)/$', views.food_detail, name='food_detail'),
   re_path(r'^new/$', views.craft_new, name='craft_new'),
   re_path(r'^post/(?P<pk>[0-9]+)/edit/$', views.craft_edit, name='craft_edit'),
   re_path(r'^drafts/$', views.craft_draft_list, name='craft_draft_list'),
   re_path(r'^post/(?P<pk>[0-9]+)/publish/$', views.craft_publish, name='craft_publish'),
   re_path(r'^post/(?P<pk>[0-9]+)/remove/$', views.craft_remove, name='craft_remove'),
   # re_path(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_craft, name='add_comment_to_craft'),
   re_path(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
   re_path(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove')
]

app_name = 'crafts'