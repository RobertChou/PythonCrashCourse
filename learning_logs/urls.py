'''
Author: Rober Chou
Date: 2020-10-22 17:32:21
LastEditTime: 2020-11-06 16:58:40
LastEditors: Rober Chou
Description: 
symbol_custom_string_obkoro1: Code make our world better！！
'''
#定义learning_logs的url模式
from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    re_path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
    re_path('new_topic/$', views.new_topic, name='new_topic'),
    re_path('new_entry/(?P<topic_id>\d+)/$', views.new_entry,
            name='new_entry'),
    re_path('edit_entry/(?P<entry_id>\d+)/$',
            views.edit_entry,
            name="edit_entry"),
]
