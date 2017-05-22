#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'boy'
def assign(service, arg):
    if service == "php168":
        return True, arg
def audit(arg):
    code, head, res, errcode,finalurl = curl.curl('%snews/js.php?type=hot&f_id=23)' % arg)
    m = res.find("SELECT")
    if m!=-1:
        security_info('find sql injection:%snews/js.php?type=hot&f_id=23)'% arg)

        return arg
if __name__== '__main__':
    from dummy import *
