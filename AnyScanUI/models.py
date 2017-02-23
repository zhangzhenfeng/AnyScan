# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=32,primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.usernaxme

class PortCrack(models.Model):
    id = models.CharField(max_length=40,primary_key=True)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    # 数据格式[{"ip":"",port:"","username":"","password":""}]
    result = models.CharField(max_length=5000)
    # running success
    status   = models.CharField(max_length=10)
    type     = models.CharField(max_length=10)
    log      = models.CharField(max_length=5000)
    progress = models.CharField(max_length=50)
    success_num = models.CharField(max_length=10,blank=False,default=0)

class PortCrackChild(models.Model):
    id = models.CharField(max_length=40,primary_key=True)
    # 父任务id
    pid = models.ForeignKey(PortCrack)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    # 用户名
    username = models.CharField(max_length=50)
    # 密码
    password = models.CharField(max_length=50)
    # running success fail error
    status   = models.CharField(max_length=10)
    type     = models.CharField(max_length=10)
    log      = models.CharField(max_length=5000)
    progress = models.CharField(max_length=50)