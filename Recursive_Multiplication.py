# Design a recursive function that accepts two integer arguments into the parameters x and y.
# The function should return the value of x times y. Remember multiplication can be performed
# as addition, as 7 x 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4

def main(): # Define the main function
	print("The following program performs recursive multiplication of positive integers!")
	print("Input two numbers and the program will get you the product!")
	x = int(input("Please input the first number: "))
	y = int(input("Please input the second number: "))

	print("") # Print a blank space
	print("The product of", x, "and", y, "is", addition(x, y), "!")

def addition(a,b): # Create the recursive function
	if a == 0:
		return 0 # This is the base case
                # When a = 0, the process stops
	else:
		return b + addition(a-1, b)
                # Note that I add b, a times, recursively

main() # Call the main function
