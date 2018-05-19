#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 2018
@author: hibikisan
"""

def charcounter(l):
    count_ ={}
    for s in l:
        count_.setdefault(s, 0)
        count_[s] += 1
    return count_
    

if __name__ == '__main__':
  
    message = 'This dog helped him watch the sheep.'
    count = charcounter(message)
    print(count)
    
    

