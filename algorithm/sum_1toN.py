#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 23 2018
@author: hibikisan
"""
import time
import matplotlib.pyplot as plt
import math

def sum1(n):
    sum = 0
    var = 1
    while(var <= n):
        sum += var
        var += 1
    print('sum={}'.format(sum))
    
if __name__ == '__main__':
    #Define the list in which the processing time is stored
    timelist = []

    for i in range(1, 9):
        #N is set to N^i (1<=i<=9)
        n = pow(10, i)
        #Start time
        time0 = time.time()
        #Calculate the sum from 1 to N 
        sum1(n)
        #End time
        time1 = time.time()
        #Add the proecessing time to 'timelist'
        timelist.append(time1 - time0)
    
        print('time for sum1:1-10^{} => {}'.format(i, time1 - time0))

#Draw graph with logarithmic scale
plt.plot(range(1, 9), [math.log10(x) for x in timelist])
plt.title("SUM 1 TO N")
plt.xlabel("log10(N)")
plt.ylabel("log10(Time) [s]")
plt.show()