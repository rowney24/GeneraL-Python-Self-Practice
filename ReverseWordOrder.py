# -*- coding: utf-8 -*-
"""
Created on Mon May  2 11:17:31 2022

@author: Ronald Chitauro
"""



def takeString(stringlystring):
    newset = stringlystring.split(" ")
    newset.reverse()
    newsetReturn = " ".join(str(x) for x in newset)
    return print("The reversed word order is:  ", newsetReturn)
    
    















string = input("Please enter your string of choice")
takeString(string)