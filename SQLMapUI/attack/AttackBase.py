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
class AttackBase(object):
    # 攻击状态
    # running
    # stoped
    #
    state = ""
    # 攻击属性
    attackOjbect = AttackObject()

    def __init__(self,attackObject):
        self.attackOjbect = attackObject

    def getState(self):
        """
        获取攻击状态
        :return: 攻击状态
        """
        return self.state

    def attack(self):
        print "attacking"
        print self.attackOjbect.getTimeout()
        print self.attackOjbect.getThreads()
