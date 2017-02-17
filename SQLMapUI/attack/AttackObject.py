# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * 攻击参数，定义了攻击动作所需要的属性
 *
 * @author margin 2017/02/16.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/02/16 margin 创建.
 *
 """

class AttackObject(object):
    # 用户名字典
    usernames = ""
    # 密码字典
    passwords = ""
    # 攻击线程
    threads = 1
    # 超时时间
    timeout = 10

    def __init__(self,threads=1,timeout=10):
        self.threads = threads
        self.timeout = timeout

    def getUserNames(self):
        """
        获取用户名字典
        :return:
        """
        return self.usernames

    def getPasswords(self):
        """
        获取密码字典
        :return:
        """
        return  self.passwords

    def getThreads(self):
        """
        获取攻击线程
        :return:
        """
        return self.threads

    def getTimeout(self):
        """
        获取超时时间
        :return:
        """
        return self.timeout