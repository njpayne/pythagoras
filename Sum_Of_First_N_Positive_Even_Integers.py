# Write a program that asks the user for a positive even integer input n, 
# and the outputs the sum 2+4+6+8+...+n, the sum of all the positive even integers up to n.

def main(): # Define the main function
	n = int(input("Please enter the positive even integer you would like to end with: "))
	
	if n % 2 != 0: # Check that the number entered is even
		print("The number that you entered is not even!")
		print("Please enter an even number!")
	else: # For all odd numbers
		total = 0 # Defines the initial total
		print("Number\tCum_Sum")
		print("-------------------")
		
		for x in range(n,0, -2):
			total = total + x # Cumulative count the sum
			print(x, "\t", total)
			
	print("") # Print a blank space
	print("The total of the numbers you entered is", total) # Print the series total
				
main() # Call the main function
