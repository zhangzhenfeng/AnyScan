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
import uuid,traceback
from AnyScanUI.util.util import currenttime
from AnyScanUI.models import cms_poc_main,cms_poc_chil
from django.db.models import Q

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
        return [pid]

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

    def stop(self,id_list):
        """

        :param id_list:
        :return:
        """
        try:
            log = "任务被手动停止"
            for id in id_list:
                cms_poc_main.objects.filter(~Q(status="stop"), ~Q(status="success"), id=id, locker="false").update(end_time=currenttime(),log=log,status="stop",locker="true")
            return True, "停止成功"
        except:
            print traceback.print_exc()
            return False, traceback.print_exc()

    def log(self,id_list):
        """

        :param id_list:
        :return:
        """
        try:
            info = ""
            status = "stop"
            for id in id_list:
                obj = cms_poc_main.objects.get(id=id)
                __log = obj.log.encode("utf-8")
                info = info + __log + "\n"
                if obj.status == "running":
                    status = obj.status
            return True,status,info
        except:
            print traceback.print_exc()
            return False,"stop",str(traceback.print_exc())

    def vuln(self,id_list):
        try:
            info = ""
            __obj__ = cms_poc_chil.objects.filter(pid__in=id_list)
            obj = __obj__.all()
            for o in obj:
                info = info + o.log.encode("utf-8") + "\n"
            return info

        except:
            print traceback.print_exc()
            return str(traceback.print_exc())

if __name__ == '__main__':
    poc = poc_core()
    poc.exploit()