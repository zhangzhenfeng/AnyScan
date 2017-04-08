# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * poc调度核心
 *
 * @author margin 2017/03/22.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/03/22 margin 创建.
 *
 """

from AnyScanUI.util.constant import ANY_THREAD,BUG_SCAN
from AnyScanUI.AnyPoc.lib.core.bug_scan import BugScan
import uuid
from AnyScanUI.util.util import currenttime
from AnyScanUI.models import cms_poc_main

class poc_core():
    __cms__ = None
    __threads__ = ANY_THREAD.POC_EXEC
    __target__ = None

    def __init__(self,target,cms = '',threads = ANY_THREAD.POC_EXEC):
        self.__cms__ = cms
        self.__threads__ = threads
        self.__target__ = target

    def exploit(self):
        # 生成主任务的id
        pid = str(uuid.uuid1())
        # 检测
        # 暂时直接执行poc，cms识别暂时不做
        bugscan = BugScan(self.__target__,pypath=BUG_SCAN.BUGSCAN_PATH,threads=self.__threads__,pid=pid)
        poc_size = bugscan.target_queue.qsize()
        # 初始化数据
        self.init_scan(pid,bugscan,poc_size)
        log = bugscan.exploit()

    def init_scan(self,id,bugscan,poc_size):
        # 起始时间
        start_time  = currenttime()
        # 目标地址
        target = self.__target__
        # 线程数
        threads = self.__threads__
        # 状态
        status = "running"
        cms_poc_main.objects.create(id=id,start_time=start_time,status="running",target=target,threads=threads,progress="0.00",poc_size=poc_size)

if __name__ == '__main__':
    poc = poc_core()
    poc.exploit()