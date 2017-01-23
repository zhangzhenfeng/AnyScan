# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json,time
from util import combination_tampper
from Http import Http
from django import forms
from models import User

host = "127.0.0.1"
port = "8889"

# 表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

#注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))

def login_index(req):
    return render_to_response("login.html")

#登陆
@method_decorator(csrf_exempt)
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/SQLMapUI/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/SQLMapUI/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf})

#登陆成功
def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})

#退出
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

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
    taskObj = json.loads(taskStr)
    return taskObj

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
    taskObj = json.loads(taskStr)
    return taskObj

def get_taskLog(http,taskid):
    """
    curl http://%s:%d/scan/$taskid/data" % (host, port)
    Args:
        http:
        taskid:

    Returns:
    获取任务日志log
    """
    if type(taskid) == list and len(taskid) > 0:
        taskid = taskid[0]
    taskStr = http.get('/scan/%s/log' % (taskid))
    taskObj = json.loads(taskStr)
    return taskObj

def get_taskStatus(http,taskid):
    """

    Args:
        http:
        taskid:

    Returns:

    """
    taskStr = http.get('/scan/%s/status' % (taskid))
    taskObj = json.loads(taskStr)
    return taskObj

def task_kill(http,taskid):
    """

    Args:
        http:
        taskid:

    Returns:

    """
    taskStr = http.get('/scan/%s/kill' % (taskid))
    taskObj = json.loads(taskStr)
    return taskObj

def task_delete(http,taskid):
    """

    Args:
        http:
        taskid:

    Returns:

    """
    print taskid
    taskStr = http.get('/scan/%s/delete' % (taskid))
    taskObj = json.loads(taskStr)
    return taskObj

def stop(http,taskid):
    """

    Args:
        http:
        taskid:

    Returns:

    """
    taskStr = http.get('/scan/%s/stop' % (taskid))
    taskObj = json.loads(taskStr)
    return taskObj

def task_list(http,taskid):
    """

    Args:
        http:
        taskid:

    Returns:

    """
    taskStr = http.get('/admin/%s/list' % (taskid))
    taskObj = json.loads(taskStr)
    return taskObj

def task_utime(http,taskid):
    lists = get_taskLog(http,taskid)
    # 任务开始时间
    start_time = 0
    # 任务结束时间
    end_time = 0
    # 任务耗时
    utime = 0
    log = lists.get("log")
    # 获取年月日
    yearMD= time.strftime("%Y-%m-%d",time.localtime())
    if lists.get("success") and len(log) > 0:
        # 任务开始时间
        start_time = yearMD + " " + log[0].get("time")
        #start_time = time.strptime(yearMD + " " + log[0].get("time"),"%Y-%m-%d %H:%M:%S")
        print start_time
        # 任务结束时间
        #end_time = time.strptime(yearMD + " " + log[len(log)-1].get("time"),"%Y-%m-%d %H:%M:%S")
        end_time = yearMD + " " + log[len(log)-1].get("time")
        print end_time
    else:
        pass
    return start_time,end_time

@method_decorator(csrf_exempt)
def add_task(req,tamper = ""):
    data=json.loads(req.body)
    taskid = ""
    if tamper:
        data['tamper'] = tamper
    data = json.dumps(data)
    http = Http('http', host, port)
    taskObj = get_taskid(http)
    if taskObj.get('success') == 'true' or taskObj.get('success') == True:
        taskid = taskObj.get('taskid')
    else:
        taskObj["msg"] = u"获取taskID失败"
        return taskObj
    # 启动扫描任务
    taskObj = send2task(http,data,taskid)
    if taskObj.get("success") == "false":
        taskObj["msg"] = u"获取taskID成功但任务启动失败！"
    return taskid

@method_decorator(csrf_exempt)
def bash_task(req):
    data=json.loads(req.body)
    taskObj = {"success":True,"msg":"","taskid":[]}
    print data
    if data.get("bash") == "1":
        combinationer = combination_tampper()
        for tamper in combinationer:
            taskObj["taskid"].append(add_task(req,tamper))
    else:
        taskObj["taskid"].append(add_task(req))

    return HttpResponse(json.dumps(taskObj, ensure_ascii=False))


