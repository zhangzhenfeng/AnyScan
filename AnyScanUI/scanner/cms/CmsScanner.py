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

import Queue
import hashlib
import os
import threading
import traceback
import uuid

from AnyScanUI.models import CmsInfo
from AnyScanUI.util.util import currenttime
from AnyScanUI.util.Http import Http


class CmsScanner():

    def __init__(self,host,threads):
        self.threads = threads
        self.host = host
        self.id = ""
        self.cms_queue_oldsize = 0
        self.cms = False
        # 初始化字典
        cms_info_file = open(os.getcwd()+"/AnyScanUI/scanner/cms/"+'cms_info.json')
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

    def get_md5_value(self,content):
        """
        获取md5值
        :param content: 要md5的值
        :return:
        """
        md5 = hashlib.md5()
        md5.update(content)
        md5_Digest = md5.hexdigest()
        return md5_Digest

    def save(self,exp_info,keyword,cms_name,version):
        """
        保存检测成功感的日志
        :param exp_info:
        :param keyword:
        :param cms_name:
        :param version:
        :return:
        """
        self.cms = True
        log = "【%s】检测成功，Payload为【%s】，CMS为【%s】,版本信息【%s】" % (self.host,exp_info.get("url"),cms_name,version)
        CmsInfo.objects.filter(id=self.id,locker="false").update(end_time=currenttime(),status="success",progress="100",log=str(log),locker="true",cms=cms_name,version=version,keyword=keyword,payload=exp_info.get("url"))
        self.cms_queue.queue.clear()

    def exploit(self):

        while True:
            if self.cms_queue.empty() is False:

                obj = CmsInfo.objects.get(id=self.id)
                if obj is None or obj.status == "stop":
                    #print "任务【%s】被删除" % self.id
                    break

                exp_info = eval(str(self.cms_queue.get()))
                # 不要忘记请求图片类型，无法获取content
                cms_name = exp_info.get("cms")
                version = exp_info.get("version")
                keyword = exp_info.get("keyword")
                cms_md5 = exp_info.get("md5")
                url = self.host + exp_info.get("url")
                http = Http('http', self.host, "")
                html_content,code = http.post_(url)

                # 计算进度
                progress = 1-float(format(float(self.cms_queue.qsize())/float(self.cms_queue_oldsize),'.4f'))
                progress = '%.2f' % (progress * 100)

                # 实时日志
                log = "【%s】正在测试【%s】" % (str(progress)+"%",str(url))
                #print log
                CmsInfo.objects.filter(id=self.id,locker="false").update(end_time=currenttime(),status="running",progress=progress,log=str(log))

                # 如果有关键字，就用关键字比较
                if code == 200:
                    md5 = self.get_md5_value(html_content)
                    if cms_md5 == "" or cms_md5 is None:
                        # 当md5为空时，比较关键字
                        if keyword in html_content:
                            self.save(exp_info,keyword,cms_name,version)
                            break
                    if md5 == cms_md5:
                        self.save(exp_info,md5,cms_name,version)
                        break

            else:
                CmsInfo.objects.filter(id=self.id,locker="false").update(end_time=currenttime(),status="success",progress="100",log="【%s】检测完成" % self.host,locker="true")
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
            tt = threading.Thread(target=self.exploit,args=())
            tt.start()
            print "启动线程【%s】" % str(t)
        return self.id



if __name__ == "__main__":
    s = CmsScanner("http://192.168.1.105/wordpress-4.7.1/",2)
    s.start()

