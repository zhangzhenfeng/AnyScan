#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,sys
import os,sys
import urllib2

class Http:
    '''配置要测试请求服务器的ip、端口、域名等信息，封装http请求方法，http头设置'''

    def __init__(self, protocol, host, port, header = {}):
       # 从配置文件中读取接口服务器IP、域名，端口
        self.protocol = protocol
        self.host = host
        self.port = port
        self.headers = header  # http 头

    def set_host(self, host):
        self.host = host

    def get_host(self):
        return self.host

    def get_protocol(self):
        return self.protocol

    def set_port(self, port):
        self.port = port

    def get_port(self):
        return  self.port

    # 设置http头
    def set_header(self, headers):
        self.headers = headers

    # 封装HTTP GET请求方法
    def get(self, url, params=''):
        print url
        url = self.protocol + '://' + self.host + ':' + str(self.port)  + url + params

        print(u'发起的请求为：%s' % url)
        request = urllib2.Request(url, headers=self.headers)
        try:
            response = urllib2.urlopen(request)
            response = response.read()
            return response
        except Exception as e:
            print('发送请求失败，原因：%s' % e)
            return None

    # 封装HTTP POST请求方法
    def post(self, url, data=''):
        url = self.protocol + '://' + self.host + ':' + str(self.port)  + url
        print url
        print(u'发起的请求为：%s' % url)
        if data=='':
            data={}
        req=urllib2.Request(url,data,{'Content-Type': 'application/json'})
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36')
        try:
            f=urllib2.urlopen(req)
            return f.read()
        except Exception as e:
            print(u'发送请求失败，原因：%s' % e)
            return None