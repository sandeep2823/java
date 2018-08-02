#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 22:33:09 2018

@author: sandeepsingh
"""

# Problem : Receive miles and convert to kilometera

miles = input("Please enter the miles : ")

# Convert miles to kilometer and store into kilometer

kilometer = int(miles) * 1.60934

# Print the kilometer value

print("{} miles equals {} kilometers".format(miles , kilometer))

