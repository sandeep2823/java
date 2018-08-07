#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 22:56:43 2018

@author: sandeepsingh
"""
# A - Z = 65 - 90
# a - z = 97 - 122
# Enter a string to hide in uppercase : HIDE

normal_string = input("Please enter a message to hide : ")

secret_string = ""

# Cycle through each character in the string

for char in normal_string:
    secret_string += str(ord(char) - 23)
    
# Print secret string
    
print("Secret Message :", secret_string)   

#Cycle through each character code 2 at a time by incrementing by 2 each time

normal_string = ""

for i in range(0, len(secret_string) - 1, 2):
    char_code = secret_string[i] + secret_string[i+1]
    
# Convert the code into character and add them in a new string
    normal_string += chr(int(char_code) + 23)    

# Print the original message
print("Original Message : " , normal_string)