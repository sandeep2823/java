#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 23:32:24 2018

@author: sandeepsingh
"""

# Have the user enter their investment amount and expected interest
# Each year their investment will increase by their investment + investment * interst rate
# Print out the earning after 10 years

# Ask for money invested and interest rate

amount = input("Enter the amount to invest: ")
interest_rate = input("Enter the interest: ")
year = input("Enter duration in years: ")

# Convert the value to float
amount = float(amount)

# Convert Interest to percentage

percentage = float(interest_rate) / 100

# Cycle through 10 years using a for loop and range from 0 to 9

for i in range(int(year)):
    amount = amount + (amount * percentage)

print("final amount after 10 years is : {:.2f}".format(amount))