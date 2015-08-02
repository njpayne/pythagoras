# Write a recursive Python function that returns the sum of the first n integers. 
# Allow the user to specify which number n is.

def main(): # Define the main function
	x = int(input("Please enter the number of intergers you would like to count to: "))
	print("The sum of the first n integers is:", recursive(x), "!")

def recursive(a):
	if a == 0: # Define the base case
		return 0
	else:
		print(a) # Print for error checking
		return a + recursive(a-1) # Implement the recursive element

main() # Call the main function
