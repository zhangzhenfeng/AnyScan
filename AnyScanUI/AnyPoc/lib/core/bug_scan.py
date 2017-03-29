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

import imp,traceback,sys,subprocess,os,Queue

from AnyScanUI.util.constant import BUG_SCAN,ANY_THREAD,POC_PLUGINS_DIR
from AnyScanUI.AnyPoc.lib.util.PocThread import PocThread
from AnyScanUI.AnyPoc.lib.util.util import files, settimeout

class console_text(object):

    def __init__(self):
        self.buffer = []

    def write(self, *args, **kwargs):
        self.buffer.append(args)
class __BugScan__():

    target = None
    # 不带python文件，只有路径
    pypath = None

    def __init__(self,target,pypath=BUG_SCAN.BUGSCAN_PATH):
        self.target = target
        self.pypath = pypath

        self.result = {'poc_name': None, 'result': False, 'target':self.target}
    def load_poc(self,path,poc_name):
        path = os.path.join(path,poc_name)
        poc = imp.load_source('audit', path)
        return poc.audit

    #@settimeout(1)
    def __exec__(self,poc_name):
        try:
            poc = self.load_poc(self.pypath,poc_name)
            sys.path.append(self.pypath)
            sys.path.append(POC_PLUGINS_DIR.PLUGINS_DIR)
            #from AnyScanUI.AnyPoc.plugins.bugscan.dummy.miniCurl import Curl as curl
            from dummy import *
            poc.func_globals.update(locals())
            try:
                ret = poc(str(self.target))
                if ret == self.target:
                    print "[%s]存在漏洞，POC[%s]" % (str(self.target),str(poc_name))
            except:
                print 'traceback.print_exc():'; traceback.print_exc()
            print '正在使用【%s】' % poc_name
            return ''
        except Exception, e:
            print 'traceback.print_exc():'; traceback.print_exc()
            #print 'traceback.format_exc():\n%s' % traceback.format_exc()
            return ''
    #@settimeout(2)
    def exploit(self,poc_name):
        try:
            log = self.__exec__(poc_name)
            return False
        except:
            print traceback.print_exc()
            self.result['result'] = True
            self.result['poc_name'] = poc_name
            return self.result


class BugScan():

    target = None
    # 不带python文件，只有路径
    pypath = None
    poc_name = ''
    target_queue = None
    threads = ANY_THREAD.POC_EXEC

    def __init__(self,target,pypath=BUG_SCAN.BUGSCAN_PATH,threads = ANY_THREAD.POC_EXEC):
        self.target = target
        self.pypath = pypath
        self.threads = threads

    def load(self,path):
        try:
            self.target_queue = files(path)
            print "当前有POC【%s】个" % self.target_queue.qsize()
            return self.target_queue
        except:
            traceback.format_exc()

    def exploit(self):
        # 加载所有的poc
        queue = self.load(self.pypath)
        # bugscan对象
        bugscan = __BugScan__(self.target,pypath=self.pypath)
        # 多线程调用poc
        thread = PocThread(threads=self.threads, func=bugscan.exploit, queue=queue)
        thread.start()