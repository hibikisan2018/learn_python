#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 19 2018
@author: hibikisan
"""
def rank(data):
    #generage array "rank" whose all elements are 1 and whose length is the same as "data" 
    rank = [1 for n in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] < data[j]:
                rank[i] += 1
    
    return rank

if __name__ == '__main__':
    import random
    import time
    import math
    import matplotlib.pyplot as plt

    #Set the number 
    x = range(1, 6)
    timelist = []
    
    for i in x:
        n = pow(10, i)

        #generate data which is consist of integer between 0 and 100 and ordered randomly
        data = [random.randint(0, 100) for m in range(n)]

        #Start time
        time0 = time.time()
        list01 = rank(data)
        #End time
        time1 = time.time()
           
        #Store the processing time of each medhod
        timelist.append(time1 - time0)

        print('Number of elementst:{}'.format(n))
        print('Processing time of ranking elementst:{}'.format(time1 - time0))
        
    #Draw graph with logarithmic scale
    plt.plot(x, [math.log10(x) for x in timelist])
    plt.xlabel("log10(N)")
    plt.ylabel("log10(Time) [s]")
    plt.show()
    



