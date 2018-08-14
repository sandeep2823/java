#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 23:17:20 2018

@author: sandeepsingh
"""

def sumall(*args):
    sum = 0
    
    for i in args:
        sum += i;
        
    return sum

print("sum = ", sumall(1,2,3,4,5))    