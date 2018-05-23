#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reference: https://hibiki-press.tech/algorithm/sum_array/659
@author: hibikisan
"""
import random
import time
import math
import matplotlib.pyplot as plt

def sum_array(data, n):
    sum_ = 0
    for idx in range(n):
        sum_ += data[idx]

    return sum_

if __name__ == '__main__':
    #Define the list in which the processing time is stored
    timelist = []
    #Set the logarithmic number for the length of data array
    x = range(1, 8)
    
    for i in x:
        #N is set to N^i (1<=i<=9)
        n = pow(10, i)
        #Generate numbers between 0 to 100 randomly for data 
        data = [random.randint(0, 100) for val in range(n)]
        #Start time
        time0 = time.time()
        #Calculate the sum from 1 to N 
        s = sum_array(data, n)
        #End time
        time1 = time.time()
        #Add the proecessing time to 'timelist'
        timelist.append(time1 - time0)
    
        print('processing time for sum of 10^{} numbers => {}'.format(i, time1 - time0))

#Draw graph with logarithmic scale
plt.plot(x, [math.log10(x) for x in timelist])
plt.title("SUM DATA ARRAY")
plt.xlabel("log10(N)")
plt.ylabel("log10(Time) [s]")
plt.show()