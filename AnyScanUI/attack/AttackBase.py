# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * 攻击基类，里面封装了攻击属性和攻击方法
 *
 * @author margin 2017/02/16.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/02/16 margin 创建.
 *
 """
from AttackObject import AttackObject
from AnyScanUI.models import PortCrackChild,PortCrack
import Queue,json

class AttackBase(object):
    # 攻击状态
    # running
    # stoped
    #
    state = ""
    # 攻击属性
    attackObject = AttackObject()

    def __init__(self,attackObject):
        self.attackObject = attackObject

    def getState(self):
        """
        获取攻击状态
        :return: 攻击状态
        """
        return self.state

    def attack(self):
        """
        攻击方法，所有的暴力破解都要重写该方法
        :return:
        """
        pass

    def attack_queue(self,id,attack_type):
        """
        获取
        :return:
        """
        result = {"status":True,"msg":"成功","data":[],"old_queue_size":0,"threads":0}
        if self.attackObject.type == "create":
            # 用户名
            usernames = []
            # 密码
            passwords = []
            # 攻击类型
            if attack_type == "SSH":
                username_file = self.attackObject.ssh_usernames
                password_file = self.attackObject.ssh_passwords
            elif attack_type == "FTP":
                username_file = self.attackObject.ftp_usernames
                password_file = self.attackObject.ftp_passwords
            elif attack_type == "MySQL":
                username_file = self.attackObject.mysql_usernames
                password_file = self.attackObject.mysql_passwords

            # 获取字典文件内容
            usernameObj = open(username_file)
            try:
                 u = usernameObj.read()
                 usernames = u.split("\n")
            except Exception:
                result = {"status":False,"msg":"读取用户名文件失败","data":[]}
                return result
            finally:
                usernameObj.close()

            # 获取字典文件内容
            passwordObj = open(password_file)
            try:
                 p = passwordObj.read()
                 passwords = p.split("\n")
            except Exception:
                result = {"status":False,"msg":"读取密码文件失败","data":[]}
                return result
            finally:
                passwordObj.close()
            attack_queue = Queue.Queue(maxsize = len(usernames) * len(passwords))
            for username_ in usernames:
                for password_ in passwords:
                    dict_ = [username_,password_]
                    attack_queue.put(dict_)
            result["old_queue_size"] = attack_queue.qsize()
            result["threads"] = self.attackObject.getThreads()
            result["data"] = attack_queue
        elif self.attackObject.type == "start":
            # 获取当前攻击的数据库对象，从中获取，线程数threads ,未进行爆破的字典attack_queue_list 任务创建时字典的长度：old_queue_size
            portcrackchild = PortCrackChild.objects.get(id=id)
            result["threads"] = int(portcrackchild.threads)
            result["old_queue_size"] = int(portcrackchild.old_queue_size)

            attack_queue_list = json.loads(portcrackchild.attack_queue_list)
            attack_queue = Queue.Queue(maxsize = len(attack_queue_list))

            # 数据格式[[username,password],[]]
            for dict_ in attack_queue_list:
                attack_queue.put(dict_)
            result["data"] = attack_queue
        return result