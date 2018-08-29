#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:20:01 2018

@author: sandeepsingh
"""

class Dog:
    
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight
    
    def run(self):
        print("{} the dog runs".format(self.name))
        
    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))        
     
        
def main():
    trigger = Dog("trigger", 66, 26)
    trigger.bark()
    
    bullet = Dog("Bullet", 45, 23)
    bullet.eat()

        
main()        