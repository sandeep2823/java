#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 22:23:45 2018

@author: sandeepsingh
"""

'''
How tall is th tree : 5

    #
   ###
  #####
 #######   
#########   
    #
'''

# Use 1 while loop and 3 for loops
# 4 spaces : 1 hash
# 3 spaces : 3 hash
# 2 spaces : 5 hash
# 1 spaces : 7 hash
# 0 spaces : 9 hash  

# Get the number of rows for the tree

tree_height = input("Please enter the height of the tree: ")

# COnvert into an integer

tree_height = int(tree_height)

# Get the starting spaces for the top of the tree

spaces = tree_height - 1

# There is one hash to start that will be incremented

hashes = 1

# Save stump spaces till later

stump_space = tree_height - 1

# Make sure the right number of rows are printed

while tree_height != 0:
    
# Print the spaces
    
    for i in range(spaces):
        print(' ', end="")    

# Print the hashes
        
    for i in range(hashes):
        print('#', end="")    
              
# Newline after each row is printed
        
    print()

# Spaces are decremented by 1 each time
    
    spaces -= 1

# hashes are incremented by 2 each time              

    hashes += 2
    
# Decrement the height of the tree each time to jump out of the loop

    tree_height -= 1

# Print the spaces before the stump and then the hash

for i in range(stump_space):
    print(' ', end="")
    
# Print the hash
print('#')    
    

















   
   
   
   