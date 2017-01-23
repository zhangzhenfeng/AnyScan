# -*- coding: utf-8 -*-
import os,itertools
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

    for i in itertools.combinations(names, 2):
        combination.append(i[0] + "," + i[1])

    # 例如：'apostrophemask,apostrophenullencode', 'apostrophemask,appendnullbyte']
    return combination

