#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 22:32:09 2018

@author: sandeepsingh
"""

# Solve for x

# Receive the string and split into variables

def solve_equation(equation):
    x, eq, num1, equal, num2 = equation.split()
    
    num1, num2 = int(num1), int(num2)
    
    if eq == "+":
        return "x = " + str(num2 - num1)
    
    if eq == "-":
        return "x = " + str(num2 + num1)
    
    if eq == "*":
        return "x = " + str(num2 / num1)
    
    if eq == "/":
        return "x = " + str(num2 * num1)
    
print(solve_equation("x / 3 = 15"))    