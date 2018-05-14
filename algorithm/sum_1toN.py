#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 23 2018
@author: hibikisan
"""
import time
import matplotlib.pyplot as plt

def sum1(n):
    sum = 0
    var = 1
    while(var <= n):
        sum += var
        var += 1
    print('sum={}'.format(sum))
    
if __name__ == '__main__':
    #n = int(input('Calcurate the sum from 1 to n. enter the number n...'))

    timelist = []

    for i in range(1, 9):
        n = pow(10, i)
    
        time0 = time.time()
        sum1(n)
        time1 = time.time()
        
        timelist.append(time1 - time0)
    
        print('time for sum1:1-10^{} => {}'.format(i, time1 - time0))
    
plt.plot(range(1, 9), timelist)
plt.title("SUM 1 TO N")
plt.xlabel("N: 10^x")
plt.ylabel("Time [s]")
plt.show()