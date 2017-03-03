# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * 攻击的调度类
 *
 * @author margin 2017/02/20.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/02/20 margin 创建.
 *
 """
from AttackObject import AttackObject
from django.db.models import Q
from Attack import Attack
import sys,threading,copy,uuid,traceback,time
from AnyScanUI.models import PortCrackChild,PortCrack
from AnyScanUI.util import currenttime
from Worker import sshWorker,ftpWorker

class Attacker():
    """
    攻击调度类
    """
    attackObject = None
    def __init__(self,attackObject):
        self.attackObject = attackObject
        reload(sys)
        sys.setdefaultencoding('utf8')

    def attack(self,attack_data,attack_task_id_dict = {},):
        """
        attack_data的数据格式为前台传递的格式
        :param attack_data: {"ip":[80,3306],"ip2":[22]}
        :return:
        """

        # 任务类型为新建任务
        for ip,ports in attack_data.items():
            self.attackObject.ip = ip
            if ports:
                for port in ports:
                    if port == "22" or port == 22:
                        id = str(uuid.uuid1())
                        __create_status,id = self.create_task(id,self.attackObject.pid,"SSH",self.attackObject.type,ip,port,attack_task_id_dict)
                        if __create_status is False:
                            return False
                        # 设置该任务的任务id
                        sshAttacker = Attack(self.attackObject)
                        t = threading.Thread(target=sshAttacker.attack,args=({"ip":ip,"port":port,"id":id,"locker":{},"callback":sshWorker,"attack_type":"SSH"},))
                        t.start()
                    elif port == "21" or port == 21:
                        id = str(uuid.uuid1())
                        __create_status,id = self.create_task(id,self.attackObject.pid,"FTP",self.attackObject.type,ip,port,attack_task_id_dict)
                        if __create_status is False:
                            return False
                        # 设置该任务的任务id
                        ftpAttacker = Attack(self.attackObject)
                        t = threading.Thread(target=ftpAttacker.attack,args=({"ip":ip,"port":port,"id":id,"locker":{},"callback":ftpWorker,"attack_type":"FTP"},))
                        t.start()
        # 单独启动线程更新任务总状态
        t = threading.Thread(target=self.update_task,args=(self.attackObject.pid,))
        t.start()
        return True

    def create_task(self,id,pid,type,task_type,ip,port,attack_task_id_dict):
        """
        创建爆破子任务
        :param pid:
        :return:
        """
        try:
            portcrack = PortCrack()
            portcrack.id = pid
            if task_type == "create":
                PortCrackChild.objects.create(id=id,ip=ip,port=port,pid=portcrack,start_time=currenttime(),status="running",type=type,progress="0.00")
                return True,id
            elif task_type == "start":
                # 获取暂停任务的id
                id = attack_task_id_dict[ip+port]
                PortCrackChild.objects.filter(id=id,status="pause").update(pid=portcrack,status="running",end_time=currenttime())
                return True,id

        except:
            print traceback.format_exc()
            return False,id

    def update_task(self,pid):
        """
        更新总任务状态
        :param pid:
        :return:
        """
        while True:
            #print "正在执行"
            portcrack = None
            try:
                portcrack = PortCrack.objects.get(id=pid)
            except:
                print "任务id【%s】不存在了" % pid
                return
            if portcrack.status == "pause":
                return
            child_set = portcrack.portcrackchild_set.all()
            # 所有任务长度
            all_length = len(child_set)

            # 未完成任务
            not_success = child_set.filter(Q(status="running") | Q(status="pause"))
            # 已完成任务个数
            success_num = all_length - len(not_success)

            now_progress = 0
            log = ""
            # 在总进度中统计爆破成功的用户名密码[{"ip":"","port":"","username":"","password":""}]
            portcrack_success = []
            # 统计总任务进度
            for child in child_set:
                progress_ = self.formatnum(child.progress)
                now_progress = now_progress + progress_

                # 统计日志
                log = log + str(child.log) + "\n"
                #print child.username != ""
                #print child
                if child.status == "success" and child.progress == "100":
                    portcrack_success.append({"ip":child.ip.encode("utf-8"),"port":child.port.encode("utf-8"),"username":child.username.encode("utf-8"),"password":child.password.encode("utf-8")})
            # 计算总任务进度
            progress = now_progress/(all_length)

            # 当所有的任务都不为running时说明都爆破完成了，无论是成功还是失败。
            if success_num == all_length:
                PortCrack.objects.filter(id=pid).update(end_time=currenttime(),status="success",result=str(portcrack_success),progress="100",log="爆破结束，结果请看详情\n" + log)
                return
            else:
                PortCrack.objects.filter(id=pid).update(end_time=currenttime(),result=str(portcrack_success),progress=str(progress),log=log)

            # 每2秒轮询一次
            time.sleep(2)

    def formatnum(self,str):
        try:
            str = str.encode("utf-8")
            if str == "" or str == None:
                return 0
            str = str.replace("%","")
            str = float(str)
            return str
        except:
            print traceback.format_exc()
            return 0


if __name__ == "__main__":

    attacker = Attacker()
    attacker.update_task("bafbc9b0-f99a-11e6-8a5b-784f435e6bbf")