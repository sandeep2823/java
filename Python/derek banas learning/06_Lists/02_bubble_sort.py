#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 21:48:15 2018

@author: sandeepsingh
"""

# Bubble sort

import random

numList = []

for i in range(5):
    numList.append(random.randrange(1,10))
    
for j in numList:
    print(j, end=", ")    
  
i = len(numList) - 1

while i > 1:
    
    j = 0
    
    while j < i:
        print()
        print("\nIs {} > {}".format(numList[j], numList[j + 1]))
        
        if numList[j] > numList[j + 1]:
            print ("Switch")
            
            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        
        else:
            print("Don't Switch")
            
        j += 1
        
        for k in numList:
            print(k, end=", ")
    print("\nEND OF ROUND")        
        
    i -= 1

for k in numList:
    print(k, end=", ")

print()        
