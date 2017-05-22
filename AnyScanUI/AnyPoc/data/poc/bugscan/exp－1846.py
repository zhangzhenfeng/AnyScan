#!/usr/bin/env python
# -*- coding: utf-8 -*-
#refer:http://www.wooyun.org/bugs/wooyun-2010-0123369

def assign(service, arg):
    if service == 'seentech_uccenter':
        return True, arg
        
def audit(arg):
    payload = "ucenter/include/globalvar_center.h"
    code,_,res,_,_ = curl.curl2(arg+payload)
    if code==200 and '$gMysql_host_name' in res :
        security_warning(arg+payload)


        return arg
if __name__== '__main__':
    from dummy import *
