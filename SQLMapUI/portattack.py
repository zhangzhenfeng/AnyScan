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
import json,traceback,uuid,datetime
from models import PortCrack
from attack.AttackObject import AttackObject
from attack.Attacker import Attacker

@method_decorator(csrf_exempt)
def portattack(req):
    """
    端口爆破
    :param req:
    :return:
    """
    data=json.loads(req.body)
    print data
    result = {"status":True,"msg":"成功","data":""}
    try:
        # 创建端口的爆破任务，存储数据库
        # id
        id = str(uuid.uuid1())
        # 爆破开始时间
        start_time = datetime.datetime.now().strftime('%Y-%M-%d %H:%M:%S')
        # 爆破状态
        status = "runing"
        # 爆破的端口类型
        type = "SSH"
        # 扫描进度
        progress = "0.00"
        PortCrack.objects.create(id=id,start_time=start_time,status=status,type=type,progress=progress)

        attackObject = AttackObject()
        attackObject.threads = 5
        attackObject.timeout = 32
        attackObject.usernames = "username.txt"
        attackObject.passwords = "password.txt"

        # 要爆破的ip，port
        attack_dict = data["attack_dict"]
        attacker = Attacker(attackObject)
        attacker.attack(attack_dict)
        # 调用
    except Exception:
        result = {"status":False,"msg":"任务添加异常异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))