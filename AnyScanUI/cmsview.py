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
        if threads > 100:threads = 100
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
        result = {"status":False,"msg":"CMS识别启动异常","data":traceback.format_exc()}
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
        result = {"status":False,"msg":"CMS识别日志获取异常","data":traceback.format_exc()}
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
        result = {"status":False,"msg":"CMS识别停止异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))

@method_decorator(csrf_exempt)
def cms_scan_list(req):
    """
    cms识别列表
    :param req:
    :return:
    """
    reload(sys)
    sys.setdefaultencoding('utf-8')
    list = []
    try:
        cmss = CmsInfo.objects.all()
        for cms in cmss:
            cmser = {"id":"","type":"","start_time":"","end_time":"","status":"","progress":""}
            cmser["id"] = str(cms.id)
            cmser["host"] = str(cms.host)
            cmser["start_time"] = str(cms.start_time)
            cmser["end_time"] = str(cms.end_time)
            cmser["status"] = str(cms.status)
            cmser["progress"] = str(cms.progress) + "%"
            cmser["threads"] = str(cms.threads)
            cmser["cms"] = str(cms.cms)
            cmser["version"] = str(cms.version)
            cmser["payload"] = str(cms.payload)
            cmser["keyword"] = str(cms.keyword)
            cmser["start_time"] = str(cms.start_time)
            cmser["end_time"] = str(cms.end_time)

            list.append(cmser)
    except Exception:
        result = {"status":False,"msg":"CMS识别列表获取异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(list, ensure_ascii=False))

@method_decorator(csrf_exempt)
def cms_scan_del(req):
    """
    CMS识别任务删除
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
            cms_info = None
            try:
                cms_info = CmsInfo.objects.get(id=id)
            except:
                print "要删除的id【%s】不存在" % id
            if cms_info is None:
                result = {"status":False,"msg":"当前任务不存在"}
            else:
                # 删除主任务
                CmsInfo.objects.filter(id=id).delete()

    except Exception:
        result = {"status":False,"msg":"删除任务异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))