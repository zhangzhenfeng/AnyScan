# -*- coding: utf-8 -*-
import os,itertools,traceback,datetime,time,re,chardet,requests
def combination_tampper(findPath = "/Users/margin/Desktop/me/white/sqlmap/sqlmap-master/tamper/"):
    # 默认两种组合进行组合排列
    '''
    #获取目录中指定的文件名
    '''
    fileNames = os.listdir(findPath)
    names = []
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
    #return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return time.strftime("%Y-%m-%d %H:%M:%S")

def repeat(url_list):
    check_list = []
    result = []
    check = "((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})?"
    for info in url_list:
        url = info.get("url")
        try:
            u = re.match(check, url, flags=0).group()
            if u not in check_list:
                result.append(info)
                check_list.append(u)
        except:
            print traceback.format_exc()
            print "URL去重异常"
            break
    return result

def current_path():
    return os.getcwd() + "/AnyScanUI/"

def url_patch(url):
    try:
        with_http = "((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})?"
        not_http = "(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})?"

        match = re.match(with_http,url,flags=0)
        _u = None
        if match:
            _u = match.group()
            return url

        _match = re.match(not_http,url,flags=0)
        __u = None
        if _match:
            __u = _match.group()
            return __u
        return url
    except:
        #print traceback.format_exc()
        return url

def __url_title(url):
    title = url
    print url
    try:
        res = requests.get(url,timeout=1).content
        char = str(chardet.detect(res))
        if re.search("encoding': 'GB.*",char):
            res = unicode(res, 'gbk')
            res.encode('utf8')
            t = re.search('<title>(.*?)</title>',res)
            if t:
                title = t.group(1)
                title = title.encode('utf8')
            else:
                title = url
        else:
            t = re.search('<title>(.*?)</title>',res)
            if t:
                title = t.group(1)
            else:
                title = url
        return title
    except:
        #print traceback.format_exc()
        return title

def url_title(url):
    url = url_patch(url)
    title = __url_title(url)
    return title


if __name__ == '__main__':
    print url_title("http://www.cnblogs.com/dkblog/archive/2011/02/28/1980646.html")