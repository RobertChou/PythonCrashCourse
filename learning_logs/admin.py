'''
Author: Rober Chou
Date: 2020-10-16 14:30:18
LastEditTime: 2020-10-18 14:25:12
LastEditors: Rober Chou
Description: 
Code make our world better！！
'''
from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic,Entry
admin.site.register(Topic)
admin.site.register(Entry)