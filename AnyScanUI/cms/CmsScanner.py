# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * CMS识别类
 *
 * @author margin 2017/03/06.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/03/06 margin 创建.
 *
 """

import json,Queue,threading
from AnyScanUI.Http import Http

class CmsScanner():

    def __init__(self):
        # 初始化字典
        cms_info_file = open('cms_info.json')
        # cms信息Queue
        cms_queue = Queue.Queue(maxsize = 10)
        try:
             cms_info_str = cms_info_file.read()
             #print cms_info_str
             cms_info = eval(cms_info_str)
             print cms_info
             self.cms_queue = Queue.Queue(maxsize = len(cms_info))
             for info in cms_info:
                 self.cms_queue.put(info)
        finally:
             cms_info_file.close()


    def exploit(self,host,port):
        exp_info = self.cms_queue.get()
        print exp_info
        # 不要忘记请求图片类型，无法获取content
        keyword = exp_info.get("keyword")
        url = exp_info.get("url")
        http = Http('http', host, port)
        html_content = http.post(url)
        print "正在检测[%s]" % url
        cms = False
        if html_content is not None and keyword.upper() in html_content.upper():
            print "检测成功" + exp_info.get("cms")
            cms = True
        return cms

    def start(self,threads = 5, host = "www.baidu.com",port = "80"):
        resulter = {"status":True,"msg":""}
        if threads > 100:
            threads = 100
        for t in range(0,threads):
            t = threading.Thread(target=self.exploit,args=(host,port))
            t.start()

if __name__ == "__main__":
    s = CmsScanner()
    s.start(2,"www.baidu.com")

