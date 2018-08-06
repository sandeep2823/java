#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 23:04:48 2018

@author: sandeepsingh
"""
number = 5
while True:
    guessed_num = int(input("Please enter a number between 1 to 10: "))
    if guessed_num == number:
        print("you guessed it right !!!")
        break


    
