# Create a program that asks the user for their age and the age of their
# best friend. Then, ask the user to return the sum of those ages
# using a function that returns the value in question

def age():
	you = int(input("Please enter your current age: ")) # Input your age
	friend = int(input("Please enter your friends age: ")) # Input your friends age

	print("") # Print a space
	print("The combined age of you an your friends is", 
		add(you, friend), # Call the add function and return the value from it
		"years old")

def add(x, y):
	sum = x + y
	return sum

age() # Call the mainfunction
