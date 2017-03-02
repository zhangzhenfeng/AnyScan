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
        print "正在破解【%s】【%s】【%s】" % (host,username,password)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host,username=username,password=password,timeout=0.5)
        return True
    except:
        #print traceback.format_exc()
        # 有时候会爆session问题，登陆成功但没有获取session的情况，没有仔细研究过
        return False
    finally:
        ssh.close()