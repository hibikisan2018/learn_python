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
  
    #message_ = 'This dog helped him watch the sheep.'
    message_ = 'Timmie Willie is a country mouse who is accidentally transported to a city in a vegetable basket. When he wakes up, he finds himself in a party and makes a friend. When he is unable to bear the city life, he returns to his home but invites his friend to the village. When his friend visits him, something similar happens.'

    message = message_.split(' ')
    count = charcounter(message)
    print(count)
    
    

