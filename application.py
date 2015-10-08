import math
import sys
import os

def ing():
	try:
		print "Calculating factorial of a number"
		num = input ("insert a number to calculate \n")
		if num == int(num):
			print "the factorial of ", num, "is", math.factorial(num)
	except NameError:
		print "you have to insert only numbers"
		raw_input("press enter to continue")
	again()

def again():
	other = raw_input("Do you want to insert any other number? y/n \n")
	if other == "y" or other == "yes":
	    clear()
	    ing()
	elif other == "n" or other == "no":
		exit()    

def clear():
	os.system("cls")

def exit():	 
	raw_input("press enter to continue")   
	sys.exit()
ing()	