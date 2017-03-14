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

from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json,traceback,uuid,datetime,sys
from AnyScanUI.epoc.ExecPoc import ExecPoc
from AnyScanUI.spider.BaiduSpider import BaiduSpider
from AnyScanUI.models import poc_urls
from AnyScanUI.util import repeat

@method_decorator(csrf_exempt)
def exe_poc(req):
    """
    poc执行
    :param req:
    :return:
    """
    data=json.loads(req.body)
    targets = data.get("targets").encode("utf-8")
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
        bs = BaiduSpider(commond=commond,count=10000)
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
    data=json.loads(req.body)
    id = data.get("id")

    result = {"status":True,"msg":"成功","data":"","log":"","log_status":"running"}
    try:
        obj = poc_urls.objects.get(id=id)
        result["log"] = obj.log
        if obj.urls is None:
            result["data"] = [{"name": "Url Result"}]
        else:
            __url__ = repeat(json.loads(obj.urls))
            result["data"] = [{"name":"去重结果共[%s]条记录" % len(__url__),"open":True,"children":__url__}]
        result["log_status"] = obj.status
    except Exception:
        result = {"status":False,"msg":"POC执行异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))