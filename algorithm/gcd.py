#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 23:00:10 2018

@author: hibikisan
"""

def gcd(a, b):
    r = a % b
    while(r != 0):
        a = b
        b = r
        r = a % b
    
    return b

if __name__ == '__main__':
    num = input("Enter 2 numbers separated by space. (ex: 24 36) ")
    num_ = list(map(int, num.split(' ')))
    a, b = num_[0], num_[1]

    n = gcd(a, b)
    print('The greatest common divisor of {} and {} is {}'.format(a, b, n))
    