# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * POC自动调用
 *
 * @author margin 2017/03/22.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/03/22 margin 创建.
 *
 """
import json
import traceback

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from AnyScanUI.AnyPoc.lib.core.poc_core import poc_core
from AnyScanUI.util.constant import ANY_THREAD


@method_decorator(csrf_exempt)
def auto_poc_start(req):
    """
    poc自动执行
    """
    data=json.loads(req.body)
    target = data.get("target")

    result = {"status":True,"msg":"成功","data":"","id_list":[]}
    try:
        poc = poc_core(target,cms = 'wordpress',threads = ANY_THREAD.POC_EXEC)
        id_list = poc.exploit()
        result['id_list'] = id_list
    except Exception:
        result = {"status":False,"msg":"POC执行异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@method_decorator(csrf_exempt)
def auto_poc_stop(req):
    """
    poc自动执行,停止
    """
    data=json.loads(req.body)
    id_list = data.get("id_list")

    result = {"status":True,"msg":"成功","data":""}
    try:
        poc = poc_core(None)
        result["status"], result["msg"] = poc.stop(id_list)
    except Exception:
        result = {"status":False,"msg":"POC执行异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@method_decorator(csrf_exempt)
def auto_poc_log(req):
    """
    poc自动执行,日志
    """
    data=json.loads(req.body)
    id_list = data.get("id_list")

    result = {"status":True,"msg":"成功","data":"","run_status":"stop"}
    try:
        poc = poc_core(None)
        result["status"], result["run_status"], result["data"] = poc.log(id_list)
        vlun_info = poc.vuln(id_list)
        result["data"] = result["data"] + vlun_info
    except Exception:
        result = {"status":False,"msg":"POC执行异常","data":str(traceback.format_exc())}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))