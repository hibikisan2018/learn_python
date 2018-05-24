#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Referenced from https://hibiki-press.tech/algorithm/gcd/700
@author: hibikisan
"""
def iterative_gcd(a, b):
    r = a % b
    while(r != 0):
        a = b
        b = r
        r = a % b
    return b

def recursive_gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return recursive_gcd(b, a % b)

if __name__ == '__main__':
    num = input("Enter 2 numbers separated by space. (ex: 24 36) ")
    num_ = list(map(int, num.split(' ')))
    a, b = num_[0], num_[1]
    
    print('The greatest common divisor of {} and {} is'.format(a, b))
    print('Iterative:{}'.format(iterative_gcd(a, b)))
    print('Recursive:{}'.format(recursive_gcd(a, b)))
    