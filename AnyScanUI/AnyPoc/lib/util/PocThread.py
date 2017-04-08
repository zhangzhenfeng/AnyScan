# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * Poc多线程类
 *
 * @author margin 2017/03/22.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/03/22 margin 创建.
 *
 """

import threading
import traceback

from AnyScanUI.util.constant import ANY_THREAD

class __PocThreadObject__():
    targets_queue = None

class __PocThread__(threading.Thread):

    func = None
    targets_queue = None

    def __init__(self,func=None,queue=None):
        threading.Thread.__init__(self)
        #super(Attack, self).__init__(attackObject)
        self.func = func
        self.targets_queue = queue

    def run(self):
        while True:
            if not self.targets_queue.empty():
                try:
                    target =  self.targets_queue.get()
                    current_poc_size = self.targets_queue.qsize()
                    #print target
                    self.func(target,current_poc_size)
                except:
                    pass
                    #print traceback.format_exc()
            else:
                print 'break'
                break


class PocThread():

    threads = ANY_THREAD.POC_EXEC
    func = None
    targets_queue = None

    def __init__(self,threads = ANY_THREAD.POC_EXEC,func=None,queue=None):
        self.threads = threads
        self.func = func
        self.targets_queue = queue

    def start(self):
        for i in range(0,self.threads):
            print "正在创建第[%s]个线程" % str(i)
            if self.targets_queue.qsize() > 0:
                poc_t = __PocThread__(self.func,self.targets_queue)
                poc_t.start()
            else:
                break