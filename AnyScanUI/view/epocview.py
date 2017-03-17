# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * url采集、poc执行相关view
 *
 * @author margin 2017/03/12.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/03/12 margin 创建.
 *
 """

import json
import sys
import traceback

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from AnyScanUI.models import poc_urls,poc_main
from AnyScanUI.scanner.epoc.ExecPoc import ExecPoc
from AnyScanUI.spider.BaiduSpider import BaiduSpider
from AnyScanUI.util.util import repeat


@method_decorator(csrf_exempt)
def exe_poc(req):
    """
    poc执行
    :param req:
    :return:
    """
    data=json.loads(req.body)
    targets = data.get("targets")
    threads = 10
    payload = data.get("payload").encode("utf-8")
    commond = data.get("commond").encode("utf-8")

    result = {"status":True,"msg":"成功","data":"","id":[]}
    try:

        exe = ExecPoc(targets,payload,threads,commond)
        result["id"] = exe.start()

    except Exception:
        result = {"status":False,"msg":"POC执行异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@method_decorator(csrf_exempt)
def exec_poc_log(req):
    """
    poc执行日志
    :param req:
    :return:
    """
    reload(sys)
    sys.setdefaultencoding('utf-8')
    data=json.loads(req.body)
    id = data.get("id")

    result = {"status":True,"msg":"成功","log":"","log_status":"running"}
    try:
        obj = poc_main.objects.get(id=id)
        # 主任务的日志
        __mainlog__ = obj.log + "\n"
        # 子任务成功的需要显示到前台
        __chil__ = obj.poc_chil_set.all()
        for child in __chil__:
            if child.vulnerable == "True" or child.vulnerable is True:
                __log = "目标【%s】存在漏洞，POC执行结果【%s】\n" %(str(child.host),str(child.keyword))
                __mainlog__ = __mainlog__ + __log
        result["log"] = __mainlog__
        result["log_status"] = obj.status
    except Exception:
        result = {"status":False,"msg":"获取URL采集日志异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@method_decorator(csrf_exempt)
def baidu_url(req):
    """
    poc执行
    :param req:
    :return:
    """
    data=json.loads(req.body)
    commond = data.get("commond").encode("utf-8")
    result = {"status":True,"msg":"成功","data":[],"id":""}
    try:
        bs = BaiduSpider(commond=commond,count=500)
        __urllist,__id__ = bs.start()
        result["data"] = __urllist
        result["id"] = __id__
    except Exception:
        result = {"status":False,"msg":"URL采集执行异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@method_decorator(csrf_exempt)
def url_log(req):
    """
    url采集的log
    :param req:
    :return:
    """
    reload(sys)
    sys.setdefaultencoding('utf-8')
    data=json.loads(req.body)
    id = data.get("id")

    result = {"status":True,"msg":"成功","data":"","log":"","log_status":"running"}
    try:
        obj = poc_urls.objects.get(id=id)
        result["log"] = obj.log
        if obj.urls is None:
            result["data"] = [{"name": "Url Result"}]
        else:
            try:
                __url__ = repeat(json.loads(obj.urls))
                result["data"] = [{"name":"去重结果共[%s]条记录" % len(__url__),"open":True,"children":__url__}]
            except:
                result["data"] = [{"name": "Url Result"}]
        result["log_status"] = obj.status
    except Exception:
        result = {"status":False,"msg":"获取URL采集日志异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@method_decorator(csrf_exempt)
def poc_main_list(req):
    """
    查询所有的poc执行主记录
    :param req:
    :return:
    """
    reload(sys)
    sys.setdefaultencoding('utf-8')
    __list__ = []
    try:
        ll = poc_main.objects.all()
        for l in ll:
            __l__ = {"id":l.id,"commond":l.commond,"progress":l.progress + "%","threads":l.threads,"status":l.status,
                     "start_time":l.start_time,"end_time":l.end_time}
            __list__.append(__l__)

    except Exception:
        result = {"status":False,"msg":"获取URL采集日志异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(__list__, ensure_ascii=False))

@method_decorator(csrf_exempt)
def poc_chil_list(req):
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
        main = poc_main.objects.get(id=id)
        ll = main.poc_chil_set.all()
        for l in ll:
            __l__ = {"id":l.id,"commond":l.commond,"host":l.host,"vulnerable":l.vulnerable,"keyword":l.keyword}
            __list__.append(__l__)
        result["rows"] = __list__

    except Exception:
        result = {"status":False,"msg":"获取URL采集日志异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))