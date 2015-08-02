# Write a program to take in a positive integer n > 1 
# from the user and print out whether or not the number the 
# number is a perfect number, an abundant number, or a deficient number.
# A perfect number is one where the sum of its proper divisors 
# (the numbers that divide into it evenly not including itself) 
# equals the number. An abundant number is one where this sum 
# exceeds the number itself and a deficient number is one where this 
# sum is less than the number itself. 
# For example, 28 is perfect since 1 + 2 + 4 + 7 + 14 = 28, 12 is 
# abundant because 1 + 2 + 3 + 4 + 6 = 16 and 16 is deficient because 1 + 2 + 4 + 8 = 15.

def main(): # Define the main function
	num = int(input("Please enter an integer greater than 1: "))
	if num > 1:
	 	print("") # Print a blank space
	 	print("The number you entered is a", abundant(num), "number!")
	else:
		print("") # Print a blank space
		print("The number you entered was below 1.")
		print("Please start the program again & re-enter the number!")

def abundant(a): # Determines the status of the number and returns it
	sum = 0 # Define the initial sum as 0
	# Calculate the sum of the divisors of the entered number
	
	print("Div\tRemai\tSum") # Print table headings

	for x in range(1,a): # Determine the list of proper divisors
		remainder = a % x # Calculate the remainder for each number
		if remainder == 0:
			sum = sum + x # If remainder = 0, number is a proper divisor
			print(x, "\t", remainder, "\t", sum) # Print the value divisor and the remainder 
		else:
			sum = sum + 0 # If remained != 0, number is not a proper divisor
			print(x, "\t", remainder, "\t", sum) # Print the value divisor and the remainder
	
	# Evaluate the sum against a
	if sum == a:
		return "Proper" # Sum of divisors = a
	elif sum > a:
		return "Abundant" # Sum of divisors > a
	else:
		return "Deficient" # Sum of divisors < a
		
main() # Call the main function
