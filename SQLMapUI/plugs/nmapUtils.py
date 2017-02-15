#coding=utf-8
import re
import sys,os
import threading

import nmap

'''
需安装python_nmap包，支持2.x以及3.x
python_nmap包提供了python调用nmap的一系列接口

（一）重要类及方法：
1.创建nmap扫描器
class PortScanner()
    __init__(self, nmap_search_path=('nmap', '/usr/bin/nmap', '/usr/local/bin/nmap', '/sw/bin/nmap', '/opt/local/bin/nmap'))
    Initialize PortScanner module

    * detects nmap on the system and nmap version
    * may raise PortScannerError exception if nmap is not found in the path

    :param nmap_search_path: tupple of string where to search for nmap executable. Change this if you want to use a specific version of nmap.
    :returns: nothing
2.扫描器方法
scan(self, hosts='127.0.0.1', ports=None, arguments='-sV', sudo=False)
    Scan given hosts

    May raise PortScannerError exception if nmap output was not xml

    Test existance of the following key to know if something went wrong : ['nmap']['scaninfo']['error']
    If not present, everything was ok.

    :param hosts: string for hosts as nmap use it 'scanme.nmap.org' or '198.116.0-255.1-127' or '216.163.128.20/20'
    :param ports: string for ports as nmap use it '22,53,110,143-4564'
    :param arguments: string of arguments for nmap '-sU -sX -sC'
    :param sudo: launch nmap with sudo if True

    :returns: scan_result as dictionnary

（二）例子
import nmap
scanner = nmap.PortScanner()    #nmap_search_path已包含了nmap所在路径，若默认路径中没有nmap,则需指出
results = scanner.scan(hosts='192.168.2.1',ports='80')
pprint.pprint(results)
{'nmap': {'command_line': 'nmap -oX - -p 80 -sV 192.168.2.1',
          'scaninfo': {'tcp': {'method': 'syn', 'services': '80'}},
          'scanstats': {'downhosts': '0',
                        'elapsed': '11.59',
                        'timestr': 'Thu Jul 21 10:08:34 2016',
                        'totalhosts': '1',
                        'uphosts': '1'}},
 'scan': {'192.168.2.1': {'addresses': {'ipv4': '192.168.2.1',
                                        'mac': 'D0:C7:C0:6A:F6:A0'},
                          'hostnames': [],
                          'status': {'reason': 'arp-response',
                                     'state': 'up'},
                          'tcp': {80: {'conf': '3',
                                       'cpe': '',
                                       'extrainfo': '',
                                       'name': 'http',
                                       'product': '',
                                       'reason': 'no-response',
                                       'state': 'filtered',
                                       'version': ''}},
                          'vendor': {'D0:C7:C0:6A:F6:A0': 'Tp-link '
                                                          'Technologies'}}}}

'''
def anlyze_port(target_port):
    #解析-p参数传入的值，返回端口列表
    #需要扫描的主机端口，支持1-100或21,53,80两种形式
    try:
        pattern = re.compile(r'(\d+)-(\d+)')    #解析连接符-模式
        match = pattern.match(target_port)
        if match:
            start_port = int(match.group(1))
            end_port = int(match.group(2))
            return([x for x in range(start_port,end_port + 1)])
        else:
            return([int(x) for x in target_port.split(',')])
    except Exception as err:
        print('请注意错误:',sys.exc_info()[0],err)
        exit(0)

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
    results = scanner.scan(hosts=target_host,ports=target_port,arguments=arguments,sudo=False)  #禁ping的快速扫描
    # 返回扫描结果的文件位置
    return current_path+target_host

def main():
    target_host = "172.16.101.143"
    target_port = "3306,80"

    # target_port = anlyze_port(target_port)
    # for port in target_port:
    #     t = threading.Thread(target=portscanner,args=(target_host,str(port)))
    #     t.start()
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
if __name__ == '__main__':
    main()