#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 22:05:56 2018

@author: sandeepsingh
"""

# Ask the user to input 2 values and store them in variables num1 num2

num1 , num2 = input("Please enter two numbers ").split()

# Convert the Strings into regular numbers Integer

num1 = int(num1)
num2 = int(num2)

# Add the vulues entered and store in variable sum 

sum = num1 + num2

# Subtract the vulues entered and store in variable difference 

difference = num1 - num2

# Multiply the vulues entered and store in variable product 

product = num1 * num2

# Divide the vulues entered and store in variable quotient 

quotient = num1 / num2

# Use Modulus on the vulues entered to find the remainder

remainder = num1 % num2

# Print the results  

print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))