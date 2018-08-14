#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 23:26:25 2018

@author: sandeepsingh
"""

import math

def get_area(shape):
    shape = shape.lower()
    
    if shape == "circle":
        circle_area()
        
    elif shape == "rectangle":
        rectangle_area()
        
    else:
        print("Please enter rectangle or circle ")

def circle_area():
    radius = float(input("PLease enter the radius: "))
    area = (math.pow(radius, 2)) * math.pi
    print("area of circle is {:.2f}".format(area))    

def rectangle_area():
    length = float(input("Please enter the length: "))
    width = float(input("Please enter the width: "))
    print("area of rectangle is: ", length * width)

def main():
    shape = input("enter the shape to calculate area: ")
    get_area(shape)
    
main()    