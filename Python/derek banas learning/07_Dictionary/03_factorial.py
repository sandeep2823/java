#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 23:16:11 2018

@author: sandeepsingh
"""

# Factorial

def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result
    
print(factorial(6))    