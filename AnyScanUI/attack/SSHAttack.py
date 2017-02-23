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
    def __init__(self,attackObject):
        super(SSHAttack, self).__init__(attackObject)
        self.attackObject = attackObject

    def attack(self,obj):
        """
        SSH爆破类
        """
        result = {"status":True,"msg":"正在破解"}
        try:

            # 获取线程数
            thread = self.attackObject.getThreads()
            ip_ = obj['ip']
            port_ = obj['port']
            # 生成字典对应的queue
            attack_queue_result = self.attack_queue()
            if attack_queue_result["status"]:
                # 将生成的queue加入到攻击属性的attack_queue_dict中
                self.attackObject.attack_queue_dict[ip_+port_] = attack_queue_result["data"]
                # 保留该queue的原始长度用于计算爆破进度
                self.attackObject.attack_queue_size_dict[ip_+port_] = attack_queue_result["data"].qsize()
            else:
                return attack_queue_result
            #print "单个线程 %s" % thread
            while True:
                print "当前线程数[%s]" % self.attackObject.threads_queue.qsize()
                if self.attackObject.threads_queue.qsize() >= thread:
                    # 使用攻击对象attactObject的线程数来控制是否要启动新的线程
                    for index in range(0,thread):
                        self.attackObject.threads_queue.get()
                        # 判断字典队列中是否还有值，如果没值了，就不用启动线程了
                        if self.attackObject.attack_queue_dict[ip_+port_].qsize() > 0:
                            attacker = Attacker(self.attackObject,{"ip":ip_,"port":port_})
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
    attackObject = AttackObject()
    self_ip_port = {}
    def __init__(self,attackObject,self_ip_port):
        #注意：一定要显式的调用父类的初始化函数。
        super(Attacker, self).__init__()
        self.attackObject = attackObject
        self.self_ip_port = self_ip_port

    def run(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        ip_ = self.self_ip_port["ip"]
        port_ = self.self_ip_port["port"]
        # 获取单个爆破线程
        thread = self.attackObject.getThreads()
        attack_queue = self.attackObject.getAttack_queue_dict(ip_+port_)
        print self.attackObject.getAttack_queue_dict(ip_+port_).qsize()
        while True:
            if self.attackObject.getAttack_queue_dict(ip_+port_).empty() is False:
                # 获取当前爆破字典queue
                up_ = self.attackObject.getAttack_queue_dict(ip_+port_).get()
                username_ = up_[0]
                password_ = up_[1]
                # 计算进度
                c_size = self.attackObject.getAttack_queue_dict(ip_+port_).qsize()
                o_size = self.attackObject.getAttack_queue_size_dict(ip_+port_)
                progress = 1-float(format(float(c_size)/float(o_size),'.4f'))
                progress = '%.2f%%' % (progress * 100)
                param = ("SSH",progress,username_,password_)
                # 读取log日志
                log = self.attackObject.getLog(param)
                #print "正在破解%s[%s:%s][%s:%s]" % (self.getName(),ip_,port_,username_,password_)
                # 更新日志数据
                PortCrack.objects.filter(id=self.attackObject.getId()).update(end_time=currenttime(),type="SSH",progress=str(progress),log=str(log))
                # 如果连接成功，说明用户名密码正确
                if self.connect(ip_,username_,password_):
                    # 清空队列
                    self.attackObject.getAttack_queue_dict(ip_+port_).queue.clear()
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
                    attack_result = json.dumps(attack_result)
                    PortCrack.objects.filter(id=self.attackObject.getId()).update(end_time=currenttime(),status="success",result=attack_result,log=self.attackObject.getSuccessLog(("SSH",username_,password_)))
                    #print "破解成功，填充线程队列 %s" % self.attackObject.threads_queue.qsize()
                    for i in range(0,thread):
                        self.attackObject.threads_queue.put("")
            else:
                # 如果字典队列空了，那么直接关掉跳出循环，结束线程。
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