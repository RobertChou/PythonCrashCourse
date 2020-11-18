'''
Author: Rober Chou
Date: 2020-10-26 15:22:39
LastEditTime: 2020-10-26 15:48:05
LastEditors: Rober Chou
Description: 
symbol_custom_string_obkoro1: Code make our world better！！
'''

from .models import Topic

topics = Topic.objects.all()
for topic in topics:
    print(topic.id, topic)