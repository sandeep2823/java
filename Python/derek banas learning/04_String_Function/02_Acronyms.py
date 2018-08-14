#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 22:26:04 2018

@author: sandeepsingh
"""

# Random Access Memory : RAM

string_word = input("Enter a string: ")

string_word = string_word.upper()

acr = string_word.split()

for i in acr:
    print(i[0], end="")