#coding=utf-8
import re
import sys,os
import threading
import uuid

import nmap

def portscanner(target_host,target_port,arguments="-T4 -A -v -Pn"):
    """
    :param target_host:
    :param target_port:
    :return:
    -sS 使用SYN半开式扫描，这种扫描方式使得扫描结果更加正确(又称半开放,或隐身扫描)
    -T4 -T(0-5) 默认为3 4 即Aggressive模式。设置5分钟的超时限制，对每台主机的扫描时间不超过5分钟，并且对每次探测回应的等待时间不超过1.5秒。
    -A 同时启用操作系统指纹识别和版本检测
    """
    current_path = "%s/nmap_file/" % (os.getcwd())
    if os.path.exists(current_path) == False:
        os.mkdir("nmap_file")
    arguments = arguments + " -oN %s%s" % (current_path,target_host)
    if target_port == "" or target_port is None:
        target_port = "1-65535"
    scanner = nmap.PortScanner()
    results = scanner.scan(hosts=target_host,ports=target_port,arguments=arguments,sudo=False)
    # 返回扫描结果的文件位置
    return current_path+target_host,results

def main():
    target_host = "172.16.101.143"
    target_port = "3306,80"

    portscanner(target_host,"")

def pinter(result):
    """

    :param result: nmap扫描的json结果
    :return:  str
    """
    str = "Starting Nmap 7.40 ( https://nmap.org ) at %s \n" % result['nmap']['scanstats']['timestr']
    str = str + "command_line : %s \n" % result['nmap']['command_line']
    for ip in result['scan']:
        ip_info= result['scan'][ip]
        # 主机状态
        status = ip_info['status']['state']
        # 主机名称
        hostname = ip_info['hostnames'][0]['name']
        # ip
        ip = ip_info['addresses']['ipv4']
        str1 = ""
        opens = 0
        #### 以下是该服务器中所开启的tcp端口
        for port,port_info in ip_info['tcp'].items():
            name = port_info['name']
            state = port_info['state']
            version = port_info['version']
            if state != "closed":
                opens+=1
                str1 = str1 + "端口【%s】状态为【%s】开放服务【%s】版本【%s】\n" % (port,state,name,version)

        str = str + "【%s】有【%s】个端口开放\n" % (ip,opens)
        str = str + str1
        str = str + "\n"
    return str

def format(result):
    """

    :param result: nmap扫描的json结果
    :return:  str
    """
    data = [{"id":str(uuid.uuid1()),"name":"Port Scan Result","open":"true","children":[]}]
    key_ip = result['scan'].keys()
    key_ip.sort(lambda x,y: cmp(''.join( [ i.rjust(3, '0') for i in x.split('.')] ), ''.join( [ i.rjust(3, '0') for i in y.split('.')] ) ) )
    for ip in key_ip:
        ip_info= result['scan'][ip]
        # 主机状态
        status = ip_info['status']['state']
        # 主机名称
        hostname = ip_info['hostnames'][0]['name']
        # ip
        ip = ip_info['addresses']['ipv4']
        # 当前循环服务器端口信息
        data_ = {"id":str(uuid.uuid1()),"name":ip,"children":[]}
        str1 = ""
        opens = 0
        #### 以下是该服务器中所开启的tcp端口
        if ip_info.get("tcp"):
            bingo = 0
            for port,port_info in ip_info['tcp'].items():
                # 开放服务
                name = port_info['name']
                # 端口状态
                state = port_info['state']
                # 服务版本
                version = port_info['version']
                data_["name"] = ip
                if state == "open":
                    data_["children"].append({"id":str(uuid.uuid1()),"name":str(port) + "(%s)" % name,"ip":ip})
                    bingo+=1
            if bingo > 0:
                data[0]["children"].append(data_)

    return data
if __name__ == '__main__':
    main()