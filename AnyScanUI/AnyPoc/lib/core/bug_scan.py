# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * BugScan调用类
 *
 * @author margin 2017/03/22.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/03/22 margin 创建.
 *
 """

import imp,traceback,sys,os

from AnyScanUI.util.constant import BUG_SCAN,ANY_THREAD,POC_PLUGINS_DIR
from AnyScanUI.AnyPoc.lib.util.PocThread import PocThread
from AnyScanUI.AnyPoc.lib.util.util import files
from AnyScanUI.models import cms_poc_chil,cms_poc_main
from AnyScanUI.util.util import currenttime
import uuid

class __BugScan__():

    target = None
    # 不带python文件，只有路径
    pypath = None

    def __init__(self,target,pypath=BUG_SCAN.BUGSCAN_PATH,pid="",poc_size=0):
        self.target = target
        self.pypath = pypath
        self.pid = pid
        self.poc_size = poc_size

        self.result = {'poc_name': None, 'result': False, 'target':self.target}

    def load_poc(self,path,poc_name):
        path = os.path.join(path,poc_name)
        poc = imp.load_source('audit', path)
        return poc.audit

    #@settimeout(1)
    def __exec__(self,poc_name,current_poc_size):
        try:
            # 更新cms——poc识别的主任务
            self.update_main(poc_name,current_poc_size)
            poc = self.load_poc(self.pypath,poc_name)
            sys.path.append(self.pypath)
            sys.path.append(POC_PLUGINS_DIR.PLUGINS_DIR)
            from dummy import *
            poc.func_globals.update(locals())
            try:
                # 执行加载到的poc
                ret = poc(str(self.target))
                # 如果返回的url和传入的url相同，则存在漏洞
                if ret == self.target:
                    log = "[%s]存在漏洞，POC[%s]" % (str(self.target),str(poc_name))
                    print log

                    parent = cms_poc_main()
                    parent.id = self.pid
                    id = str(uuid.uuid1())
                    cms_poc_chil.objects.create(id=id,pid=parent,poc_type="BugScan",target=self.target,poc_name=poc_name,poc_size=self.poc_size,log=log)
                    return True
            except:
                print 'traceback.print_exc():'; traceback.print_exc()
            print '正在使用【%s】' % poc_name

            return False
        except Exception, e:
            print 'traceback.print_exc():'; traceback.print_exc()
            return False

    def update_main(self,poc_name,current_poc_size):
        if current_poc_size == 0:
            progress = "100"
            cms_poc_main.objects.filter(id=self.pid,locker="false").update(end_time=currenttime(),log="[%s]正在使用POC[%s]" % (progress+"%",poc_name),status="success",progress=progress,locker="true")

        # 计算进度
        progress = 1-float(format(float(current_poc_size)/float(self.poc_size),'.4f'))
        progress = '%.2f' % (progress * 100)
        cms_poc_main.objects.filter(id=self.pid,locker="false").update(end_time=currenttime(),log="[%s]正在使用POC[%s]" % (str(progress)+"%",poc_name),progress=progress)

    #@settimeout(2)
    def exploit(self,poc_name,current_poc_size):
        try:
            if self.isstop():
                return self.__exec__(poc_name,current_poc_size)
            else:
                return "stop"
        except:
            print traceback.print_exc()
            self.result['result'] = True
            self.result['poc_name'] = poc_name
            return self.result

    def isstop(self):
        obj = cms_poc_main.objects.get(id=self.pid)
        if obj:
            if obj.status == "running":
                return True
            else:
                return False
        else:
            return False



class BugScan():

    target = None
    # 不带python文件，只有路径
    pypath = None
    poc_name = ''
    target_queue = None
    threads = ANY_THREAD.POC_EXEC
    poc_size = 0

    def __init__(self,target,pypath=BUG_SCAN.BUGSCAN_PATH,threads = ANY_THREAD.POC_EXEC,pid=""):
        self.target = target
        self.pypath = pypath
        self.threads = threads
        self.pid = pid

        # 加载所有的poc
        self.queue = self.load(self.pypath)

    def load(self,path):
        try:
            self.target_queue = files(path)
            print "当前有POC【%s】个" % self.target_queue.qsize()
            self.poc_size = self.target_queue.qsize()
            return self.target_queue
        except:
            traceback.format_exc()

    def exploit(self):

        # bugscan对象
        bugscan = __BugScan__(self.target,pypath=self.pypath,pid=self.pid,poc_size=self.poc_size)
        # 多线程调用poc
        thread = PocThread(threads=self.threads, func=bugscan.exploit, queue=self.queue)
        thread.start()