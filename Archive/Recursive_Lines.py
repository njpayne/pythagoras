# Write a recursive function that accepts an integer argument, n.
# The function should display n lines of asterisks on the screen, with the first line
# showing 1 asterisk, the second line showing 2 asterisks, up to the nth line which 
# shows n asterisks.

def main(): # The main function
	y = int(input("Please input the number of asterisks that you want to start from! "))
	x = int(input("Please input the number of asterisks that you would like to draw! "))
	ast(y, x) # Call the asterisk generator function

#def ast(a): # def ast(a) defined iteratively (non-recursively)
#	for x in range(1,a):
#		print("*" * x)

#def ast(a): # Defined recursively, printing in the opposite direction
#	if a > 0: # Function counts down from a, rather than forward
#		print("*" * a)
#		ast(a-1)

def ast(b, a): # Defined recursively, printing in the correct direction
	if b < (a + 1): # In this case, the user inputs the starting number
		print("*" * b)
		ast(b+1, a) # Recursive function
	else:
		return 0 # Base case
			
main() # Call the main function
