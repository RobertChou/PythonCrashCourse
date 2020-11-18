'''
Author: Rober Chou
Date: 2020-10-16 14:30:18
LastEditTime: 2020-11-16 08:29:32
LastEditors: Rober Chou
Description: 
Code make our world better！！
'''
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    # 用户学习的主题
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        # 返回模型的字符串表示
        return self.text


class Entry(models.Model):
    #学到的某个知识的具体内容
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        #返回模型的字符串表示
        return self.text[:50] + "..."
