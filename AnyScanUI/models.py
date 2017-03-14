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
    # running success pause
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
    # running success fail error pause
    status   = models.CharField(max_length=10)
    type     = models.CharField(max_length=10)
    log      = models.CharField(max_length=5000)
    progress = models.CharField(max_length=50)
    threads = models.CharField(max_length=10,blank=False,default="1")
    ip = models.CharField(max_length=50,blank=False,default="")
    port = models.CharField(max_length=50,blank=False,default="")
    # 存储到数据库的未进行爆破的字典，为暂停功能服务
    attack_queue_list = models.TextField(blank=False,default="")
    # 初始字典的总长度
    old_queue_size = models.CharField(max_length=20,blank=False,default="")
    # 模拟数据锁
    locker = models.CharField(max_length=5,blank=False,default="false")

class CmsInfo(models.Model):
    id = models.CharField(max_length=40,primary_key=True)
    host = models.CharField(max_length=40)
    url_list = models.TextField(blank=False,default="")
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    log      = models.CharField(max_length=5000)
    progress = models.CharField(max_length=50)
    threads = models.CharField(max_length=10,blank=False,default="1")
    # running success fail error pause
    status   = models.CharField(max_length=10)
    # 模拟数据锁
    locker = models.CharField(max_length=5,blank=False,default="false")
    cms = models.CharField(max_length=50,blank=False,default="")
    version = models.CharField(max_length=50,blank=False,default="")
    payload = models.CharField(max_length=300,blank=False,default="")
    keyword = models.CharField(max_length=50,blank=False,default="")

# POC执行主任务
class poc_main(models.Model):
    id = models.CharField(max_length=40,primary_key=True)
    commond = models.CharField(max_length=200)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    log      = models.CharField(max_length=5000)
    progress = models.CharField(max_length=50)
    threads = models.CharField(max_length=10,blank=False,default="1")
    # running success fail error pause
    status   = models.CharField(max_length=10)
    # 模拟数据锁
    locker = models.CharField(max_length=5,blank=False,default="false")

# POC执行子任务
class poc_chil(models.Model):
    id = models.CharField(max_length=40,primary_key=True)
    pid = models.ForeignKey(poc_main)
    commond = models.CharField(max_length=200)
    # True False
    vulnerable   = models.CharField(max_length=10)
    host = models.CharField(max_length=500)
    # poc执行结果
    keyword = models.CharField(max_length=500)


# POC执行主任务
class poc_urls(models.Model):
    id = models.CharField(max_length=40,primary_key=True)
    commond = models.CharField(max_length=200)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    log      = models.CharField(max_length=5000)
    urls = models.TextField(blank=False,default="")
    counts = models.CharField(max_length=50)
    threads = models.CharField(max_length=10,blank=False,default="1")
    # running success fail error pause
    status   = models.CharField(max_length=10)
    # 模拟数据锁
    locker = models.CharField(max_length=5,blank=False,default="false")
