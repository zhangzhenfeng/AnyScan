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

import json,Queue,threading,uuid,traceback,os
from AnyScanUI.Http import Http
from AnyScanUI.models import CmsInfo
from AnyScanUI.util import currenttime

class CmsScanner():

    def __init__(self,host,threads):
        self.threads = threads
        self.host = host
        self.id = ""
        self.cms_queue_oldsize = 0
        self.cms = False
        print os.getcwd()
        # 初始化字典
        cms_info_file = open(os.getcwd()+"/AnyScanUI/cms/"+'cms_info1.json')
        # cms信息Queue
        cms_queue = Queue.Queue(maxsize = 10)
        try:
            cms_info_str = cms_info_file.read()
            cms_info = eval(cms_info_str)
            self.cms_queue = Queue.Queue(maxsize = len(cms_info))
            self.cms_queue_oldsize = len(cms_info)
            for info in cms_info:
                self.cms_queue.put(info)
            id = str(uuid.uuid1())
            self.id = id
            # 初始化数据库数据
            CmsInfo.objects.create(id=id,start_time=currenttime(),status="running",host=self.host,threads=self.threads,progress="0.00")
        except:
            print traceback.format_exc()
        finally:
            cms_info_file.close()


    def exploit(self):
        host = self.host
        while True:
            if self.cms_queue.empty() is False:
                obj = CmsInfo.objects.get(id=self.id)
                if obj is None:
                    print "任务【%s】被删除" % self.id
                    break
                if obj.status == "stop":
                    print "任务【%s】被停止" % self.id
                    break
                exp_info = self.cms_queue.get()
                exp_info = eval(str(exp_info))
                # 不要忘记请求图片类型，无法获取content
                cms_name = exp_info.get("cms")
                version = exp_info.get("version")
                keyword = exp_info.get("keyword")
                url = host + exp_info.get("url")
                http = Http('http', host, "")
                html_content,redirect_url = http.post_(url)
                # 计算进度
                progress = 1-float(format(float(self.cms_queue.qsize())/float(self.cms_queue_oldsize),'.4f'))
                progress = '%.2f' % (progress * 100)

                # 实时日志
                log = "【%s】正在测试【%s】" % (str(progress)+"%",str(url))
                print log
                CmsInfo.objects.filter(id=self.id,locker="false").update(end_time=currenttime(),status="running",progress=progress,log=str(log))
                # 如果有关键字，就用关键字比较
                if keyword != "" and keyword is not None:
                    if html_content is None:
                        print "检测失败" + url
                        self.cms = False
                        continue
                    if keyword.upper() in html_content.upper():
                        self.cms = True
                        print "检测成功2" + url
                        log = "【%s】检测成功，Payload为【%s】，关键字【%s】，CMS为【%s】,版本信息【%s】" % (host,exp_info.get("url"),keyword,cms_name,version)
                        CmsInfo.objects.filter(id=self.id,locker="false").update(end_time=currenttime(),status="success",progress="100",log=str(log),locker="true",cms=cms_name,version=version,keyword=keyword,payload=exp_info.get("url"))
                        self.cms_queue.queue.clear()
                        break
                else:
                    # 当没有关键字，只能通过文件来判断是否存在时，需要检测重定向url是否为原来的url，如果不是说明文件不存在
                    if html_content is not None and redirect_url == url:
                        self.cms = True
                        print "检测成功3" + url
                        log = "【%s】检测成功，Payload为【%s】，关键字【%s】，CMS为【%s】,版本信息【%s】" % (host,exp_info.get("url"),keyword,cms_name,version)
                        CmsInfo.objects.filter(id=self.id,locker="false").update(end_time=currenttime(),status="success",progress="100",log=log,locker="true",cms=cms_name,version=version,payload=exp_info.get("url"))
                        self.cms_queue.queue.clear()
                        break
                    else:
                        self.cms = False
                        print "检测失败" + url
                        continue
            else:
                CmsInfo.objects.filter(id=self.id,locker="false").update(end_time=currenttime(),status="success",progress="100",log="【%s】检测完成" % host,locker="true")
                self.cms_queue.queue.clear()
                break

    def start(self):
        threads = self.threads
        host = self.host
        if threads > 100:
            threads = 100
        for t in range(0,threads):
            if self.cms_queue.empty():
                break
            t = threading.Thread(target=self.exploit,args=())
            t.start()
        return self.id



if __name__ == "__main__":
    s = CmsScanner("http://192.168.1.105/wordpress-4.7.1/",2)
    s.start()

