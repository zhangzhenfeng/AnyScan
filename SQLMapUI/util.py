# -*- coding: utf-8 -*-
import os,itertools,traceback,datetime
def combination_tampper(findPath = "/Users/margin/Desktop/me/white/sqlmap/sqlmap-master/tamper/"):
    # 默认两种组合进行组合排列
    '''
    #获取目录中指定的文件名
    '''
    fileNames = os.listdir(findPath)
    names = []
    combination = []
    for name in fileNames:
        if ".py" in name and name != "__init__.py":
            names.append(name.replace(".py",""))

    # 例如：'apostrophemask,apostrophenullencode', 'apostrophemask,appendnullbyte']
    return names

def read_file_content(path):
    """

    :param path:
    :return:
    """
    path = str(path)
    data = {"status":True,"data":""}
    if os.path.isfile(path) is False:
        data["status"] == False
        data["data"] == "读取文件失败%s" % path
        return data
    file_object = open(path,"r")
    all_the_text = ""
    try:
        all_the_text = file_object.read()
        data["data"] = all_the_text
        print all_the_text
    finally:
        print traceback.format_exc()
        file_object.close()
    return data

def currenttime():
    """
    获取当前时间
    :return:
    """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')