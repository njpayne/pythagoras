# Ackermann's function is a recursive mathematical algorithm that can be used to test how well a system optimizes
# its performance of recursion. Design a function ackermann(m,n), which solves Ackermann's function.
# Use the following logic in your function:
# If m = 0 then return n + 1; if n = 0 then return ackermann(m-1,1)
# Otherwise, return ackermann(m-1, ackermann(m,n-1))
# Once you've designed your function, test it by calling it with small values for m and n

# The Ackermann function is a total computable function that is not primitive recursive
# Primitive recursive functions are defined using primitive recursion and composition as central operations
# Note that its value grows rapidly, even for small inputs. 
# For example A(4,2) is an integer of 19,729 decimal digits.
# It may not be immediately obvious, but the evaluation of A(m, n) always terminates

def main(): # The main function
	x = int(input("Please enter the first item in the pair: "))
	y = int(input("Please enter the second item in the pair: "))
	print(ackermann(x, y)) # Call Ackermann's function

def ackermann(m,n): # Create Ackermann's function
	if m == 0: # if m == 0
		# print(m,n) # Print the next digit
		return (n + 1)
	elif n == 0: # if m > 0 and n = 0
		print(m,n) # Print the next digit
		return ackermann(m-1,1)
	else: # if m > 0 and n > 0
		print(m,n) # Print the next digit
		return ackermann(m-1, ackermann(m,n-1))

main() # Call the main function
