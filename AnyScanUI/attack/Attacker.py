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
from SSHAttack import SSHAttack
import sys,threading,copy,uuid,traceback,time
from AnyScanUI.models import PortCrackChild,PortCrack
from AnyScanUI.util import currenttime

class Attacker():
    """
    攻击调度类
    """
    attackObject = AttackObject()
    def __init__(self,attackObject):
        self.attackObject = attackObject
        reload(sys)
        sys.setdefaultencoding('utf8')

    def attack(self,attack_data):
        """
        attack_data的数据格式为前台传递的格式
        :param attack_data: {"ip":[80,3306],"ip2":[22]}
        :return:
        """
        if self.attackObject.type == "create":
            # 任务类型为新建任务
            for ip,ports in attack_data.items():
                self.attackObject.ip = ip
                if ports:
                    for port in ports:
                        if port == "22" or port == 22:
                            id = str(uuid.uuid1())
                            if self.create_task(id,self.attackObject.pid,"SSH",ip,port) is False:
                                return False
                            # 设置该任务的任务id
                            sshAttacker = SSHAttack(self.attackObject)
                            t = threading.Thread(target=sshAttacker.attack,args=({"ip":ip,"port":port,"id":id},))
                            t.start()
        elif self.attackObject.type == "start":
            # 任务启动类型为：暂停-->启动
            pass
        # 单独启动线程更新任务总状态
        t = threading.Thread(target=self.update_task,args=(self.attackObject.pid,))
        t.start()
        return True

    def create_task(self,id,pid,type,ip,port):
        """
        创建爆破子任务
        :param pid:
        :return:
        """
        try:
            portcrack = PortCrack()
            portcrack.id = pid
            PortCrackChild.objects.create(id=id,ip=ip,port=port,pid=portcrack,start_time=currenttime(),status="running",type=type,progress="0.00")
            return True
        except:
            print traceback.format_exc()
            return False

    def update_task(self,pid):
        """
        更新总任务状态
        :param pid:
        :return:
        """
        while True:
            #print "正在执行"
            portcrack = PortCrack.objects.get(id=pid)
            child_set = portcrack.portcrackchild_set.all()
            # 所有任务长度
            all_length = len(child_set)

            # 未完成任务
            not_success = child_set.filter(status="running")
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
                if child.status == "success":
                    portcrack_success.append({"ip":child.ip.encode("utf-8"),"port":child.port.encode("utf-8"),"username":child.username.encode("utf-8"),"password":child.password.encode("utf-8")})
            # 计算总任务进度
            progress = now_progress/(all_length)

            # 当所有的任务都不为running时说明都爆破完成了，无论是成功还是失败。
            if success_num == all_length:
                PortCrack.objects.filter(id=pid).update(end_time=currenttime(),status="success",result=str(portcrack_success),progress="100",log="爆破结束，结果请看详情\n" + log)
                return
            else:
                PortCrack.objects.filter(id=pid).update(end_time=currenttime(),status="running",result=str(portcrack_success),progress=str(progress),log=log)

            # 没2秒轮询一次
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