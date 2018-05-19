#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on May 20 2018

@author: hibikisan
"""
import random

def raw_sum(data):
    for i in data:
        sum_ = 0
        for j in range(len(i)):
            sum_ += i[j]
        i.append(sum_)
    
    return data
    

if __name__ == '__main__':
    
    dim = (5, 3) # the dimension of original data array
    data = []
    for i in range(dim[0]):
        data.append([random.randint(0, 10) for n in range(dim[1])])
        
    #print(data)
    print('----Original data----')
    for l in data:
        print(l)
    
    sum_data = raw_sum(data)
    #print(sum_data)
    print('----Adding the colomn of sum of each raw----')
    for l in sum_data:
        print(l)