# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:32:56 2017

@author: HN7569
"""
import math

#Welcome Auditor

def welcome():
    name=input("Welcome IAS member! What is your name?")
    print("\nWelcome",name,"!")
    print("\nThis is a program that will help you extrapolate the results from your test.")
    print("\nLet's start by getting some input variables from you.")
    return name

#Import Variables

def population():
    while True:
        try:
            pop=float(input("\nHow many records in your population?"))
            return pop
        except:
           print("\nThat is not a valid number! Try again")

def num_pass():
    while True:
        try:
            np=float(input("\nHow many instances passed in your test?"))
            return np
        except:
           print("\nThat is not a valid number! Try again")
           
def num_fail():
    while True:
        try:
            nf=float(input("\nHow many instances failed in your test?"))
            return nf
        except:
           print("\nThat is not a valid number! Try again")
           
def num_sam():
    while True:
        try:
            ns=float(input("\nHow many instances were in your sample?"))
            return ns
        except:
           print("\nThat is not a valid number! Try again")         

def results(name,population,sample,passed,failed):
    CI=1.96
    sam_def=(failed/sample)
    sam_def=sam_def
    print("\n",name,", your sample defect rate is ",round(sam_def*100,2),"%.")
    s1=(population-sample)/(population-1)
    s2=((sam_def*(1-sam_def))/sample)
    s3=math.sqrt(s1*s2)
    s4=float(s3*CI)
    min_level= (sam_def-s4)
    max_level =(sam_def+s4)
    print("\nYou can be 95% confidence that the actual defect rate in your population is between", round(min_level*100,2), "% and ", round(max_level*100,2),"%.")
    return sam_def
 
    
    
name = welcome()           
population = population()
sample=num_sam()
passed= num_pass()
failed=num_fail()
pct=results(name,population,sample,passed,failed)


import webbrowser

answer= input("\nWould you like to see a video on confidence intervals to understand this? Answer Yes or No.")
if answer == "Yes":
    webbrowser.open("https://www.youtube.com/watch?v=tFWsuO9f74o")


    






#Output sample