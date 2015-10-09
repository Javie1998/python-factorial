"""this program will help the user to calculate the factorial
 of a number, and it will ask the user
  if wants insert other number to calculate"""
import math
import sys
import os

def ing():
    """this function will ask the user for the number that he/she wants to calculate"""
    try:
        print "Calculating factorial of a number"
        num = raw_input("insert a number to calculate \n")
        if num == int(num):
            print "the factorial of ", num, "is", math.factorial(num)
    except NameError:
        print "you have to insert only numbers"
        raw_input("press enter to continue")
    again()

def again():
    """in this part the program will ask if the user wants to insert other number"""
    other = raw_input("Do you want to insert any other number? y/n \n")
    if other == "y" or other == "yes":
        clear()
        ing()
    elif other == "n" or other == "no":
        out()

def clear():
    """it only clear"""
    os.system("cls")

def out():
    """and it serves to go out of the program"""
    raw_input("press enter to continue")
    sys.exit()
ing()
