# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * AnyPoc
 *
 * @author margin 2017/03/22.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/03/22 margin 创建.
 *
 """
from AnyScanUI.AnyPoc.lib.util.util import cms
from AnyScanUI.util.constant import ANY_THREAD

class AnyPoc():
    cms_scanner_threads = ANY_THREAD.CMS_SCANNER
    epoc_threads = ANY_THREAD.POC_EXEC
    target = None
    result = {'status':False,'msg':''}
    def __init__(self,cms_scanner_threads = ANY_THREAD.CMS_SCANNER,epoc_threads = ANY_THREAD.POC_EXEC,target = "http://www.baidu.com"):
        self.cms_scanner_threads = cms_scanner_threads
        self.epoc_threads = epoc_threads
        self.target = target

    def exploit(self):
        # CMS识别,cms_info的结构和上面的result相同
        cms_info = cms(self.target,self.cms_scanner_threads)
        if cms_info.get('status') is False:
            return cms_info

        # 调用POC进行攻击

