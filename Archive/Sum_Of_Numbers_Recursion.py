# Design a function that accepts an integer argument and returns the sum of all the integers from
# 1 up to the number passed as an argument. For example, if 50 is passed as an argument, the function
# will rturn the sum of 1, 2, 3, 4, .... 50. Use recursion to calculate the sum.

def main():
	start = int(input("Please enter the number you would like to start at: "))
	finish = int(input("Please enter the integer you would like to sum to: "))
	print("The sum of all numbers from", start, "to", finish, "is", sum(start, finish), "!")
	
def sum(x, y): # x = start and y = #finish
	if x > y: # If start > finish, add 0 to the sum
		return 0 # Define the base case
	else:
		return x + sum(x+1, y) # Implement recursive functionality

main() # Call the main function
