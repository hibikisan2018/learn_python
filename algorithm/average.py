#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reference: https://hibiki-press.tech/algorithm/ave_with_sentinel/661
@author: hibikisan
"""
import random

def average(data):
    count = 0
    sum_ = 0
    idx = 0
    while data[idx] != -1:
        sum_ += data[idx]
        count += 1
        idx += 1
    average = sum_ / count
    return average

if __name__ == '__main__':
    #Generate input data
    data = [0] * 10
    n = random.randint(1, 9)
    data[:n] = [random.randint(0, 100) for n in range(n)]
    data[n] = -1
    print(data)

    ave = average(data)
    print(ave)