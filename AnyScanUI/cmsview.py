# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * cms识别
 *
 * @author margin 2017/03/08.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/03/08 margin 创建.
 *
 """

from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json,traceback,uuid,datetime,sys
from models import CmsInfo
from util import currenttime
from cms.CmsScanner import CmsScanner

@method_decorator(csrf_exempt)
def cms_scan(req):
    """
    cms识别
    :param req:
    :return:
    """
    data=json.loads(req.body)
    url = data.get("url")
    threads = data.get("threads")
    result = {"status":True,"msg":"成功","data":"","ids":[]}
    try:
        if threads is None:threads=10
        threads = int(threads)
        if threads > 20:threads = 20
        url_list = url.split(",")
        for url in url_list:
            url = str(url)
            if url is None or url == "":
                continue
            if url[0:4] != "http":
                url = "http://" + url
            s = CmsScanner(url,threads)
            id = s.start()
            result["ids"].append(id)

    except Exception:
        result = {"status":False,"msg":"获取爆破日志异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@method_decorator(csrf_exempt)
def cms_scan_log(req):
    """
    cms识别log
    :param req:
    :return:
    """
    reload(sys)
    sys.setdefaultencoding('utf-8')
    data=json.loads(req.body)
    id_list = data.get("ids")
    result = {"status":True,"msg":"成功","data":"","success":"success"}
    log = ""
    try:
        for id in id_list:
            obj = CmsInfo.objects.get(id=id)
            log = log + obj.log + "\n"
            if obj.status == "running":
                result["success"] = "running"
        result["data"] = log
    except Exception:
        result = {"status":False,"msg":"获取爆破日志异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@method_decorator(csrf_exempt)
def cms_scan_stop(req):
    """
    cms识别停止
    :param req:
    :return:
    """
    reload(sys)
    sys.setdefaultencoding('utf-8')
    data=json.loads(req.body)
    id_list = data.get("ids")
    result = {"status":True,"msg":"成功","data":"","success":"success"}
    log = ""
    try:
        for id in id_list:
            CmsInfo.objects.filter(id=id,locker="false",status="running").update(end_time=currenttime(),status="stop",locker="true")
        result["data"] = log
    except Exception:
        result = {"status":False,"msg":"获取爆破日志异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))