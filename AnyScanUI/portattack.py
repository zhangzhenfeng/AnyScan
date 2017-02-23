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
from models import PortCrack
from attack.AttackObject import AttackObject
from attack.Attacker import Attacker
from util import currenttime

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
        # 创建端口的爆破任务，存储数据库
        # id
        id = str(uuid.uuid1())
        # 爆破开始时间
        start_time = currenttime()
        # 爆破状态
        status = "runing"
        # 爆破的端口类型
        type = "SSH"
        # 扫描进度
        progress = "0.00"
        PortCrack.objects.create(id=id,start_time=start_time,status=status,type=type,progress=progress)

        attackObject = AttackObject()
        # 必须调用setThreads方法，里面有对queue的初始化
        attackObject.setThreads(data["threads"])
        attackObject.id = id
        attackObject.usernames = "/Users/margin/PycharmProjects/AnyScan/AnyScanUI/attack/username.txt"
        attackObject.passwords = "/Users/margin/PycharmProjects/AnyScan/AnyScanUI/attack/password.txt"

        result["logid"] = id
        # 要爆破的ip，port
        attack_dict = data["attack_dict"]
        attacker = Attacker(attackObject)
        attacker.attack(attack_dict)
        # 调用
    except Exception:
        result = {"status":False,"msg":"任务添加异常","data":traceback.format_exc(),"logid":""}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@method_decorator(csrf_exempt)
def portattacklog(req):
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
            if obj.status == "success":
                result["attack_status"] = obj.status
                result["result"] = str(obj.result)

    except Exception:
        result = {"status":False,"msg":"获取爆破日志异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))