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

import Queue

class AttackObject(object):
    # 用户名字典
    ssh_usernames = "/Users/margin/PycharmProjects/AnyScan/AnyScanUI/attack/ssh_username.txt"
    # 密码字典
    ssh_passwords = "/Users/margin/PycharmProjects/AnyScan/AnyScanUI/attack/ssh_password.txt"
    # ftp用户名字典
    ftp_usernames = "/Users/margin/PycharmProjects/AnyScan/AnyScanUI/attack/ftp_username.txt"
    # ftp密码字典
    ftp_passwords = "/Users/margin/PycharmProjects/AnyScan/AnyScanUI/attack/ftp_password.txt"
    # mysql用户名字典
    mysql_usernames = "/Users/margin/PycharmProjects/AnyScan/AnyScanUI/attack/mysql_username.txt"
    # mysql密码字典
    mysql_passwords = "/Users/margin/PycharmProjects/AnyScan/AnyScanUI/attack/mysql_password.txt"
    # 攻击线程
    threads = 1
    # 总线程数，所有任务从这里申请
    queue_thread_size = 100
    # 超时时间
    timeout = 10
    # ip
    ip = ""
    # 端口
    port = "22"
    # 总线程数，由queue来控制总线程数
    threads_queue = Queue.Queue(maxsize = 10)

    # 破解队列queue的字典集合,{"ip+port":queue}
    attack_queue_dict = {}
    # 破解队列对应的字典原始长度,{"ip+port":queue.qsize}
    attack_queue_size_dict = {}

    # 当前爆破任务id
    id = ""
    # 当前爆破任务的pid
    pid = ""
    # 爆破日志
    log = ""

    # 数据锁，当为True时不可更新数据库内容{"ip+port":True}
    locker = {}

    # 攻击的类型，是重启还是新建，还是暂停后又启动  create restart start
    type = "create"

    def __init__(self,threads=1,timeout=10):
        super(AttackObject, self).__init__()
        self.threads_queue = Queue.Queue(maxsize = self.queue_thread_size)
        for i in range(0,self.queue_thread_size):
            self.threads_queue.put("")
        self.timeout = timeout
        # 初始化locker
        locker = {}

    def setThreads(self,threads):
        self.threads = threads
        self.threads_queue = Queue.Queue(maxsize = self.queue_thread_size)
        for i in range(0,self.queue_thread_size):
            self.threads_queue.put("")

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
        return self.passwords

    def getThreads(self):
        """
        获取攻击线程
        :return:
        """
        # 字符串转化int
        try:
            self.threads = int(self.threads)
            if self.threads == 0 or self.threads == "":
                self.threads = 10
            if self.threads > 100:
                self.threads = 100
        except:
            self.threads = 10

        return self.threads

    def getTimeout(self):
        """
        获取超时时间
        :return:
        """
        return self.timeout

    def getIp(self):
        """
        获取ip
        :return:
        """
        return self.ip

    def getPort(self):
        """
        获取port
        :return:
        """
        return self.port

    def getAttack_queue(self):
        """
        获取port
        :return:
        """
        return self.attack_queue

    def getId(self):
        """
        获取port
        :return:
        """
        return self.id

    def getAttack_queue_size(self):
        """
        获取队列最初的长度
        :return:
        """
        return self.attack_queue_size

    def getAttack_queue_current_size(self):
        """
        获取队列当前的长度
        :return:
        """
        return self.attack_queue.qsize()

    def getLog(self,data):
        """
        获取爆破进度log
        :param data:
        :return:
        """
        log = "【%s:%s】【%s爆破】进度【%s】，当前用户名:%s，密码:%s" % data
        return log

    def getSuccessLog(self,data):
        """
        获取爆破成功log
        :param data:
        :return:
        """
        log = "【%s:%s】【%s爆破成功】当前用户名:%s，密码:%s" % data
        return log

    def getFinishLog(self,data):
        """
        获取爆破成功log
        :param data:
        :return:
        """
        log = "【%s:%s】【爆破完成】" % data
        return log

    def getAttack_queue_dict(self,key):
        """
        获取爆破队列字典对应的queue
        :param key:
        :return:
        """
        return self.attack_queue_dict.get(key)

    def getAttack_queue_size_dict(self,key):
        """
        获取攻击字典的原始长度
        :param key:
        :return:
        """
        size = self.attack_queue_size_dict.get(key)
        if size:
            return size
        else:
            return 0

    def getThreads_queue(self):
        """
        获取当前空余线程队列个数
        :return:
        """
        return self.threads_queue

    def getPid(self):
        """
        获取pid
        :return:
        """
        return self.getPid()

    def getLocker_dict(self,key):
        """

        :param key:
        :return:
        """
        return self.locker.get(key)

    def getType(self):
        """
        获取攻击任务类型
        :return:
        """
        return self.type