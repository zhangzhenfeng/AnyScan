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

class poc_core():
    __cms__ = None
    __threads__ = ANY_THREAD.POC_EXEC
    __target__ = None

    def __init__(self,target,cms = '',threads = ANY_THREAD.POC_EXEC):
        self.__cms__ = cms
        self.__threads__ = threads
        self.__target__ = target

    def exploit(self):
        # 暂时直接执行poc
        bugscan = BugScan(self.__target__,pypath=BUG_SCAN.BUGSCAN_PATH,threads = self.__threads__)
        log = bugscan.exploit()

if __name__ == '__main__':
    poc = poc_core()
    poc.exploit()