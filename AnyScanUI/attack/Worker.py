# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * 暴力破解函数体
 *
 * @author margin 2017/02/20.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/02/20 margin 创建.
 *
 """
import paramiko
from ftplib import FTP

def sshWorker(host,username,password):
    """
    ssh连接
    :param host:
    :param username:
    :param password:
    :return:
    """
    ssh=paramiko.SSHClient()
    try:
        #print "正在破解SSH【%s】【%s】【%s】" % (host,username,password)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host,username=username,password=password,timeout=1)
        return True
    except:
        #print traceback.format_exc()
        # 有时候会爆session问题，登陆成功但没有获取session的情况，没有仔细研究过
        return False
    finally:
        ssh.close()

def ftpWorker(host,username,password,port=21):
    """
    ftp连接
    :param host:
    :param username:
    :param password:
    :return:
    """
    ftp = FTP(host)
    try:
        print "正在破解FTP【%s】【%s】【%s】" % (host,username,password)
        ftp.connect(host,port)  #连接 服务器名  端口号
        ftp.login(username,password)
        print "FTP破解成功"
        return True
    except:
        #print traceback.format_exc()
        # 有时候会爆session问题，登陆成功但没有获取session的情况，没有仔细研究过
        return False
    finally:
        ftp.quit()