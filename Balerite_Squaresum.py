# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 03:04:19 2019

@author: PL SERIES
"""

squaresum = int(input("Enter Value:"))
i = 1
sum = 0
while(i<= squaresum):
    sum = sum+(i*i)
    
    i=i+1
    
if i>= squaresum:

    print ("The sum of the squares is ", sum)