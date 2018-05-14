#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 18:56:20 2018
@author: hibikisan
"""
def makelist01():
    a = []
    for i in range(N):
        a.append(2*i+1)
    return a

def makelist02():
    return list(map(lambda x:2*x+1, range(N)))

def makelist03():
    return [2*n+1 for n in range(N)]

if __name__ == '__main__':
    import time
    N = 10**7
    time0 = time.time()
    
    list01 = makelist01()
    time1 = time.time()
       
    list02 = makelist02()
    time2 = time.time()

    list03 = makelist03()
    time3 = time.time()

    print('for loop\t\t:{}'.format(time1-time0))
    print('map function\t\t:{}'.format(time2-time1))
    print('list comprihension\t:{}'.format(time3-time2))
    