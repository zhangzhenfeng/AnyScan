#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from AnyScanUI.util.Http import Http


def get_taskid(http):
    """
    获取sqlmapapi的taskid
    Returns:
    taskid
    """
    taskStr = http.get('/task/new',params='')
    taskObj = json.loads(taskStr)
    return taskObj

def send2task(http,data,taskid):
    """
    dbgMsg += "\n\t$ curl -H \"Content-Type: application/json\" -X POST -d '{\"url\": \"http://testphp.vulnweb.com/artists.php?artist=1\"}'
    http://%s:%d/scan/$taskid/start" % (host, port)
    Returns:

    """
    taskStr = http.post('/scan/%s/start' % taskid,data=data)
    print taskStr

def get_taskData(http,taskid):
    """
    curl http://%s:%d/scan/$taskid/data" % (host, port)
    Args:
        host:
        port:
        taskid:

    Returns:
    获取任务日志log
    """
    taskStr = http.get('/scan/%s/data' % (taskid))
    print taskStr

def get_taskLog(http,taskid):
    """
    curl http://%s:%d/scan/$taskid/data" % (host, port)
    Args:
        http:
        taskid:

    Returns:
    获取任务日志log
    """
    taskStr = http.get('/scan/%s/log' % (taskid))
    print taskStr

def get_taskStatus(http,taskid):
    """

    Args:
        http:
        taskid:

    Returns:

    """
    taskStr = http.get('/scan/%s/status' % (taskid))
    print taskStr

def task_kill(http,taskid):
    """

    Args:
        http:
        taskid:

    Returns:

    """
    taskStr = http.get('/scan/%s/kill' % (taskid))
    print taskStr

def task_stop(http,taskid):
    """

    Args:
        http:
        taskid:

    Returns:

    """
    taskStr = http.get('/scan/%s/stop' % (taskid))
    print taskStr

def task_list(http,taskid):
    """

    Args:
        http:
        taskid:

    Returns:

    """
    taskStr = http.get('/admin/%s/list' % (taskid))
    print taskStr


host = "127.0.0.1"
port = "8889"
taskid = ""
adminID = "ce5289b7c98f7304a791ef3c22ca3280"
url = 'http://192.168.1.175:8099/test.php?id=1'
data = {}
data['url'] = url
data['tamper'] = "versionedmorekeywords"
data = json.dumps(data)
http = Http('http', host, port)
taskObj = get_taskid(http)
print type(taskObj)
if taskObj.get('success') == 'true' or taskObj.get('success') == True:
    taskid = taskObj.get('taskid')
else:
    print u"获取taskid失败"
#taskid = "9b983be267d395a1"
# 启动扫描任务
send2task(http,data,taskid)
# 查看扫描结果
get_taskData(http,taskid)
# 查看扫描日志
get_taskLog(http,taskid)
# 查看扫描状态
get_taskStatus(http,taskid)
# 停止扫描
#task_stop(http,taskid)
# 杀掉扫描线程
#task_kill(http,taskid)
#task_list(http,taskid)