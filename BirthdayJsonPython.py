# -*- coding: utf-8 -*-
"""
Created on Sun May  8 12:53:12 2022

@author: Ronald Chitauro
"""

#Just a small program using Json to store data 


import json


def BirthdayRecords(nameBirthdays):
    return print(nameBirthdays,"'s birthday is on", infoBirthdays[nameBirthdays])
    
   



dictBirthdays = {"Ronald":"27-02-1996","Richard":"27-02-1996","Raymond":"24-10-2001","Martin":"25-01-1961","Margrate":"25-10-1968",}


with open("FamBirthdays.json", "w")as f: #writing the Json file
    json.dump(dictBirthdays, f)
    
with open("FamBirthdays.json", "r") as f: #Saving the json file onto the disk
    infoBirthdays = json.load(f)
    
    
nameBirthday = input("Enter the name of the person whose birthday you want to see below: \n") #Ask user for name

BirthdayRecords(nameBirthday) #pass this name into a function
    




