# -*- coding: utf-8 -*-
"""
Created on Fri May  6 18:55:13 2022

@author: Ronald Chitauro
"""


#Prime Numbers


#function
def primenumber(numberInput):

    if numberInput == 1 or numberInput == 2 or numberInput == 3 or numberInput == 5 or numberInput == 7:
        return print("The number you input is a prime number")
    if numberInput % 2 == 0 or numberInput % 3 == 0 or numberInput % 5 == 0 or numberInput % 7 == 0:
        return print("The number you input is not a prime number")
    else:
        return print("The number you input is a prime number")
        









numberIntake = input("Please input the number below:\n")
primenumber(int(numberIntake))
