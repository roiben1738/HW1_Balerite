# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 02:21:11 2019

"""
year=int(input("Enter year:"))

if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")