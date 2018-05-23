#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reference: https://hibiki-press.tech/algorithm/fibonatch/336
@author: hibikisan
"""
import time
import matplotlib.pyplot as plt

def fibo(n):
    f = [0 for i in range(n)]
    f[0] = 0
    f[1] = 1
    i = 2
    while i < n:
        f[i] = f[i-2] + f[i-1]
        i += 1
    return f
    
if __name__ == '__main__':
    import math
    
    #Define the list in which processing time is stored
    timelist = []

    for i in range(1, 5):
        # n is set to 10^i (1<=i<=4) 
        n = pow(10, i)
        fibo_ = []
    
        #Start time
        time0 = time.time()
        #Calculate fibonacci sequence 
        fibo_ = fibo(n)
        #End time
        time1 = time.time()
        #Add the processing time to 'timelist'
        timelist.append(time1 - time0)
    
        print('time for fibonacci:{} => {}'.format(pow(10, i), time1 - time0))

#Draw graph with logarithmic scale    
plt.plot(range(1, 5), [math.log10(x) for x in timelist])
plt.title("Fibonacci sequence")
plt.xlabel("log10(N)")
plt.ylabel("log10(Time) [s]")
plt.show()