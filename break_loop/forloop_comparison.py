#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 02:11:58 2019
@author: hibikisan
"""
import itertools
import time
import matplotlib.pyplot as plt

# Get array example
def get_array(N):
    return [[list(range(j*N*N+k*N, j*N*N+(k+1)*N)) for k in range(N)] for j in range(N)]

# for~else
def exit_loop1(array):
    H, W, D = len(array), len(array[0]), len(array[0][0])
    
    for i in range(H):
        for j in range(W):
            for k in range(D):
                if array[i][j][k] == int(H*H*H/2):
                    break
            else:
                continue
            break
        else:
            continue
        break

# using flg
def exit_loop2(array):
    H, W, D = len(array), len(array[0]), len(array[0][0])

    flg = True
    for i in range(H):
        for j in range(W):
            for k in range(D):
                if array[i][j][k] == int(H*H*H/2):
                    flg = False
                    break
            if flg == False:
                break
        if flg == False:
            break

# return to break
def exit_loop3(array):
    H, W, D = len(array), len(array[0]), len(array[0][0])
    for i in range(H):
        for j in range(W):
            for k in range(D):
                if array[i][j][k] == int(H*H*H/2):
                    return False
    return True

# using itertools
def find_val(array):
    H, W, D = len(array), len(array[0]), len(array[0][0])
    
    for (i, j, k) in itertools.product(range(H), range(W), range(D)):
        if array[i][j][k] == int(H*H*H/2):
            break
    
if __name__ == '__main__':
    
    tl1 = []
    tl2 = []
    tl3 = []
    tl4 = []

    N = 100
    M = 100
    
    H = get_array(N)
    
    for i in range(1, M+1):
        print('--- {}/{} ---'.format(i, M))
    
        t0 = time.time()
        
        exit_loop1(H)
        t1 = time.time()
        d1 = t1- t0
                
        exit_loop2(H)
        t2 = time.time()
        d2 = t2 - t1
        
        exit_loop3(H)
        t3 = time.time()
        d3 = t3 -t2
        
        find_val(H)
        t4 = time.time()
        d4 = t4 -t3
        
        print('loop 1:\t\t{}'.format(d1))
        print('loop 2:\t\t{}'.format(d2))
        print('loop 3:\t\t{}'.format(d3))
        print('itertools:\t{}'.format(d4))
      
        tl1.append(d1*10**3)
        tl2.append(d2*10**3)
        tl3.append(d3*10**3)
        tl4.append(d4*10**3)
     
    labels = ['for~else', 'using flg', 'return to break', 'itertools']
    plt.hist([tl1, tl2, tl3, tl4], label=labels, stacked=False, bins=30)
    
    plt.xlabel("Time (ms)")
    plt.legend()
    plt.show()  