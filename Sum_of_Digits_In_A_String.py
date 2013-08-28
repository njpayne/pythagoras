# Write a program that asks the user to enter a series of single-digit numbers with nothing separating them
# The program should display the sum of all the single-digit numbers in the string.
# For example, is the user enters 2154, the method should return 12, which is the sum of 2, 1, 5, 4

def sum(): # Define the sum function
	container = [] # The list used to hold the numbers	
	number = input("Please enter a string of numbers that contains spaces: ") # Get the number from the user
	
	for x in number: # Loop through all the characters in the number entry
		container.append(int(x)) # int(x) converts a string value to an integer (if possible)

	total = 0 # Set the total equal to zero
	for b in range(0,len(container)):
		total += container[b] # Loop through the entries in the container to generate a total
	
	print("You entered the string: ", number)
	print("The sum of all the numbers in your string is", total, "!")
	
sum() # Call the first function