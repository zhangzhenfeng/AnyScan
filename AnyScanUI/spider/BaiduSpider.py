# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * 百度搜索
 *
 * @author margin 2017/03/13.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/03/13 margin 创建.
 * https://www.baidu.com/s?wd=site:*.gov.cn inurl:*.dod&pn=0&rn=10&tn=html
 *
 """
import urllib2,traceback,random,requests,json,uuid,sys,Queue,threading
from AnyScanUI.util import repeat

class BaiduSpider():

    def __init__(self,commond="",count=1000,tn="json"):
        self.commond = commond
        #rn——一页显示多少条，最大50
        self.rn = 50
        #pn——   pn = rn * (当前页数)   页数从0开始为第一页
        self.pn = 0
        self.tn = tn
        self.targets = []
        # 计算所有要查询的http请求次数
        self.pn_queue = Queue.Queue(maxsize = count / self.rn)
        for i in range(0,count / self.rn):
            self.pn_queue.put(i*self.rn)
            print i*self.rn

    def target(self):
        pn = self.pn_queue.get()
        host = "http://www.baidu.com/s?wd=%s&pn=%s&rn=%s&tn=%s&ie=utf-8" % (self.commond,pn,self.rn,self.tn)
        return host

    def exploit(self):
        while True:

            if self.pn_queue.empty() == False:
                try:
                    reload(sys)
                    sys.setdefaultencoding("utf-8")
                    response=requests.get(self.target(),verify=True,timeout=10)
                    content = json.loads(response.content)
                    response.close()
                    entry = content.get("feed").get("entry")
                    for en in entry:
                        __title = en.get("title")
                        __url = en.get("url")
                        __pn = en.get("pn")
                        __id = str(uuid.uuid1())
                        if __url is not None:
                            __e = {"id":__id,"name":__title,"url":__url,"pn":__pn}
                            self.targets.append(__e)

                except Exception as e:
                    print traceback.format_exc()
                    print('获取百度内容失败，原因：%s' % e)
                    return None
            else:
                #print self.targets
                break

    def start(self):
        for t in range(0,20):
            if self.pn_queue.empty():
                break
            tt = threading.Thread(target=self.exploit,args=())
            tt.start()
            # 等所有的url采集完成
            tt.join()
            print "启动线程【%s】" % str(t)
        # 去重
        new = repeat(self.targets)
        return new

if __name__ == '__main__':
    b = BaiduSpider(commond="inurl:*.edu.cn inurl:*.do ",count=1000)
    r=b.start()
    print r
    print "去重后长度" + str(len(r))
