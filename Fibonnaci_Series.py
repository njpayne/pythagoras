# Develop a recursive algorithm that produces the Fibonnaci sequence
# The sequence can be writeen as 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233
# After the second number, each number in the series is the sum of the previous 2
# Ask the users to print the first n fibonnaci numbers
# If n = 0, then Fib(n) = 0
# If n = 1, then Fib(n) = 1
# If n > 1, then Fib(n) = Fib(n-1) + Fib(n-2)

def main(): # Set the main function
	num = int(input("Please enter the number of numbers you would like to see in the Fibonnaci sequence: "))
	print("Fibonacci Numbers")
	print("------------------")
	
	for x in range(1,num+1): # Loop through all possible fibonacci numbers in the series
		print(fib(x))

def fib(a): # Note that this returns the fibonnaci number for the ath element
	if a == 0: # Define the base case, for Fib(n) = 0
		return 0
	elif a == 1: # Define the case where Fib(n) = 1
		return 1
	else:
		return fib(a-1) + fib(a-2)

main() # Call the main function
