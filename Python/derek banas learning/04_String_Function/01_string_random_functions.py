#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:15:08 2018

@author: sandeepsingh
"""
rand_string = "    this is a string     "

rand_string = rand_string.lstrip()

rand_string = rand_string.rstrip()

rand_string = rand_string.strip()

print(rand_string.capitalize())

print(rand_string.upper())

print(rand_string.lower())

a_list = ["a", "bunch", "of", "words"]
print(" ". join(a_list))

a_list_2 = rand_string.split()
for i in a_list_2:
    print(i)
    
print("How many is : ", rand_string.find("is"))

print("Where is string : " , rand_string.find("string"))

print(rand_string.replace("a", "very important"))