#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Referenced by https://hibiki-press.tech/python/sorted_sort/594
@author: hibikisan
"""
import string
import random
from operator import itemgetter
import time
import math
import matplotlib.pyplot as plt

def rand_str():
    c = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return random.choice(c)

def rand_strs(n):
    return ''.join([rand_str() for n in range(n)])

def make_data_(n0, n1, m):
    data = (rand_strs(n0), rand_strs(n1), random.randint(0, m))
    return data

def make_data(num):
    data = []
    for i in range(num):
        data.append(make_data_(5, 5, 10000))
    return data

#print(make_data(10))
if __name__ == '__main__':

    #Set the number 
    x = range(1, 7)
    timelist00 = []
    timelist01 = []
    sortdata = []
    
    for i in x:
        sortdata = []
        N = pow(10, i)

        #Generate data
        sortdata = make_data(N)
        #print(sortdata)
        
        time0 = time.time()
        #Use lambda for key function
        sortdata00 = sorted(sortdata, key = lambda x:x[2])
        time1 = time.time()
        #print(sortdata00)
        
        #Use itemgetter for key function
        sortdata01 = sorted(sortdata, key = itemgetter(2))
        time2 = time.time()
        #print(sortdata01)
        
        print('N={}'.format(N))
        print('Use lambda:{}'.format(time1 - time0))
        print('Use itemgetter:{}'.format(time2 - time1))
        timelist00.append(time1 - time0)
        timelist01.append(time2 - time1)
    
    #Draw graph with logarithmic scale
    plt.plot(x, [math.log10(x) for x in timelist00], label='lambda')
    plt.plot(x, [math.log10(x) for x in timelist01], label='itemgetter')

    plt.xlabel("log10(N)")
    plt.ylabel("log10(Time) [s]")
    plt.legend()
    plt.show()    
