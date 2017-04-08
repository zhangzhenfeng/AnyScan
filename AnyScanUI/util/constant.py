# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * 常量类
 *
 * @author margin 2017/03/22.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/03/22 margin 创建.
 *
 """

from util import current_path
import os

PROJECT_PATH = "/Users/margin/PycharmProjects/AnyScan/AnyScanUI/"
MODEL_NAME = "AnyPoc"

class ANY_THREAD():
    PORT_ATTACK = 20
    CMS_SCANNER = 20
    POC_EXEC    = 20

class BUG_SCAN():
    BASE_PATH = os.path.join(PROJECT_PATH,MODEL_NAME)
    BUGSCAN_PATH = os.path.join(BASE_PATH,"data","poc","bugscan")
    BUG_SCAN_POC_RESULT_API_URL = 'http://127.0.0.1:8000/AnyScanUI/bug_scan_poc_result_save'

class POC_PLUGINS_DIR():
    BASE_DIR = os.path.join(PROJECT_PATH,MODEL_NAME,"plugins")
    PLUGINS_DIR = os.path.join(BASE_DIR + 'plugins')

if __name__ == '__main__':
    #print e.BUGSCAN_PATH
    pass
