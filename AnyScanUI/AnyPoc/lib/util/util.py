# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * 工具库
 *
 * @author margin 2017/03/22.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/03/22 margin 创建.
 *
 """
import Queue
from threading import Thread

from AnyScanUI.scanner.cms.CmsScanner import CmsScanner
from AnyScanUI.models import CmsInfo
import os

def cms(url,threads):
    """
    调用CMS识别任务
    :param url:
    :param threads:
    :return: {'status':False,'cms':'wordpress','version':'v1.1'}
    """
    result = {'status':False,'cms':'','version':'','msg':'未识别出CMS'}
    cmsScanner = CmsScanner(url,threads)
    cmsScanner_id = cmsScanner.start()

    # 循环判断CMS识别任务是否完成
    cmsInfoObj = None
    mark = True
    while mark:
        cmsInfoObj = CmsInfo.objects.get(id=cmsScanner_id)
        if cmsInfoObj is None:
            continue
        cms = cmsInfoObj.cms
        version = cmsInfoObj.version
        msg = cmsInfoObj.log
        if cms is not None and cms != "":
            result = {'status':True,'cms':cms,'version':version,'msg':msg}
            break

    return result

def files(path):
    fileNames = os.listdir(path)
    target_queue = Queue.Queue(maxsize=len(fileNames))
    for name in fileNames:
        if ".py" in name and name != "__init__.py":
            target_queue.put(name)

    return target_queue

class console_text(object):

    def __init__(self):
        self.buffer = []

    def write(self, *args, **kwargs):
        self.buffer.append(args)

class bugscan_util():

    def load_poc(self,path):
        pass


class TimeoutException(Exception):
    pass

ThreadStop = Thread._Thread__stop#获取私有函数

def settimeout(timeout):
    def decorator(function):
        def decorator2(*args,**kwargs):
            class TimeLimited(Thread):
                def __init__(self,_error= None,):
                    Thread.__init__(self)
                    self._error =  _error

                def run(self):
                    try:
                        self.result = function(*args,**kwargs)
                    except Exception,e:
                        self._error =e

                def _stop(self):
                    if self.isAlive():
                        ThreadStop(self)

            t = TimeLimited()
            t.start()
            t.join(timeout)

            if isinstance(t._error,TimeoutException):
                t._stop()
                raise TimeoutException('timeout for %s' % (repr(function)))

            if t.isAlive():
                t._stop()
                raise TimeoutException('timeout for %s' % (repr(function)))

            if t._error is None:
                return t.result

        return decorator2
    return decorator