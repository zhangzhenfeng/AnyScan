#!/usr/bin/env python
# -*- coding:utf-8 -*-
if __name__ == '__main__':
    # num1和num2相同长度，存储到list中
    num_1 = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4]
    num_2 = [64,65,66,67,89,90,12,13,14,25,11,34,56,78,34]

    old_num = num_1[0]

    for index in range(0,len(num_1)):
        #print str(num_1[index]) + "   " + str(old_num)
        if num_1[index] != old_num:
            print num_2[index]
            old_num = num_1[index]

