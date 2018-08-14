#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 21:24:33 2018

@author: sandeepsingh
"""
# Generate 5 random number and store it in list and print

import random

numList = []

for i in range(5):
    numList.append(random.randrange(1,10))

for i in numList:
    print(i,end=", ")


    