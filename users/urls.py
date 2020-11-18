'''
Author: Rober Chou
Date: 2020-11-06 15:50:25
LastEditTime: 2020-11-11 15:52:56
LastEditors: Rober Chou
Description: 
symbol_custom_string_obkoro1: Code make our world better！！
'''
#定义users的url模式
from django.urls import path
from django.urls import re_path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    #登录页面
    re_path('login/$',
            LoginView.as_view(template_name='users/login.html'),
            name='login'),
    re_path('logout/$', views.logout_view, name='logout'),
    re_path('register/$', views.register, name='register'),
]
