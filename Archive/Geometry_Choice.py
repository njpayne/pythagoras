# Write a program that allows the user to choose from one of 4 different
# options and return the value of those functions. Specifically:
# 1) Area of a circle
# 2) Circumference of a circle
# 3) Area of a rectangle
# 4) Perimeter of a rectangle

# Allow the user to make a choice prior to executing the function that
# they would like to execute (using a menu driven approach)

import math # Import the math library to be used
	# Make sure that the import math function is outside of the function to be used

def main():
	print("Welcome to the geometry program!")
	print("This program allows you to do mathematical calculations.")
	print("Please choose from one of the following options") 
	print("1 = area of a circle") 
	print("2 = circumference of a circle")
	print("3 = area of a rectangle") 
	print("4 = perimeter of a rectangle")
	print("Please type -1 to exit!")
	choice = int(input("Please enter your selection now: "))
	
	while choice != -1:
		print("")
		
		if choice == 1:
			print("You would like to find the area of a circle!")
			p = float(input("Please enter the radius of your circle (in cm): "))
			print("The area of your circle is",
				format(area_circle(p), '.2f'), "cm squared!")
			
			print("")
			print("Would you like to make another choice?")
			print("Remember that -1 exits the program!")
			choice = int(input("Please enter your selection now: "))

		elif choice == 2:
			print("You would like to find the circumference of a circle!")
			q = float(input("Please enter the radius of your circle (in cm): "))
			print("The circumference of your circle is", 
				format(cir_circle(q), '.2f'), "cm!")

			print("")
			print("Would you like to make another choice?")
			print("Remember that -1 exits the program!")
			choice = int(input("Please enter your selection now: "))

		elif choice == 3:
			print("You would like to find the area of a rectangle!")
			length = float(input("Please enter the length of your rectangle (in cm): "))
			width = float(input("Please enter the width of your rectangle (in cm): "))
			print("The area of your rectangle is",
				format(area_rectangle(length, width), '.2f'), "cm squared!")

			print("")
			print("Would you like to make another choice?")
			print("Remember that -1 exits the program!")
			choice = int(input("Please enter your selection now: "))

		elif choice == 4:
			print("You would like to find the perimeter of a rectangle!")
			print("You would like to find the area of a rectangle!")
			length = float(input("Please enter the length of your rectangle (in cm): "))
			width = float(input("Please enter the width of your rectangle (in cm): "))
			print("The area of your rectangle is",perimeter_rectangle(length, width),"cm!")

			print("")
			print("Would you like to make another choice?")
			print("Remember that -1 exits the program!")
			choice = int(input("Please enter your selection now: "))

		else:
			print("You did not enter a valid selection!")
			print("Would you like to make another choice?")
			print("If so, please start the program again & make a more accurate choice!")
			choice = int(input("Please enter your selection now: "))

def area_circle(x): # The area of a circle function
	y = math.pi * (x ** 2) # Note that the area = pi*r^2
	return y

def cir_circle(x): # Note that the diameter = pi * d ; or pi * r * 2
	y = math.pi * ( x * 2)
	return y

def area_rectangle(x, y): # Calculates the area of a rectangle
	z = x * y
	return z

def perimeter_rectangle(x, y):
	peri = (2 * x) + (2 * y)
	return peri

main() # Call the main function