@method_decorator(csrf_exempt)
def alltasks(req):
    http = Http('http', host, port)
    # taskObj = get_taskid(http)
    # print type(taskObj)
    # if taskObj.get('success') == 'true' or taskObj.get('success') == True:
    #     taskid = taskObj.get('taskid')
    # else:
    #     print u"获取taskid失败"
    taskid = "0"
    # 启动扫描任务
    #send2task(http,data,taskid)
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
    lists = task_list(http,taskid)
    data = {"total":lists.get("tasks_num"),"rows":[]}
    # 声明任务列表对象
    # 获取所有的任务id
    for taskid in lists.get("tasks"):
        rows = {"id":"id","status":"1","result":"1","progress":"1","start_time":"1H","end_time":"1H"}
        rows["id"] = taskid
        rows["status"] = lists.get("tasks").get(taskid)
        rows["start_time"],rows["end_time"] = task_utime(http,taskid)
        taskData = get_taskData(http,taskid)
        print taskData
        if taskData.get("success") == True:
            if len(taskData.get("data")) == 0  and len(taskData.get("error")) < 1:
                rows["result"] = u"扫描未完成或无漏洞"
            elif len(taskData.get("data")) == 0 and len(taskData.get("error")) > 0:
                rows["result"] = u"扫描出错"
            elif len(taskData.get("data")) > 0 and taskData.get("data")[0].get("status") == 1:
                rows["result"] = u"有漏洞"
            else:
                rows["result"] = u"无漏洞"
        else:
            rows["result"] = u"任务失败"
        data["rows"].append(rows)

    return HttpResponse(json.dumps(data["rows"], ensure_ascii=False))

@method_decorator(csrf_exempt)
def web_log(req):
    http = Http('http', host, port)
    data=json.loads(req.body)
    log = get_taskLog(http,data.get("taskid"))
    return HttpResponse(json.dumps(log.get("log"), ensure_ascii=False))

@method_decorator(csrf_exempt)
def task_stop(req):
    data=json.loads(req.body)
    print data
    http = Http('http', host, port)
    obj = {"success":"true","msg":"任务已停止"}
    if data and data.get("taskid"):
        for taskid in data.get("taskid"):
            obj = stop(http,taskid)
            if obj.get("success") == "false" or obj.get("success") == False:
                return HttpResponse(json.dumps(obj, ensure_ascii=False))
    return HttpResponse(json.dumps(obj, ensure_ascii=False))

@method_decorator(csrf_exempt)
def web_kill(req):
    data=json.loads(req.body)
    print data
    http = Http('http', host, port)
    obj = {"success":"true","msg":"kill成功"}
    if data and data.get("taskid"):
        for taskid in data.get("taskid"):
            obj = task_kill(http,taskid)
            if obj.get("success") == "false" or obj.get("success") == False:
                obj["msg"] = obj.get("message")
                return HttpResponse(json.dumps(obj, ensure_ascii=False))
    return HttpResponse(json.dumps(obj, ensure_ascii=False))

@method_decorator(csrf_exempt)
def web_delete(req):
    data=json.loads(req.body)
    print data
    http = Http('http', host, port)
    obj = {"success":"true","msg":"删除成功"}
    if data and data.get("taskid"):
        for taskid in data.get("taskid"):
            obj = task_delete(http,taskid)
            if obj.get("success") == "false" or obj.get("success") == False:
                obj["msg"] = obj.get("message")
                return HttpResponse(json.dumps(obj, ensure_ascii=False))
    return HttpResponse(json.dumps(obj, ensure_ascii=False))

@method_decorator(csrf_exempt)
def web_flush(req):
    """

    Args:
        http:
        taskid:

    Returns:

    """
    http = Http('http', host, port)
    taskStr = http.get('/admin/0/flush')
    taskObj = json.loads(taskStr)
    return HttpResponse(json.dumps(taskObj, ensure_ascii=False))