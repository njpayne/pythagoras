# The colors red, blue, and yellow are known as the primary colors because they
# cannot be obtained by mixing other colors. When you mix two colors, you get a
# secondary color, as shown here: red + blue = purple, red + yellow = orange
# blue + yellow = green. Design a program that prompts the user to enter the
# names of two primary colors to mix. If the user enters anything other than "red",
# "blue", or "yellow", the program should display an error message. Otherwise,
# the program should display the name of the secondary color that results.

print("Welcome to the color mixer!")
a = input("Please enter the first color that you want to mix: ")
b = input("Please enter the second color that you want to mix: ")

def mixer(x, y):
	if a not in ('red', 'blue', 'yellow'): # 'not in' is used instead of !=
		print("Please re-enter your first color, as it was not a primary color!")
	elif b not in ('red', 'blue', 'yellow'): # 'not in' is used instead of !=
		print("Please re-enter your second color, as it was not a primary color!")
	else: # Return the relevant output
		if (a == 'red' and b == 'blue') or (a == 'blue' and b == 'red'):
			print("You mixed", a, "and", b, ". This creates the color purple!")
		elif (a == 'red' and b == 'yellow') or (a == 'yellow' and b == 'red'):
			print("You mixed", a, "and", b, ". This creates the color orange!")
		elif (a == 'blue' and b == 'yellow') or (a == 'yellow' and b == 'blue'):
			print("You mixed", a, "and", b, ". This creates the color green!")

print("") # Print a blank line
mixer(a, b) # Call the function mixer
