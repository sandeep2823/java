#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 22:40:44 2018

@author: sandeepsingh
"""

# Calculation based on the operator

# Store the user input of 2 numbers and the operator

num1, operator, num2 = input("Enter the number with operator : ").split()

# Convert the Strings into Integers

num1 = int(num1)
num2 = int(num2)

#Condition for operators

if operator == "+":
    result = num1 + num2
    print("{} {} {} = {}".format(num1, operator, num2, result))
    
elif operator == "-":
    result = num1 - num2
    print("{} {} {} = {}".format(num1, operator, num2, result))
    
elif operator == "*":
    result = num1 * num2
    print("{} {} {} = {}".format(num1, operator, num2, result))

elif operator == "/":
    result = num1 / num2    
    print("{} {} {} = {}".format(num1, operator, num2, result))
    
else:
    print("Please use + _ * / operators only")
    

    
    