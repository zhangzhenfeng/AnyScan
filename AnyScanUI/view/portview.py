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

import json
import sys
import traceback
import uuid

from AnyScanUI.scanner.port.AttackObject import AttackObject
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from AnyScanUI.models import PortCrack,PortCrackChild
from AnyScanUI.scanner.port.Attacker import Attacker
from AnyScanUI.util.util import currenttime


@method_decorator(csrf_exempt)
def portattack(req):
    """
    端口爆破
    :param req:
    :return:
    """
    data=json.loads(req.body)
    result = {"status":True,"msg":"成功","data":"","logid":""}

    # id
    id = str(uuid.uuid1())
    try:
        if data["type"] == "create":
            # 创建端口的爆破任务，存储数据库
            # 爆破开始时间
            start_time = currenttime()
            # 爆破状态
            status = "running"
            # 爆破任务类型
            type = "ALL"
            # 扫描进度
            progress = "0.00"
            # 创建主任务数据
            PortCrack.objects.create(id=id,start_time=start_time,status=status,type=type,progress=progress)

            attackObject = AttackObject()
            # 必须调用setThreads方法，里面有对queue的初始化
            attackObject.setThreads(data["threads"])
            print attackObject.attack_queue_dict
            attackObject.pid = id
            attackObject.usernames = "/Users/margin/PycharmProjects/AnyScan/AnyScanUI/port/ssh_username.txt"
            attackObject.passwords = "/Users/margin/PycharmProjects/AnyScan/AnyScanUI/port/ssh_password.txt"

            # 实时显示任务的id
            result["logid"] = id
            # 要爆破的ip，port
            attack_dict = data["attack_dict"]
            attacker = Attacker(attackObject)
            status = attacker.attack(attack_dict,attack_task_id_dict = {})
            if status == False:
                result["status"] == False
                result["msg"] == "任务添加异常，请查看日志"
        elif data["type"] == "start":
            id = data["id"]
            if id is None or id == "":
                result = {"status":False,"msg":"任务ID不可为空"}
                return HttpResponse(json.dumps(result, ensure_ascii=False))
            # 判断任务id是否存在
            portcrack = PortCrack.objects.get(id=id)
            if portcrack is None:
                result = {"status":False,"msg":"您所选的任务ID不存在"}
                return HttpResponse(json.dumps(result, ensure_ascii=False))
            # 如果任务不是暂停状态就在启动任务
            if portcrack.status != "pause":
                result = {"status":False,"msg":"您所选的任务不是【%s】，不能启动" % portcrack.status}
                return HttpResponse(json.dumps(result, ensure_ascii=False))

            # 查询任务信息和子任务信息，组织数据给Attacker.py
            child_set = portcrack.portcrackchild_set.all()
            # 组织给Attacker.py的数据  attack_dict: {"ip":[80,3306],"ip2":[22]}
            attack_dict = {}
            # 搞一个字典{"ip+port":id}，为了能让attacker正确的取出当前任务的id
            attack_task_id_dict = {}
            for child in child_set:
                __ip = attack_dict.get(child.ip)
                if __ip is None or __ip == "":
                    attack_dict[child.ip] = [child.port]
                else:
                    attack_dict[child.ip].append(child.port)
                attack_task_id_dict[child.ip+child.port] = child.id

            # 更新该任务状态
            PortCrack.objects.filter(id=id).update(status="running",end_time=currenttime())
            attackObject = AttackObject()
            # 当前攻击启动的类型
            attackObject.type = "start"
            attackObject.pid = id
            attacker = Attacker(attackObject)
            status = attacker.attack(attack_dict,attack_task_id_dict)
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
    obj = None
    log = ""
    try:
        if logid is "" or logid is None:
            result = {"status":False,"msg":"日志id为空","data":"日志id为空"}
        else:
            try:
                obj = PortCrack.objects.get(id=logid)
                child_set = obj.portcrackchild_set.all()
                for child in child_set:
                    # 统计日志
                    log = log + str(child.log) + "\n"
            except:
                result = {"status":False,"msg":"任务被删除！","data":"任务被删除！"}
                print traceback.format_exc()
                return HttpResponse(json.dumps(result, ensure_ascii=False))
            result["data"] = log
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
                a=PortCrack.objects.filter(id=id).update(status="pause")
                # 更新从任务,只有任务是运行状态的才进行暂停，失败或者success的就不用暂停。
                b=PortCrackChild.objects.filter(pid=id,status="running").update(status="pause")

    except Exception:
        result = {"status":False,"msg":"更新任务状态异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@method_decorator(csrf_exempt)
def portattackdel(req):
    """
    暴力破解任务删除
    :param req:
    :return:
    """
    data=json.loads(req.body)
    id = data.get("id")
    result = {"status":True,"msg":"删除成功","data":""}
    try:
        if id is "" or id is None:
            result = {"status":False,"msg":"id不能为空"}
        else:
            portattack = None
            try:
                portattack = PortCrack.objects.get(id=id)
            except:
                print "要删除的id【%s】不存在" % id
            if portattack is None:
                result = {"status":False,"msg":"当前任务不存在"}
            else:
                # 删除主任务
                PortCrack.objects.filter(id=id).delete()
                # 删除子任务
                PortCrackChild.objects.filter(pid=id).delete()

    except Exception:
        result = {"status":False,"msg":"删除任务异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))


@method_decorator(csrf_exempt)
def portattackchild_list(req):
    """
    获取所有的暴力破解任务
    :param req:
    :return:
    """
    id = ""
    try:
        data=json.loads(req.body)
        id = data.get("id")
    except:
        result = {"status":False,"msg":"参数id为空，请查看后台日志"}
        return HttpResponse(json.dumps(result, ensure_ascii=False))
    result = {"status":True,"msg":"成功","total":0,"rows":[]}
    list = []
    try:
        all = PortCrack.objects.get(id=id).portcrackchild_set.all()
        for a in all:
            attacker = {"id":"","type":"","start_time":"","end_time":"","status":"","progress":"","ip":"","port":""}
            attacker["id"] = str(a.id)
            attacker["type"] = str(a.type)
            attacker["start_time"] = str(a.start_time)
            attacker["end_time"] = str(a.end_time)
            attacker["status"] = str(a.status)
            attacker["progress"] = str(a.progress) + "%"
            attacker["ip"] = str(a.ip)
            attacker["port"] = str(a.port)
            attacker["type"] = str(a.type)
            attacker["threads"] = str(a.threads)
            attacker["username"] = str(a.username)
            attacker["password"] = str(a.password)
            list.append(attacker)
        result["rows"] = list
    except Exception:
        result = {"status":False,"msg":"获取爆破任务列表失败，请查看后台日志"}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))