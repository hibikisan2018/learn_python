#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 18:56:20 2018
@author: hibikisan
"""
def makelist01(n):
    a = []
    for i in range(n):
        a.append(2*i+1)
    return a

def makelist02(n):
    return list(map(lambda x:2*x+1, range(n)))

def makelist03(n):
    return [2*n_+1 for n_ in range(n)]

if __name__ == '__main__':
    import time
    import math
    import matplotlib.pyplot as plt
   
    #Set the number 
    x = range(1, 7)
   
    timelist_01 = []
    timelist_02 = []
    timelist_03 = []
    
    for i in x:
        n = pow(10, i)

        #Start time
        time0 = time.time()
        list01 = makelist01(n)
        time1 = time.time()
           
        list02 = makelist02(n)
        time2 = time.time()
    
        list03 = makelist03(n)
        time3 = time.time()
        
        #Store the processing time of each medhod
        timelist_01.append(time1 - time0)
        timelist_02.append(time2 - time1)
        timelist_03.append(time3 - time2)

        print('for loop\t\t:{}'.format(time1 - time0))
        print('map function\t\t:{}'.format(time2 - time1))
        print('list comprihension\t:{}'.format(time3 - time2))
        
    #Draw graph with logarithmic scale
    plt.plot(x, [math.log10(x) for x in timelist_01], label = 'for loop')
    plt.plot(x, [math.log10(x) for x in timelist_02], label = 'map function')
    plt.plot(x, [math.log10(x) for x in timelist_03], label = 'list comprehension')

    plt.xlabel("log10(N)")
    plt.ylabel("log10(Time) [s]")
    plt.legend()
    plt.show()
    