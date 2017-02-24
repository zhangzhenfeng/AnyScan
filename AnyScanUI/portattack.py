# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * 端口爆破相关view
 *
 * @author margin 2017/02/20.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/02/20 margin 创建.
 *
 """

from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json,traceback,uuid,datetime,sys
from models import PortCrack,PortCrackChild
from attack.AttackObject import AttackObject
from attack.Attacker import Attacker
from util import currenttime
from django.core import serializers

@method_decorator(csrf_exempt)
def portattack(req):
    """
    端口爆破
    :param req:
    :return:
    """
    data=json.loads(req.body)
    result = {"status":True,"msg":"成功","data":"","logid":""}
    try:
        if data["type"] == "create":
            # 创建端口的爆破任务，存储数据库
            # id
            pid = str(uuid.uuid1())
            # 爆破开始时间
            start_time = currenttime()
            # 爆破状态
            status = "running"
            # 爆破任务类型
            type = "ALL"
            # 扫描进度
            progress = "0.00"
            # 创建主任务数据
            PortCrack.objects.create(id=pid,start_time=start_time,status=status,type=type,progress=progress)

            attackObject = AttackObject()
            # 必须调用setThreads方法，里面有对queue的初始化
            attackObject.setThreads(data["threads"])
            attackObject.pid = pid
            attackObject.usernames = "/Users/margin/PycharmProjects/AnyScan/AnyScanUI/attack/username.txt"
            attackObject.passwords = "/Users/margin/PycharmProjects/AnyScan/AnyScanUI/attack/password.txt"

            # 实时显示任务的id
            result["logid"] = pid
            # 要爆破的ip，port
            attack_dict = data["attack_dict"]
            attacker = Attacker(attackObject)
            status = attacker.attack(attack_dict)
            if status == False:
                result["status"] == False
                result["msg"] == "任务添加异常，请查看日志"
        elif data["type"] == "start":
            id = data["id"]
            if id is None or id == "":
                result = {"status":False,"msg":"任务ID不可为空"}
                return HttpResponse(json.dumps(result, ensure_ascii=False))
            # 判断id是否存在
            portcrack = PortCrackChild.objects.get(pid=id)
            if portcrack is None:
                result = {"status":False,"msg":"您所选的任务ID不存在"}
                return HttpResponse(json.dumps(result, ensure_ascii=False))

            # 更新该任务状态
            PortCrack.objects.filter(id=id).update(status="running",end_time=currenttime())
            attackObject = AttackObject()
            # 当前攻击启动的类型
            attackObject.type = "start"
            attacker = Attacker(attackObject)
            status = attacker.attack("")
            if status == False:
                result["status"] == False
                result["msg"] == "任务启动异常，请查看日志"

    except Exception:
        result = {"status":False,"msg":"任务添加异常","data":traceback.format_exc(),"logid":""}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@method_decorator(csrf_exempt)
def portattacklog(req):
    """
    暴力破解日志
    :param req:
    :return:
    """
    reload(sys)
    sys.setdefaultencoding('utf8')
    data=json.loads(req.body)
    logid = data.get("logid")
    result = {"status":True,"msg":"成功","data":"","attack_status":False,"result":[]}
    try:
        if logid is "" or logid is None:
            result = {"status":False,"msg":"日志id为空","data":"日志id为空"}
        else:
            obj = PortCrack.objects.get(id=logid)
            result["data"] = str(obj.log)
            result["attack_status"] = obj.status
            result["result"] = str(obj.result)

    except Exception:
        result = {"status":False,"msg":"获取爆破日志异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))


@method_decorator(csrf_exempt)
def portattack_list(req):
    """
    获取所有的暴力破解任务
    :param req:
    :return:
    """
    result = {"status":True,"msg":"成功","total":0,"rows":[]}
    list = []
    try:
        all = PortCrack.objects.all()
        for a in all:
            attacker = {"id":"","type":"","start_time":"","end_time":"","status":"","progress":""}
            attacker["id"] = str(a.id)
            attacker["type"] = str(a.type)
            attacker["start_time"] = str(a.start_time)
            attacker["end_time"] = str(a.end_time)
            attacker["status"] = str(a.status)
            attacker["progress"] = str(a.progress) + "%"
            list.append(attacker)
        result["rows"] = list
        result["total"] = len(list)
    except Exception:
        result = {"status":False,"msg":"获取爆破任务列表失败，请查看后台日志","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(list, ensure_ascii=False))


@method_decorator(csrf_exempt)
def portattackpause(req):
    """
    暴力破解暂停
    :param req:
    :return:
    """
    data=json.loads(req.body)
    id = data.get("id")
    result = {"status":True,"msg":"成功","data":""}
    try:
        if id is "" or id is None:
            result = {"status":False,"msg":"id不能为空"}
        else:
            portattack = PortCrack.objects.get(id=id)
            if portattack.status != "running":
                result = {"status":False,"msg":"当前任务已停止，不可暂停！"}
            else:
                # 更新主任务
                PortCrack.objects.filter(id=id).update(status="pause")
                # 更新从任务
                PortCrackChild.objects.filter(pid=id).update(status="pause")

    except Exception:
        result = {"status":False,"msg":"更新任务状态异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))