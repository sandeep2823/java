#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 22:47:42 2018

@author: sandeepsingh
"""

# Multiple Return

def mul_divide(num1, num2):
    return (num1 * num2 , num1 / num2)

mul, divide = mul_divide(4, 2)

print("4 * 2 = ", mul)
print("4 / 2 = ", divide)