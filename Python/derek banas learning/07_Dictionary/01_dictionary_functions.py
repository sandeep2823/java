#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 22:26:47 2018

@author: sandeepsingh
"""

# Add a dictionary 
sandDict = {"fname" : "Sandeep", "lname" : "Singh", "address" : "Delhi"}
print("My name :", sandDict["fname"])

#Change the value of the key
sandDict["address"] = "Delhi NCR" 

print(sandDict["address"])

# Add a key value pair
sandDict['age'] = "22"

print(sandDict)

# Check if the value is present
print("Is there a age :", "age" in sandDict)

# Print key value pair

print(sandDict.values())
print(sandDict.keys())

# Print key value pair 

for k, v in sandDict.items():
    print(k, v)

#print default valueif key is not present
print(sandDict.get("mname", "Not Here"))

# Delete a key

del sandDict["lname"]
print(sandDict)


# Print key pair using for loop
for i in sandDict:
    print(i)
    
# clear the dictionary
sandDict.clear()    
    
# Create list of dictionary
employee = []
fname, lname = input("enter employee name: ").split()
employee.append({"fname" : fname, "lname" : lname})
print(employee)    
    
    
    
    
    
    