# Write a program that gets a string containing a person's first, middle, and last names
# and then displays their first, middle, and last initials. For example, if the user enters the name
# John William Smith, then the program should display J. W. S.

def name(): # Define the main function
	names = [] # Create an empty list to hold all the names
	initials = [] # Create a list to hold the initials

	print("Welcome to the name initial converter!")

	# Note that no explicit variables are declared for the separate names; only a list
	names.append(input("Please enter your first name: ")) # Enter the first name
	names.append(input("Please enter your middle name: ")) # Enter the middle name
	names.append(input("Please enter your last name: ")) # Enter your last name

	for x in names: # Rotate through all the words in the list; x = the words
		initials.append(x[0]) # Select the first letters from each of the words
						
	print("After reviewing your entry, I see that your proper initials are ",
		initials[0], ".", initials[1], ".", initials[2], ".")

name() # Call the main function
