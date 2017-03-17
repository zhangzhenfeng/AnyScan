# -*- coding:utf-8 -*-
import urllib2,re
import sys,Queue,threading,traceback
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

url_file = open('url1.txt')
url_str = url_file.read()
url_file.close()
url_list = url_str.split("\n")
print len(url_list)
check_list = []
result = []
check = "((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})?"
for info in url_list:
    try:
        u = re.match(check, info, flags=0).group()
        if u not in check_list:
            print u
            result.append(u)
            check_list.append(u)
    except:
        pass

url_file = open('url_result_host.txt','wb+')
for r in result:
    url_file.write(r+"\n")
url_file.close()