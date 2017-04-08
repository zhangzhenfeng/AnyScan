#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = LinE
#__refer__  = http://www.wooyun.org/bugs/wooyun-2010-0132543
'''
华创路由器源码泄露
'''
import urlparse
def assign(service, arg):
    if service == 'huachuang_router':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    posturl =  "login_check.php."
    target = arg + posturl
    code, head, res, errcode, _ = curl.curl2(target)
    if code == 200 and "<?php" in res:
        security_hole(arg)


        return arg
if __name__== '__main__':
    from dummy import *
