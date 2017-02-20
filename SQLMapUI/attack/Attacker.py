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

class Attacker():
    """
    攻击调度类
    """
    attackObject = AttackObject()
    def __init__(self,attackObject):
        self.attackObject = attackObject

    def attack(self,attack_data):
        """
        attack_data的数据格式为前台传递的格式
        :param attack_data: {"ip":[80,3306],"ip2":[22]}
        :return:
        """
        for ip,ports in attack_data.items():
            self.attackObject.ip = ip
            if ports:
                for port in ports:
                    if port == "22" or port == 22:
                        sshAttacker = SSHAttack(self.attackObject)
                        sshAttacker.attack()


if __name__ == "__main__":
    attackObject = AttackObject()
    attackObject.threads = 5
    attackObject.timeout = 32
    attackObject.usernames = "username.txt"
    attackObject.passwords = "password.txt"

    attacker = Attacker(attackObject)
    attacker.attack({"192.168.1.223":[80,3306],"192.168.1.222":[22]})