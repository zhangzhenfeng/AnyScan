#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__ = '1c3z'

import re
    

def fetch(url,raw):
    card15 = r"\b([1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3})\b"
    card18 = r"\b([1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}([0-9]|X))\b"
    URL = r"\b(http://(\d{1,3}\.){3}\d{1,3}(:\d+)?)\b"
    mail = r"\b([a-zA-Z\-_1-9]+@([a-zA-Z\-_1-9]+\.){1,3}(com|cn|net|org))\b"
    phone = r"\b((13|14|15|17|18)\d{9})\b"

    regexs = [card15,card18,mail,phone,URL]

    for r in regexs:
        rst = re.findall(r, raw)
        for i in rst:
            security_note(i[0])

def audit(url, head, body):
    fetch(url, body)


if __name__ == '__main__':
    # import local simulation environment
    from dummy import *
    body = """
    13050367040103446 36 01533366346
    13888888888 fgdfsffesse
    13888888887 fsdfffdsf 132435345757567545345535355
34354334 3543   37100119801082394 sfsdfd <>shuishalr
    450803197404237599 asf
fsfdfasfsdf
    nxhr@zwcad.com asfsdfdsf
    nxhr@xx.zwcad.com sadfsdfd
    >http://1.1.1.1:888 asfsdf
    >http://1.1.1.1:888 aedsf
    >http://1.1.122.1
    """
    audit("http://test.test","header",body)