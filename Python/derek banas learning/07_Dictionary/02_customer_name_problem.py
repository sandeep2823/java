#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 22:53:56 2018

@author: sandeepsingh
"""
cust_name = []
while True:
    response = input("enter customer (Yes/ No) : ")
    response = response[0].lower()
    if response == "y":
        fname, lname = input("Enter cunstomer name: ").split()
        cust_name.append({'fname' : fname, 'lname' : lname})
        #cust_name.append("{} {}".format(fname,lname))
    elif response == "n":
        break

#print(cust_name)  
for cust in cust_name:
    print(cust['fname'], cust['lname'])