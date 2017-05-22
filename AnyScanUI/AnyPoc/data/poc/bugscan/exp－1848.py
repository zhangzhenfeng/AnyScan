#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer:http://www.wooyun.org/bugs/wooyun-2010-0123359

def assign(service, arg):
    if service == 'seentech_uccenter':
        return True, arg
        
def audit(arg):
    payload = "ucenter/include/getpasswd.php"
    code,_,res,_,_ = curl.curl2(arg+payload)
    if len(res)>0 and code ==200:
        security_warning(arg+payload)


        return arg
if __name__== '__main__':
    from dummy import *
