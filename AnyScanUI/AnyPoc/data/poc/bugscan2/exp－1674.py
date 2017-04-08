#!/usr/bin/env python
#coding=utf8
import re
import urlparse

'''
Only one function named 'audit', the function is automatically called during the spider crawling
    url     : the URL of current page
    head    : HTTP Response header
    body    : HTTP Body
'''
def audit(url, head, body):

    asmxs = re.findall(r'<script src="([^.]+.asmx)', body)
    arr = urlparse.urlparse(url)
    mainurl = '%s://%s' % (arr.scheme, arr.netloc)

    for asmx in asmxs:
        security_note(mainurl+asmx)


        return url
if __name__== '__main__':
    from dummy import *
