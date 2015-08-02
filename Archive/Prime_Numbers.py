# A prime number is a number that is only evenly divisible by itself and 1.
# Write a Boolean function named is_prime() which takes an integer and determines
# if the integer is prime (returns True). Recall that the % operator divides
# one number by another number and returns the remainder in the divisor. In 
# an expression such as num1 % num2, the % operator will return 0 if num1 is
# evenly divisible by num2

# a number is prime if it is greater than one and if none of 2, 3, ..., n − 1 
# divides n (without remainder)

def main():
	num = int(input("Please enter the integer that you wish to evaluate: "))

	print("You entered the integer", num)
	print("This integer is a", named_is_prime(num), "number!")

def named_is_prime(x):
	result = "prime" # Define the base case

	if x <= 1: # Confirm that the number is greater than 1
		result = "non-prime"
		return result # The number is not a prime number
	else:
		for a in range(2,x): # Check case 2 where divisor is zero
			remainder = x % a # Calculate the remainder
			# print(x, a, remainder) # Optional for trouble shooting
			while remainder == 0:
				result = "non-prime" # The number is non prime
				return result

	return result # Return the base case if non of the conditions are met
	                
main() # Call the main function
