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
import Queue

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

    def attack_queue(self):
        """
        获取
        :return:
        """
        result = {"status":True,"msg":"成功","data":[]}
        username_file = self.attackObject.getUserNames()
        password_file = self.attackObject.getPasswords()

        usernames = []
        passwords = []
        print username_file
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
                attack_queue.task_done()
        result["data"] = attack_queue
        return result