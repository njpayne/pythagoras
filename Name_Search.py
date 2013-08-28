# GirlNames.txt contains a list of the 200 most popular girl names from the year 2009
# BoyNames.txt contains a list of the 200 most popular boy names from the year 2009
# Write a program that reads the content of the two files into two separate lists
# Then, allow the user to enter a a boys name, girls name, or both, search through the
# Relevant list, and let the user know whether the names were among the most popular
# Also, confirm with the user the rank on the list (Assume that the order matches the rank)

def name(): # Create the main search function
	# Open the respective files
	boys = open('BoyNames.txt', 'r') # Note that 'r'= read; 'w' = write; 'a' = append
	girls = open('GirlNames.txt', 'r') # Note that 'r'= read; 'w' = write; 'a' = append

	# Create an empty list of names
	boys_list = [] # Empty
	girls_list = [] # Empty

	# Read in the file contents
	for lines in boys: # This read in the value from every line in boys
		lines = lines.rstrip('\n') # This strips off the '\n' from each line
		boys_list.append(lines) # Append the list of boys names

	for lines in girls: # This reads in the value from every line in girls
		lines = lines.rstrip('\n') # This strips off the '\n' from each line
		girls_list.append(lines) # Append the list of girls names
	
	boys.close() # Close the boys list
	girls.close() # Close the girls list

	# Search for matching names
	print("Thank you for using the naming search engine!")
	name = input("Please enter the name that you would like to search for: ")
	search(name, boys_list, girls_list) # Pass name and lists to the search function

def search(a, boys_list, girls_list): # Create a search function that looks for the name

	if a in (boys_list and girls_list): # Name is in both lists
		print("The name you looked for,", a ,", is on both lists!")
		print("The name", a, "is in the", boys_list.index(a), "position on the boys list!")
		print("The name", a, "is in the", girls_list.index(a), "position on the boys list!")
		
	elif a in boys_list: # Boys list only
		print("The name you looked for,", a ,", is on the boys list!")
		print("The name", a, "is in the", boys_list.index(a), "position on the boys list!")

	elif a in girls_list: # Girls list only
		print("The name you looked for,", a ,", is on the girls list!")
		print("The name", a, "is in the", boys_list.index(a), "position on the boys list!")

	else: # Search returned empty value
		print("Sorry, the name that you entered,", a ,", is not in either of the respective lists!")

name() # Call the main search function

