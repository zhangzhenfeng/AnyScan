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
import json,sys
import traceback

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from AnyScanUI.AnyPoc.lib.core.poc_core import poc_core
from AnyScanUI.util.constant import ANY_THREAD
from AnyScanUI.models import cms_poc_main,cms_poc_chil


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
    reload(sys)
    sys.setdefaultencoding('utf-8')
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

@method_decorator(csrf_exempt)
def auto_poc_data(req):
    """
    poc扫描任务
    """
    reload(sys)
    sys.setdefaultencoding('utf-8')
    list = []
    try:
        cms = cms_poc_main.objects.all()
        for _ in cms:
            cmser = {"id":"","poc_size":"","start_time":"","end_time":"","status":"","progress":"","log":"","target":"","threads":""}
            cmser["id"] = str(_.id)
            cmser["target"] = str(_.target)
            cmser["poc_size"] = str(_.poc_size)
            cmser["start_time"] = str(_.start_time)
            cmser["end_time"] = str(_.end_time)
            cmser["status"] = str(_.status)
            cmser["progress"] = str(_.progress) + "%"
            cmser["threads"] = str(_.threads)
            cmser["log"] = str(_.log)

            list.append(cmser)
    except Exception:
        result = {"status":False,"msg":"获取信息异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(list, ensure_ascii=False))

@method_decorator(csrf_exempt)
def auto_poc_data_chil(req):
    """
    查询所有的poc执行子记录
    :param req:
    :return:
    """
    reload(sys)
    sys.setdefaultencoding('utf-8')
    id = ""
    try:
        data=json.loads(req.body)
        id = data.get("id")
    except:
        result = {"status":False,"msg":"参数id为空，请查看后台日志"}
        return HttpResponse(json.dumps(result, ensure_ascii=False))
    result = {"status":True,"msg":"成功","total":0,"rows":[]}
    __list__ = []
    try:
        main = cms_poc_main.objects.get(id=id)
        ll = main.cms_poc_chil_set.all()
        for l in ll:
            __l__ = {"id":l.id,"poc_type":l.poc_type,"poc_size":l.poc_size,"poc_name":l.poc_name,"log":l.log,"target":l.target}
            __list__.append(__l__)
        result["rows"] = __list__

    except Exception:
        result = {"status":False,"msg":"获取数据异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@method_decorator(csrf_exempt)
def auto_poc_del(req):
    """
    poc自动执行,删除
    """
    data=json.loads(req.body)
    id_list = data.get("id_list")

    result = {"status":True,"msg":"成功","data":""}
    try:
        poc = poc_core(None)
        result["status"], result["msg"] = poc.delete(id_list)
    except Exception:
        result = {"status":False,"msg":"POC执行异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))