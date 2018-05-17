#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hibikisan
"""
import random
import time
import math
import matplotlib.pyplot as plt

def cal_max(data, n):
    val_max = data[0]
    idx = 0
    while idx < n:
        if data[idx] > val_max:
            val_max = data[idx]
        idx += 1
    
    return val_max

def cal_min(data, n):
    val_min = 999
    idx = 0
    while idx < n:
        if data[idx] < val_min:
            val_min = data[idx]
        idx += 1
    
    return val_min

if __name__ == '__main__':
    #Define the list in which the processing time is stored
    timelist_max = []
    timelist_min = []
    #Set the logarithmic number for the length of data array
    x = range(1, 7)
    for i in x:
        #N is set to N^i (1<=i<=9)
        n = pow(10, i)
        #Set the list of 'data' which inclueds n elements generaged randomly
        data = [random.randint(0, 100) for n in range(n)]
        #print('DATA:{}'.format(data))
        #Start time
        time0 = time.time()

        max_ = cal_max(data, len(data))
        time1 = time.time()
        timelist_max.append(time1-time0)

        min_ = cal_min(data, len(data))
        time2 = time.time()
        timelist_min.append(time2-time1)

        print('N:{}'.format(n))
        print('Max={}/Processing Time:{}'.format(max_, time1-time0))
        print('Min={}/Processing Time:{}'.format(min_, time2-time1))

#Draw graph with logarithmic scale
plt.plot(x, [math.log10(x) for x in timelist_max], label='MAX')
plt.plot(x, [math.log10(x) for x in timelist_min], label='MIN')

plt.title("MAX/MIN of DATA ARRAY")
plt.xlabel("log10(N)")
plt.ylabel("log10(Time) [s]")
plt.legend()
plt.show()
        
        
    