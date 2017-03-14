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
from AnyScanUI.models import poc_urls
from AnyScanUI.util import currenttime

class BaiduSpider():

    def __init__(self,commond="",count=1000,tn="json",threads=10):
        self.commond = commond
        #rn——一页显示多少条，最大50
        self.rn = 10
        #pn——   pn = rn * (当前页数)   页数从0开始为第一页
        self.pn = 0
        self.tn = tn
        self.threads = threads
        self.id = str(uuid.uuid1())
        # 计算所有要查询的http请求次数
        self.pn_queue = Queue.Queue(maxsize = count / self.rn)
        # 保存搜集到的url
        self.targets_queue = Queue.Queue(maxsize = count)
        for i in range(0,count / self.rn):
            self.pn_queue.put(i*self.rn)
            print i*self.rn
        # 初始化数据库记录
        poc_urls.objects.create(id=self.id,start_time=currenttime(),status="running",commond=self.commond,threads=self.threads,counts=0,
                                log="【%s】正在采集【%s】相关网站" % (str(0),self.commond))

    def target(self):
        pn = self.pn_queue.get()
        host = "http://www.baidu.com/s?wd=%s&pn=%s&rn=%s&tn=%s&ie=utf-8" % (self.commond,pn,self.rn,self.tn)
        print host
        return host

    def exploit(self):
        while True:
            if self.pn_queue.empty() == False:
                try:
                    reload(sys)
                    sys.setdefaultencoding("utf-8")
                    response=requests.get(self.target(),verify=True,timeout=10)
                    content = ""
                    try:
                        if response.content is None:continue
                        content = json.loads(response.content)
                    except:
                        print content
                        continue
                    response.close()
                    entry = content.get("feed").get("entry")
                    for en in entry:
                        __title = en.get("title")
                        __url = en.get("url")
                        __pn = en.get("pn")
                        __id = str(uuid.uuid1())
                        if __url is not None:
                            __e = {"id":__id,"name":__title,"url":__url,"pn":__pn,"children":[{"name":__url}]}
                            self.targets_queue.put(__e)
                            # 先将数据取出来，定义一次，以防止其他线程干扰
                            __tmp_queue = self.targets_queue
                            __targets__ = self.format(repeat(list(__tmp_queue.queue)))
                            __len__ = __tmp_queue.qsize()
                            poc_urls.objects.filter(id=self.id,locker="false").update(end_time=currenttime(),counts=__len__,
                                log="【%s】正在采集【%s】相关网站" % (str(__len__),self.commond),urls=json.dumps(__targets__))

                except Exception as e:
                    poc_urls.objects.filter(id=self.id,locker="false").update(end_time=currenttime(),status="success",log="采集【%s】相关网站异常" % (self.commond))
                    print traceback.format_exc()
                    print('获取百度内容失败，原因：%s' % e)
                    return None
            else:
                poc_urls.objects.filter(id=self.id,locker="false").update(end_time=currenttime(),status="success",locker="true",
                                log="采集完成【%s】相关网站" % (self.commond))
                break
    def format(self,targets):
        """
        格式化返回到前台的格式
        :param targets:
        :return:
        """
        return [{"name":"去重结果共[%s]条记录" % len(targets),"open":True,"children":targets}]

    def start(self):
        for t in range(0,5):
            if self.pn_queue.empty():
                break
            tt = threading.Thread(target=self.exploit,args=())
            tt.start()
            print "启动线程【%s】" % str(t)
        # 去重
        new = repeat(list(self.targets_queue.queue))
        return self.format(new),self.id

if __name__ == '__main__':
    b = BaiduSpider(commond="inurl:*.edu.cn inurl:*.do ",count=1000)
    r=b.start()
    print r
    print "去重后长度" + str(len(r))
