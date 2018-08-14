#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 23:21:25 2018

@author: sandeepsingh
"""

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        series = fibonacci(num - 1) + fibonacci(num - 2)
        return series
   
print(fibonacci(6))    