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
def auto_poc(req):
    """
    poc自动执行
    """
    data=json.loads(req.body)
    target = data.get("target")

    result = {"status":True,"msg":"成功","data":"","id":""}
    try:
        poc = poc_core(target,cms = 'wordpress',threads = ANY_THREAD.POC_EXEC)
        poc.exploit()

    except Exception:
        result = {"status":False,"msg":"POC执行异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))